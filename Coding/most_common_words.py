import pandas as pd
from collections import Counter
import re

def clean_text(text):
    # Remove special characters and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def most_common_words(file_path, top_n=10):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Initialize a Counter to store word frequencies
    word_counter = Counter()
    
    for review in data['review_text']:
        # Clean and split each review into words
        cleaned_review = clean_text(review)
        words = cleaned_review.split()
        # Update word counter
        word_counter.update(words)
    
    # Get the most common words
    return word_counter.most_common(top_n)

# Example usage:
# most_common_words('path_to_csv_file.csv', top_n=5)
