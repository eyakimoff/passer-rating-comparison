from data_cleaning import get_dataframe
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc

df = get_dataframe()


df["Outcome"] = df["Outcome"].map({"W": 1, "L": 0})

# Drop rows where 'Outcome' is NaN (Tie, 13 total ties)
df = df.dropna(subset=["Outcome"])


# Correlation
traditional_corr = df["Passer Rating"].corr(df["Outcome"])
refined_corr = df["Refined Passer Rating"].corr(df["Outcome"])
print(traditional_corr)
print(refined_corr)

X_traditional = df[["Passer Rating"]]
X_refined = df[["Refined Passer Rating"]]
y = df["Outcome"]

# Split data into training and testing sets
X_train_trad, X_test_trad, y_train, y_test = train_test_split(
    X_traditional, y, test_size=0.2, random_state=42
)
X_train_ref, X_test_ref, y_train, y_test = train_test_split(
    X_refined, y, test_size=0.2, random_state=42
)

# train logistic regression models
model_trad = LogisticRegression()
model_trad.fit(X_train_trad, y_train)

model_ref = LogisticRegression()
model_ref.fit(X_train_ref, y_train)

# Predictions
y_pred_trad = model_trad.predict(X_test_trad)
y_pred_ref = model_ref.predict(X_test_ref)

# evaluate metrics
print("Traditional Rating Model:")
print(classification_report(y_test, y_pred_trad))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_trad))

print("Refined Rating Model:")
print(classification_report(y_test, y_pred_ref))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred_ref))

# ROC Curve for Traditional
y_prob_trad = model_trad.predict_proba(X_test_trad)[:, 1]
fpr_trad, tpr_trad, _ = roc_curve(y_test, y_prob_trad)
roc_auc_trad = auc(fpr_trad, tpr_trad)

# ROC Curve for Refined
y_prob_ref = model_ref.predict_proba(X_test_ref)[:, 1]
fpr_ref, tpr_ref, _ = roc_curve(y_test, y_prob_ref)
roc_auc_ref = auc(fpr_ref, tpr_ref)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(fpr_trad, tpr_trad, label=f"Traditional (AUC = {roc_auc_trad:.2f})")
plt.plot(fpr_ref, tpr_ref, label=f"Refined (AUC = {roc_auc_ref:.2f})")
plt.plot([0, 1], [0, 1], "k--")  # Diagonal for random guessing
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.show()
