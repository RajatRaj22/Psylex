import pandas as pd
import re
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)

    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if w not in stop_words]

    return " ".join(tokens)


# Load dataset
df = pd.read_csv("data/essays.csv", encoding="latin1")

# Clean TEXT column
df["clean_text"] = df["TEXT"].apply(clean_text)

# Save processed dataset
df.to_csv("data/cleaned_data.csv", index=False)

print("Data preprocessing completed")