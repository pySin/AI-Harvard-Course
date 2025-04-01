import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Features (hours studied)
X = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]).reshape(-1, 1)

# Labels (0 = fail, 1 = pass)
y = np.array([0, 0, 0, 0, 1, 0, 1, 1, 1, 1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"X train: {X_train}")
print(f"X test: {X_test}")
print(f"Y train: {y_train}")
print(f"Y test: {y_test}")

X_test = [[6]]

model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)
print("Predicted labels:", y_pred)

# Predict probability (confidence score)
y_proba = model.predict_proba(X_test)
print("Probability (fail, pass):", y_proba)

# Plot data points
plt.scatter(X, y, color='blue', label='Actual')

# Plot predicted probabilities
X_range = np.linspace(0, 5, 100).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]
plt.plot(X_range, y_prob, color='red', label='Logistic Curve')

plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()
