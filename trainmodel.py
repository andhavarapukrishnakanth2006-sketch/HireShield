import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline


# ============================================================
# HIREShIELD - FAKE JOB POSTING DETECTOR
# Model Training Script
# ============================================================


# ============================================================
# 1. LOAD DATASET
# ============================================================

print("Loading dataset...")

df = pd.read_csv("data/fake_job_postings.csv")

print("Dataset loaded successfully!")
print(f"Total job postings: {len(df)}")


# ============================================================
# 2. SELECT IMPORTANT TEXT COLUMNS
# ============================================================

text_columns = [
    "title",
    "company_profile",
    "description",
    "requirements",
    "benefits"
]


# ============================================================
# 3. HANDLE MISSING VALUES
# ============================================================

print("\nHandling missing values...")

for column in text_columns:
    df[column] = df[column].fillna("")


# ============================================================
# 4. COMBINE TEXT COLUMNS
# ============================================================

print("Combining job posting information...")

df["job_text"] = df[text_columns].agg(" ".join, axis=1)


# ============================================================
# 5. DEFINE INPUT AND TARGET
# ============================================================

X = df["job_text"]
y = df["fraudulent"]


# ============================================================
# 6. SPLIT DATA INTO TRAINING AND TESTING SETS
# ============================================================

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ============================================================
# 7. CREATE MACHINE LEARNING PIPELINE
# ============================================================

print("\nCreating ML pipeline...")

model = Pipeline([
    # Convert text into numerical TF-IDF features
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=50000,
            ngram_range=(1, 2)
        )
    ),

    # Classification algorithm
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            class_weight="balanced"
        )
    )
])


# ============================================================
# 8. TRAIN MODEL
# ============================================================

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# ============================================================
# 9. MAKE PREDICTIONS
# ============================================================

print("\nTesting model...")

y_pred = model.predict(X_test)


# ============================================================
# 10. CALCULATE ACCURACY
# ============================================================

accuracy = accuracy_score(y_test, y_pred)


# ============================================================
# 11. DISPLAY MODEL PERFORMANCE
# ============================================================

print("\n")
print("=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.2%}")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        target_names=["Genuine", "Fake"]
    )
)


# ============================================================
# 12. SAVE TRAINED MODEL
# ============================================================

print("\nSaving trained model...")

joblib.dump(
    model,
    "models/job_detector.pkl"
)

print("\nModel saved successfully!")
print("Location: models/job_detector.pkl")


# ============================================================
# 13. FINISHED
# ============================================================

print("\n")
print("=" * 50)
print("HIREShIELD MODEL TRAINING COMPLETE")
print("=" * 50)