import numpy as np

class TreeNode:
    def __init__(self, feature_index=None, threshold=None, value=None, left=None, right=None):
        self.feature_index = feature_index  # Index of feature to split on
        self.threshold = threshold          # Threshold value for binary split
        self.value = value                  # Class label for leaf node
        self.left = left                    # Left child node
        self.right = right                  # Right child node

class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def entropy(self, y):
        unique_labels, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return entropy

    def information_gain(self, X, y, feature_idx, threshold):
        total_entropy = self.entropy(y)
        left_indices = np.where(X[:, feature_idx] <= threshold)[0]
        right_indices = np.where(X[:, feature_idx] > threshold)[0]
        left_entropy = self.entropy(y[left_indices])
        right_entropy = self.entropy(y[right_indices])
        weighted_entropy = (len(left_indices) / len(X)) * left_entropy + (len(right_indices) / len(X)) * right_entropy
        information_gain = total_entropy - weighted_entropy
        return information_gain

    def find_best_split(self, X, y):
        num_features = X.shape[1]
        best_information_gain = -np.inf
        best_feature_idx = None
        best_threshold = None
        for feature_idx in range(num_features):
            thresholds = np.unique(X[:, feature_idx])
            for threshold in thresholds:
                current_information_gain = self.information_gain(X, y, feature_idx, threshold)
                if current_information_gain > best_information_gain:
                    best_information_gain = current_information_gain
                    best_feature_idx = feature_idx
                    best_threshold = threshold
        return best_feature_idx, best_threshold

    def build_tree(self, X, y, depth=0):
        if depth == self.max_depth or len(np.unique(y)) == 1:
            leaf_value = np.argmax(np.bincount(y))
            return TreeNode(value=leaf_value)
        
        feature_idx, threshold = self.find_best_split(X, y)
        if feature_idx is None:
            leaf_value = np.argmax(np.bincount(y))
            return TreeNode(value=leaf_value)
        
        left_indices = np.where(X[:, feature_idx] <= threshold)[0]
        right_indices = np.where(X[:, feature_idx] > threshold)[0]

        left_subtree = self.build_tree(X[left_indices], y[left_indices], depth+1)
        right_subtree = self.build_tree(X[right_indices], y[right_indices], depth+1)

        return TreeNode(feature_index=feature_idx, threshold=threshold, left=left_subtree, right=right_subtree)

    def fit(self, X, y):
        self.tree = self.build_tree(X, y)

    def predict_sample(self, x, node):
        if node.value is not None:
            return node.value
        if x[node.feature_index] <= node.threshold:
            return self.predict_sample(x, node.left)
        else:
            return self.predict_sample(x, node.right)

    def predict(self, X):
        if self.tree is None:
            raise ValueError("Tree not fitted.")
        predictions = []
        for x in X:
            prediction = self.predict_sample(x, self.tree)
            predictions.append(prediction)
        return np.array(predictions)

if __name__ == "__main__":
    X = np.array([[1, 0], [1, 1], [0, 0], [0, 1]])
    y = np.array([1, 1, 0, 0])

    tree = DecisionTreeClassifier(max_depth=1)
    tree.fit(X, y)

    print("Tree structure:")
    print("Root feature index:", tree.tree.feature_index)
    print("Root threshold:", tree.tree.threshold)

    test_samples = np.array([[1, 0], [0, 1]])
    predictions = tree.predict(test_samples)
    print("Predictions for test samples:", predictions)
