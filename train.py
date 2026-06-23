from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("Loading dataset...")

dataset = fetch_20newsgroups(
    subset='all',
    remove=('headers', 'footers', 'quotes')
)

X = dataset.data
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        max_df=0.7,
        min_df=2,
        ngram_range=(1,2)
    )),
    ("classifier", LinearSVC())
])

print("Training model...")

model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\nAccuracy :", round(accuracy*100,2),"%")

print("\nClassification Report\n")
print(classification_report(y_test,prediction))

joblib.dump(model,"document_classifier.pkl")
joblib.dump(dataset.target_names,"categories.pkl")

print("\nModel Saved Successfully!")