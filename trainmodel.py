from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Simple training data
texts = [
    # Positive
    "I love this product",
    "This is amazing",
    "Very happy with the service",
    "Excellent experience",
    "Absolutely fantastic",
    "I really enjoyed this",
    "Great service and support",

    # Negative
    "I hate this",
    "This is terrible",
    "Very bad experience",
    "Worst service ever",
    "This service was horrible",
    "I am very disappointed",
    "Extremely poor quality",
    "Not satisfied at all",

    # Neutral
    "It is okay",
    "Average experience",
    "Not bad but not good",
    "It works fine",
    "Nothing special"
]

labels = [
    "Positive","Positive","Positive","Positive","Positive","Positive","Positive",
    "Negative","Negative","Negative","Negative","Negative","Negative","Negative","Negative",
    "Neutral","Neutral","Neutral","Neutral","Neutral"
]


# Create ML pipeline
model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(texts, labels)

# Save trained model (NO underscore)
joblib.dump(model, "sentimentmodel.pkl")

print("Model trained and saved as sentimentmodel.pkl")
