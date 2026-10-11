import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC


df = pd.read_csv("data/resume_skill_gap_dataset_v2.csv")
X = df["text"]
y = df["job_role"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
print("Training TF-IDF shape:", X_train_tfidf.shape)
print("Testing TF-IDF shape:", X_test_tfidf.shape)


model = LogisticRegression(
    max_iter=1000,
    random_state=42
)
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Predictions completed!")

nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
nb_pred = nb_model.predict(X_test_tfidf)
nb_accuracy = accuracy_score(y_test, nb_pred)
print("\nNaive Bayes Accuracy:", nb_accuracy)
print("\nNaive Bayes Classification Report:")
print(classification_report(y_test, nb_pred))

svm_model = LinearSVC(random_state=42)
svm_model.fit(X_train_tfidf, y_train)
svm_pred = svm_model.predict(X_test_tfidf)
svm_accuracy = accuracy_score(y_test, svm_pred)
print("\nSVM Accuracy:", svm_accuracy)
print("\nSVM Classification Report:")
print(classification_report(y_test, svm_pred))