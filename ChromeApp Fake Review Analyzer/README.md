Chromeapp postive Review Analyser with one star rating
There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating.

The goal is to identify such ratings where review text is good, but rating is negative- so that the support team can point this to users.

In this project I have made use of codes which I used for sentiment Analysis of IMDB dataset and also from Google & stack overflow which includes the following steps:

1.Replace short words

2.Remove Punctuation

3.Making text lower case

4.Remove stopwords

5.Lemmatization

6.Sentiment Analyzer

7.Bag of words Model (one gram and tf-idf)

8.Word Cloud

9 Model Building

With the help of streamlit-authenticator package I created Login authentication to access the application and deployed it uisng Streamlit.

Access the live application link below:
https://share.streamlit.io/akkijd/nextgrowthlabs-assignments/main/chromeapp-review/app.py

Once the above link is loaded, you can see a login screen as shown below. Enter the below given credentials there. Login

Authentication
Username: nlabs or avijayan

Password: 98765 or 98765

Once you enter the credentials correctly you will be able to see the below page. We can add both CSV & Xlsx files in this application.

chromeapp
