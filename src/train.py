import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor

from embeddings import generate_embeddings

data = pd.read_csv("data/cleaned_data.csv")

# convert labels
trait_cols = ["cEXT","cNEU","cAGR","cCON","cOPN"]

for col in trait_cols:
    data[col] = data[col].map({"y":1, "n":0})

texts = data["clean_text"]

X = generate_embeddings(texts)

y = data[trait_cols]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = MultiOutputRegressor(RandomForestRegressor())

model.fit(X_train, y_train)

joblib.dump(model, "models/personality_model.pkl")

print("Model training complete")