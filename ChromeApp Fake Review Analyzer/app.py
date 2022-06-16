import re
import pickle
# import nltkmodule
import nltk
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# # --- USER AUTHENTICATION ---
names = ["Akhilesh Vijayan", "Nextlabs"]
usernames = ["avijayan", "nlabs"]
#
# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "user", "sig_key")


name, authentication_status, usernames = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:


 def main():
    """Function for file upload"""
    #logout button in main
    authenticator.logout("Log out","sidebar")
    st.sidebar.title(f"Welcome {name}!! :sunglasses:")

    global df
    # title
    st.title("ChromeApp fake review Analyzer")
    menu = ["CSV File","Xlsx File"]
    choice = st.selectbox("Menu", menu)

    if choice == "CSV File":
        st.subheader("CSV File")
        file = st.file_uploader("Upload CSV", type=["csv"])
        if st.button("process"):
            if file is not None:
                df = pd.read_csv(file)
                st.dataframe(df.head(5))

    elif choice == "Xlsx File":
        st.subheader("Xlsx File")
        file = st.file_uploader("Upload Xlsx file", type=["xlsx"])
        if st.button("Process"):
            if file is not None:
                df = pd.read_excel(file)
                st.write(df.head(5))
    try:
     feature = ['ID', 'Review URL', 'Thumbs Up', 'User Name', 'Developer Reply', 'Version', 'Review Date', 'App ID']
     df.drop(feature, axis=1, inplace=True)
     # Dropping null values
     df.dropna(subset=['Text'], inplace=True)
     #Replacing short words
     def decontracted(phrase):
         sen = []
         for sentence in phrase:
             sentence = re.sub(r"won\'t", "will not", sentence)
             sentence = re.sub(r"Won\'t", "will not", sentence)
             sentence = re.sub(r"WON\'T", "will not", sentence)
             sentence = re.sub(r"can\'t", "cannot", sentence)
             sentence = re.sub(r"Can\'t", "cannot", sentence)
             sentence = re.sub(r"CAN\'T", "cannot", sentence)

             # general
             sentence = re.sub(r"n\'t", " not", sentence)
             sentence = re.sub(r"\'re", " are", sentence)
             sentence = re.sub(r"\'s", " is", sentence)
             sentence = re.sub(r"\'d", " would", sentence)
             sentence = re.sub(r"\'ll", " will", sentence)
             sentence = re.sub(r"\'t", " not", sentence)
             sentence = re.sub(r"\'ve", " have", sentence)
             sentence = re.sub(r"\'m", " am", sentence)
             sen.append(sentence)
         return sen

     text = df["Text"]

     result = decontracted(text)

     df["Text_processed"] = result

     ##shotword removal
     df['Text_processed'] = df['Text_processed'].apply(
         lambda row: ' '.join([word for word in row.split() if len(word) > 2]))

     # Removing Punctuation(.!<>{}’,”(/)-)

     df['Text_processed'] = df['Text_processed'].str.replace("[^a-zA-Z0-9]", " ")

     # Re-ordering columns
     df = df[['Text', 'Text_processed', 'Star']]
     # Converting to lowercase characters
     df['Text_processed'] = [text.lower() for text in df['Text_processed']]

     # Begin Lemmatization


     # function to convert nltk tag to wordnet tag
     lemmatizer = WordNetLemmatizer()

     # Finds the part of speech tag
     # Convert the detailed POS tag into a shallow information
     def nltk_tag_to_wordnet_tag(nltk_tag):
         if nltk_tag.startswith('J'):
             return wordnet.ADJ
         elif nltk_tag.startswith('V'):
             return wordnet.VERB
         elif nltk_tag.startswith('N'):
             return wordnet.NOUN
         elif nltk_tag.startswith('R'):
             return wordnet.ADV
         else:
             return None

     # lemmatize sentence using pos tag
     def lemmatize_sentence(sentence):
         # word tokenize -> pos tag (detailed) -> wordnet tag (shallow pos) -> lemmatizer -> root word
         # tokenize the sentence and find the POS tag for each token
         nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
         # tuple of (token, wordnet_tag)
         wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
         lemmatized_sentence = []
         for word, tag in wordnet_tagged:
             if tag is None:
                 # if there is no available tag, append the token as is
                 lemmatized_sentence.append(word)
             else:
                 # else use the tag to lemmatize the token
                 lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
         return " ".join(lemmatized_sentence)

     df['Text_processed'] = df['Text_processed'].apply(lambda x: lemmatize_sentence(x))

     # Remove stop words

     stop_words=stopwords.words('english')
     stop_words.remove("not")
     stop_words.remove("no")
     # Making custom list of words to be removed
     add_words = ['chrome', 'download', 'google', 'aap', 'app', 'ads', 'one', 'make', 'even', 'like', 'see', 'get',
                  'make',
                  ]

     # Adding to the list of words
     stop_words.extend(add_words)

     # Function to remove stop words

     def remove_stopwords(rev):
         # iNPUT : IT WILL TAKE ROW/REVIEW AS AN INPUT
         # take the paragraph, break into words, check if the word is a stop word, remove if stop word, combine the words into a para again
         review_tokenized = word_tokenize(rev)
         rev_new = " ".join([word for word in review_tokenized if word not in stop_words])
         return rev_new

     # Removing stopwords
     df['Text_processed'] = [remove_stopwords(r) for r in df['Text_processed']]

     sid = SentimentIntensityAnalyzer()

     sentiment = []

     for sen in df["Text_processed"]:
         score = sid.polarity_scores(sen)
         # blob_score = TextBlob(sen).sentiment.polarity
         if (score['pos'] >= 0.5):
             sentiment.append('Positive')
         else:
             sentiment.append('Negative')

     df["sentiment"] = sentiment

     one_rating_review = df[df.Star == 1]
     one_rating_review.reset_index(drop=True)

     positive_review_one_star_rating = one_rating_review[one_rating_review.sentiment == 'Positive']
     positive_review_one_star_rating = positive_review_one_star_rating[["Text_processed", "Star", "sentiment"]]
     positive_review_one_star_rating.reset_index(drop=True)
     st.subheader("Chromeapp positive review with one star rating")
     st.write(positive_review_one_star_rating)


    except Exception as e:
      print(e)
    #cd C:\Users\LENOVO\PycharmProjects\streamlitcd

 if __name__ == '__main__':
  main()

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
