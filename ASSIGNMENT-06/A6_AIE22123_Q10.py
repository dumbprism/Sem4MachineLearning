from sklearn.neural_network import MLPClassifier
import numpy as np
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
X_xor = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_xor = np.array([0, 1, 1, 0])
and_classifier = MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', max_iter=10000)
and_classifier.fit(X_and, y_and)
xor_classifier = MLPClassifier(hidden_layer_sizes=(4,), activation='logistic', max_iter=10000)
xor_classifier.fit(X_xor, y_xor)
print("AND gate predictions:", and_classifier.predict(X_and))
print("XOR gate predictions:", xor_classifier.predict(X_xor))
