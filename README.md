#  AI Document Classifier
# AI Document Classifier

## Live Demo

(https://document-classifier-vmggh4antvj3wkf42dr9mr.streamlit.app/)

##  Project Overview

The AI Document Classifier is a Machine Learning application that automatically classifies text documents into predefined categories. The project uses Natural Language Processing (NLP) techniques to convert textual data into numerical features and applies a Logistic Regression model to predict the category of a given document.

This application provides a simple and interactive web interface built with Streamlit, where users can enter any text and instantly receive the predicted document category.

---

#  Objectives

- Develop an intelligent document classification system.
- Apply Natural Language Processing (NLP) techniques for text preprocessing.
- Convert text into numerical features using TF-IDF Vectorization.
- Train a Machine Learning model to classify documents accurately.
- Deploy the model using Streamlit for real-time predictions.

---

#  Features

- User-friendly web interface.
- Real-time document classification.
- Machine Learning-based prediction.
- TF-IDF feature extraction.
- Logistic Regression classification model.
- Fast and lightweight application.
- Easy to deploy and use.

---

#  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Scikit-learn | Machine Learning |
| Streamlit | Web Application |
| Joblib | Model Saving and Loading |
| NumPy | Numerical Operations |
| Pandas | Data Handling |

---

#  Machine Learning Workflow

1. Load the dataset.
2. Split the dataset into training and testing sets.
3. Convert text into numerical vectors using TF-IDF Vectorizer.
4. Train a Logistic Regression classifier.
5. Evaluate the model using Accuracy Score.
6. Save the trained model.
7. Load the model in the Streamlit application.
8. Predict the category of user-entered text.

---

#  Project Structure

```
document-classifier/
│
├── train.py
├── app.py
├── document_classifier.pkl
├── categories.pkl
├── requirements.txt
├── README.md
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/cchanduvenkatpavan33/document-classifier.git
```

Move into the project folder

```bash
cd document-classifier
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

#  Running the Project

Train the model

```bash
python train.py
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

#  Model Performance

Algorithm Used:

- Logistic Regression

Feature Extraction:

- TF-IDF Vectorizer

Evaluation Metric:

- Accuracy Score

Current Accuracy:

**73.32%**

---

#  Future Enhancements

- Support PDF and DOCX document uploads.
- Improve prediction accuracy using advanced NLP models.
- Add multilingual document classification.
- Integrate Deep Learning models such as LSTM or BERT.
- Store prediction history in a database.
- Deploy using Docker and cloud platforms.

---

# Application Preview

The Streamlit application provides:

- Text input area
- Classify button
- Instant prediction of document category

---

#  Learning Outcomes

Through this project, I learned:

- Natural Language Processing (NLP)
- Text Vectorization using TF-IDF
- Logistic Regression
- Machine Learning Model Training
- Model Serialization using Joblib
- Streamlit Application Development
- GitHub Version Control
- Project Deployment

---

#  Author

**Chandu Venkat Pavan**



---

# 📄 License

This project is developed for educational and internship purposes.
