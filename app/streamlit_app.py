import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.express as px

from src.predict import predict_personality

st.title("🧠 PsyLex Personality Analyzer")

st.write("Analyze personality traits from text using AI.")

text = st.text_area("Enter text to analyze")

if st.button("Analyze Personality"):

    result = predict_personality(text)

    df = pd.DataFrame(
        list(result.items()),
        columns=["Trait", "Score"]
    )

    st.subheader("Predicted Personality Traits")

    st.dataframe(df)

    # Radar chart
    traits = df["Trait"].tolist()
    scores = df["Score"].tolist()

    fig = px.line_polar(
        r=scores,
        theta=traits,
        line_close=True
    )

    fig.update_traces(fill='toself')

    fig.update_layout(title="Personality Radar Profile")

    st.plotly_chart(fig)