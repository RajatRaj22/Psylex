# PsyLex

PsyLex is an AI system that predicts human personality traits from conversational text using Natural Language Processing and Machine Learning.

The system analyzes linguistic patterns and semantic embeddings to estimate the Big Five personality traits.

---

## Features

• NLP text preprocessing  
• Transformer based sentence embeddings  
• Personality prediction using machine learning  
• Interactive Streamlit dashboard  
• Personality trait visualization

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

## Personality Traits Predicted

Openness  
Conscientiousness  
Extroversion  
Agreeableness  
Neuroticism  

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

## Future Improvements

• Personality evolution tracking  
• Explainable AI for predictions  
• Chatbot personality adaptation  
• Multimodal personality analysis