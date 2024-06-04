# Import necessary libraries
import spacy
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the spaCy model
nlp = spacy.load('en_core_web_sm') # Small model
# nlp = spacy.load('en_core_web_lg') # Large model


# Add SpacyTextBlob to the pipeline
nlp.add_pipe('spacytextblob')

# Read the CSV file with low_memory set to False and turn it into Dataframe
df = pd.read_csv("amazon_product_reviews.csv", low_memory=False)

# Select the 'reviews.text' column
reviews_data = df['reviews.text'].dropna()

# Function to preprocess text data
def preprocess_text(text):
    # Create a spaCy document
    doc = nlp(text)

    # Remove stop words and punctuation, and lemmatise tokens
    cleaned_text = " ".join([token.lemma_ for token in doc if token.text not in STOP_WORDS and not token.is_punct])

    return cleaned_text

# Apply preprocessing to the reviews
reviews_data_cleaned = reviews_data.apply(preprocess_text)

# Sentiment Analysis
def analyse_sentiment(text):
    # Create a spaCy document
    doc = nlp(text)
    
    # Get the sentiment polarity and subjectivity
    polarity = doc._.blob.polarity
    subjectivity = doc._.blob.subjectivity
    
    # Determine the sentiment label
    if polarity > 0:
        sentiment = 'Positive'
    elif polarity < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, polarity, subjectivity

# Sample reviews 
sample_reviews = {
    "review": [
        "I absolutely love this product! It has exceeded all my expectations and I couldn't be happier with my purchase.", # Positive sample
        "As a long-time user of this product, I have found it to be adequate for my needs. While it doesn't offer any groundbreaking features, it gets the job done.", # Neutral sample
        "I am very disappointed with this product. It stopped working after just one week and customer service was unhelpful." # Negative sample
    ]
}

# Create DataFrame
sample_df = pd.DataFrame(sample_reviews)

# Iterate through each review in the DataFrame
for index, row in sample_df.iterrows():
    # Preprocess the current review using the preprocess_text function
    cleaned_review = preprocess_text(row['review'])
    
    # Analyze the sentiment of the preprocessed review using the analyse_sentiment function
    sentiment, polarity, subjectivity = analyse_sentiment(cleaned_review)
    
    # Print the sentiment analysis results, including sentiment label, polarity, and subjectivity
    print(f"Sample_Review {index+1}: Sentiment: {sentiment}, Polarity: {polarity}, Subjectivity: {subjectivity}\n")

# Function to compare the similarity of two product reviews
def compare_similarity(review1, review2):
    # Create spaCy documents for each review
    doc1 = nlp(review1)
    doc2 = nlp(review2)
    
    # Calculate the similarity score between the two reviews
    similarity_score = doc1.similarity(doc2)
    
    return similarity_score

# Choose reviews from specific rows
chosen_reviews = reviews_data.iloc[[100, 200]]

# Iterate through each chosen review
for index, review_text in chosen_reviews.items():
    # Preprocess the current review
    cleaned_review = preprocess_text(review_text)
    
    # Analyze the sentiment of the preprocessed review
    sentiment, polarity, subjectivity = analyse_sentiment(cleaned_review)
    
    # Print the sentiment analysis results
    print(f"Review: {review_text}")
    print(f"Preprocessed Text: {cleaned_review}")
    print(f"Sentiment: {sentiment}, Polarity: {polarity}, Subjectivity: {subjectivity}")
    print()

# Compare the similarity of the two chosen reviews
similarity_score = compare_similarity(chosen_reviews.iloc[0], chosen_reviews.iloc[1])
print(f"Similarity Score between the two chosen reviews: {similarity_score}")
