# Automated News Emailer

This app automates the delivery of personalized daily news emails to contacts based on their interests. It fetches recent news articles from the NewsAPI,
and sends customized email digests to recipients listed in a Excel contacts sheet.

## How it Works
The app performs the following steps:

1. Parses an Excel file containing a contacts list with columns for First Name, Last Name, Email, and Interests.
2. Queries the NewsAPI for the latest headlines related to each interest.
3. Compiles a daily newsletter email for each contact.
4. Sends individual emails to each recipient with news tailored to their specified interests.

## Setup
1. Clone this repo
2. Create a NewsAPI account and get your API key
3. Add your API key and the sender's email credentials (to .ENV)
4. Set the path to your Excel contact list
5. Run main.py to send the first batch of emails
