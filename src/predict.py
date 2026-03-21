import joblib

# Load trained model + SAME vectorizer
model = joblib.load("models/personality_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_personality(text):

    # 🔥 IMPORTANT: use transform NOT fit_transform
    embedding = vectorizer.transform([text]).toarray()

    prediction = model.predict(embedding)[0]

    traits = [
        "Extroversion",
        "Neuroticism",
        "Agreeableness",
        "Conscientiousness",
        "Openness"
    ]

    return dict(zip(traits, prediction))