import joblib
from src.embeddings import generate_embeddings

# Load trained model
model = joblib.load("models/personality_model.pkl")

# Map dataset labels → real personality names
trait_mapping = {
    "cEXT": "Extroversion",
    "cNEU": "Neuroticism",
    "cAGR": "Agreeableness",
    "cCON": "Conscientiousness",
    "cOPN": "Openness"
}

def predict_personality(text):

    embedding = generate_embeddings([text])

    prediction = model.predict(embedding)[0]

    # Convert results to readable labels
    result = dict(zip(trait_mapping.values(), prediction))

    return result