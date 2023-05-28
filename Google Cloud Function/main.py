#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import jsonify

# Load the English language model for spaCy
nlp = spacy.load('en_core_web_sm')

# Function to extract lemma features from the input text
def extract_features_lemma(text):
    doc = nlp(text)
    features = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(features)

# Function to compute similarity scores between input text and dataset
def compute_similarity(input_text, dataset):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(dataset)
    input_vector = vectorizer.transform([input_text])

    similarity_scores = cosine_similarity(X, input_vector)
    return similarity_scores

# Flask route to handle the request and return similar items
def get_similar_items(request):
    request_json = request.get_json()
    if request_json and 'text' in request_json and 'top_n' in request_json:
        input_text = request_json['text']
        top_n = request_json['top_n']
        
        # Read the dataset from a CSV file
        df = pd.read_csv('clothing-final.csv')
        product_descriptions = df['Product_Description']
        product_links = df['Product_Link']
        
        # Extract lemma features from the product descriptions
        lemma_features = product_descriptions.apply(extract_features_lemma)
        
        # Compute similarity scores between input text and dataset
        similarity_scores = compute_similarity(input_text, lemma_features)
        
        # Get the top N indices with highest similarity scores
        top_indices = similarity_scores.argsort(axis=0).flatten()[-top_n:]
        
        # Get the corresponding product links for the top indices
        top_links = product_links.iloc[top_indices].tolist()
        
        # Create a JSON response with the ranked links
        response = {'ranked_links': top_links}
        return jsonify(response)
    else:
        # Return an error response for invalid requests
        return jsonify({'error': 'Invalid request. Please provide a "text" and "top_n" parameter in the JSON payload.'}), 400


# In[ ]:
