import numpy as np

class DecisionTreeRootFinder:
    def __init__(self):
        pass

    def entropy(self, y):
    
        unique_labels, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return entropy

    def information_gain(self, X, y, feature_idx):
    
        total_entropy = self.entropy(y)
        unique_values, value_counts = np.unique(X[:, feature_idx], return_counts=True)
        weighted_entropy = 0
        for value, count in zip(unique_values, value_counts):
            subset_indices = np.where(X[:, feature_idx] == value)[0]
            subset_entropy = self.entropy(y[subset_indices])
            weighted_entropy += (count / len(X)) * subset_entropy
        information_gain = total_entropy - weighted_entropy
        return information_gain

    def find_root_feature(self, X, y):
       
        num_features = X.shape[1]
        best_feature_idx = None
        best_information_gain = -np.inf
        for feature_idx in range(num_features):
            current_information_gain = self.information_gain(X, y, feature_idx)
            if current_information_gain > best_information_gain:
                best_information_gain = current_information_gain
                best_feature_idx = feature_idx
        return best_feature_idx

if __name__ == "__main__":
    X = np.array([[1, 0], [1, 1], [0, 0], [0, 1]])
    y = np.array([1,1,1,1])
    tree_root_finder = DecisionTreeRootFinder()
    root_feature_idx = tree_root_finder.find_root_feature(X, y)
    print("Root feature index:", root_feature_idx)
