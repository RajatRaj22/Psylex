import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

model = joblib.load("models/personality_model.pkl")

vectorizer = TfidfVectorizer(max_features=5000)

def predict_personality(text):

    embedding = vectorizer.fit_transform([text]).toarray()

    prediction = model.predict(embedding)[0]

    traits = [
        "Extroversion",
        "Neuroticism",
        "Agreeableness",
        "Conscientiousness",
        "Openness"
    ]

    return dict(zip(traits, prediction))