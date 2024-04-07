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

    def equal_width_binning(self, feature, num_bins):

        min_val = np.min(feature)
        max_val = np.max(feature)
        bin_width = (max_val - min_val) / num_bins
        bins = [min_val + i * bin_width for i in range(num_bins)]
        binned_feature = np.digitize(feature, bins)
        return binned_feature

    def frequency_binning(self, feature, num_bins):
        
        sorted_indices = np.argsort(feature)
        bin_size = len(feature) // num_bins
        binned_feature = np.zeros_like(feature)
        for i in range(num_bins):
            start_idx = i * bin_size
            end_idx = start_idx + bin_size if i < num_bins - 1 else len(feature)
            binned_feature[sorted_indices[start_idx:end_idx]] = i
        return binned_feature

    def find_root_feature(self, X, y, binning_type='equal_width', num_bins=None):
       
        if binning_type == 'equal_width':
            binning_function = self.equal_width_binning
        elif binning_type == 'frequency':
            binning_function = self.frequency_binning
        else:
            raise ValueError("Invalid binning type. Choose 'equal_width' or 'frequency'.")

        if num_bins is None:
            num_bins = int(np.sqrt(len(X)))  # Default number of bins

        num_features = X.shape[1]
        best_feature_idx = None
        best_information_gain = -np.inf
        for feature_idx in range(num_features):
            if len(np.unique(X[:, feature_idx])) > 1:  # Skip features with only one unique value
                binned_feature = binning_function(X[:, feature_idx], num_bins)
                current_information_gain = self.information_gain(binned_feature.reshape(-1, 1), y, 0)
                if current_information_gain > best_information_gain:
                    best_information_gain = current_information_gain
                    best_feature_idx = feature_idx
        return best_feature_idx

# Example usage
if __name__ == "__main__":
    X = np.array([[1, 0], [1, 1], [0, 0], [0, 1]])
    y = np.array([1, 0, 1, 0])

    tree_root_finder = DecisionTreeRootFinder()
    root_feature_idx = tree_root_finder.find_root_feature(X, y, binning_type='equal_width', num_bins=2)
    print("Root feature index:", root_feature_idx)
