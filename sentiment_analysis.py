# sentiment_analysis.py
# Simple Sentiment Analysis Project - Harshit Shukla

import nltk
from textblob import TextBlob

# Download resources
nltk.download('punkt')

# Sample reviews
reviews = [
    "I love this product, it's amazing!",
    "Worst experience ever, I hate it.",
    "The app is okay, but could be better.",
    "Absolutely fantastic service!"
]

print("---- Sentiment Analysis Results ----")
for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😡"
    else:
        sentiment = "Neutral 😐"
    print(f"{review} => {sentiment}")
