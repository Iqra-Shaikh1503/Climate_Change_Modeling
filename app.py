import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model and vectorizer
model = joblib.load('notebook\\best_sentiment_model.pkl')
vectorizer = joblib.load('notebook\\tfidf_vectorizer.pkl')

# Set up the Streamlit app
st.set_page_config(page_title="Sentiment Analysis", page_icon="💬", layout="centered")
st.title("💬 Sentiment Analysis on Climate Change Comments")

st.markdown("""
Enter a comment or sentence related to climate change, and this app will predict whether the sentiment is **positive**, **neutral**, or **negative**.
""")

# Input box
user_input = st.text_area("✏️ Enter your comment here:", height=150)

# Prediction
if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Vectorize input text
        vectorized_input = vectorizer.transform([user_input])
        
        # Predict
        prediction = model.predict(vectorized_input)[0]
        probas = model.predict_proba(vectorized_input)[0]
        confidence = np.max(probas) * 100

        # Show results
        st.success(f"**Predicted Sentiment:** {prediction.capitalize()}")
        st.info(f"Confidence: {confidence:.2f}%")

        st.markdown("### 🔍 Probability for each class:")
        st.json({
            label: f"{p * 100:.2f}%" for label, p in zip(model.classes_, probas)
        })

# Show probabilities
        st.subheader("🔍 Class Probabilities")
        prob_df = pd.DataFrame({
            'Sentiment': model.classes_,
            'Probability': probas * 100
        })

        st.dataframe(prob_df.style.format({"Probability": "{:.2f}%"}))

        # Visual
        st.bar_chart(prob_df.set_index("Sentiment"))

        # Optionally color output
        if confidence < 50:
            st.info("The model seems **uncertain** about this prediction.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and scikit-learn")
