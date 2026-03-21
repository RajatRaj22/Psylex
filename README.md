# PsyLex

PsyLex is an AI system that predicts human personality traits from conversational text using Natural Language Processing and Machine Learning.

The system analyzes linguistic patterns and semantic embeddings to estimate the Big Five personality traits.

---

## 🚀 Live Demo
👉 https://https://psylex.onrender.com

---

## Features

- Predicts Big Five traits:
  - Extroversion
  - Neuroticism
  - Agreeableness
  - Conscientiousness
  - Openness
- Real-time text analysis
- Interactive visualization using Plotly
- Lightweight and production-ready pipeline

---

## 🧠 How It Works
1. Input text is preprocessed using NLP techniques
2. TF-IDF vectorizer converts text into numerical features
3. Multi-output regression model predicts personality traits
4. Results are visualized in an interactive radar chart

---

## Tech Stack

Python  
NLTK  
Sentence Transformers  
Scikit-learn  
Streamlit  
Pandas  
NumPy  

---

## Project Architecture

User Text  
↓  
Text Preprocessing  
↓  
Sentence Embeddings  
↓  
Machine Learning Model  
↓  
Personality Trait Prediction  
↓  
Visualization Dashboard

---

## 🏗️ Key Engineering Highlights
- Maintained consistency between training and inference by saving and reusing the same TF-IDF vectorizer
- Handled real-world deployment challenges including dependency conflicts and environment issues
- Optimized system for production by removing heavy dependencies and ensuring stability

---

## Installation

Clone repository

git clone https://github.com/rajatraj22/psylex.git

cd psylex

Install dependencies

pip install -r requirements.txt

---

## Run Project

Step 1: Preprocess Data

python src/preprocess.py

Step 2: Train Model

python src/train.py

Step 3: Run Application

streamlit run app/streamlit_app.py

---

## 📊 Example Input

I enjoy working in teams and love exploring new ideas.

---

## 📈 Future Improvements

- Add transformer-based embeddings (BERT)
- Introduce explainability (SHAP/LIME)
- Improve UI/UX for better interaction
