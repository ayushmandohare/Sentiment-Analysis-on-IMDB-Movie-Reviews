import streamlit as st
import pickle

# Load trained model and vectorizer
with open("sentiment_svm_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# App Title
st.set_page_config(page_title="Sentiment Analysis App", page_icon="📝", layout="centered")
st.title("📝 Sentiment Analysis on Reviews")
st.write("Enter a review below and let the SVM model predict its sentiment!")

# Input
user_input = st.text_area("✍️ Write your review here:")

# Prediction
if st.button("Predict Sentiment"):
    if user_input.strip() != "":
        X = vectorizer.transform([user_input])
        prediction = model.predict(X)[0]

        # Display result
        if prediction == "positive":
            st.success("✅ Prediction: Positive Sentiment")
        else:
            st.error("❌ Prediction: Negative Sentiment")
    else:
        st.warning("⚠️ Please enter some text to analyze.")
