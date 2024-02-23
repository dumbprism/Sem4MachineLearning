import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
k_values = range(1, 12)
accuracy_scores_knn = []
accuracy_scores_nn = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    accuracy_scores_knn.append(accuracy_knn)
    nn = KNeighborsClassifier(n_neighbors=1)
    nn.fit(X_train, y_train)
    y_pred_nn = nn.predict(X_test)
    accuracy_nn = accuracy_score(y_test, y_pred_nn)
    accuracy_scores_nn.append(accuracy_nn)
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_scores_knn, label='kNN (k=3)', marker='o')
plt.plot(k_values, accuracy_scores_nn, label='Nearest Neighbor (k=1)', marker='*')
plt.title('Accuracy vs. k for kNN and Nearest Neighbor')
plt.xlabel('Value of k')
plt.ylabel('Accuracy')
plt.xticks(k_values)
plt.legend()
plt.grid(True)
plt.show()