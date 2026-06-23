import streamlit as st
import joblib

st.set_page_config(
    page_title="AI Document Classifier",
    page_icon="📄",
    layout="centered"
)

model = joblib.load("document_classifier.pkl")
categories = joblib.load("categories.pkl")

st.title("📄 AI Document Classifier")

st.markdown("""
This application classifies text documents into one of the predefined categories using Machine Learning.

**Model Used:** Linear Support Vector Machine (LinearSVC)

**Feature Extraction:** TF-IDF Vectorization
""")

text = st.text_area("Enter your document here", height=220)

if st.button("Classify Document"):

    if text.strip()=="":

        st.warning("Please enter some text.")

    else:

        prediction = model.predict([text])[0]

        st.success("Prediction Completed Successfully!")

        st.subheader("Predicted Category")

        st.info(categories[prediction])