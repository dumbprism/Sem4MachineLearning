### Assignment -02 
Contributors : 
## Kotamraju Arhant - AIE22123
## Ganganapalli Naveen - AIE22115 [https://github.com/GanganapalliNaveen]
## Aasritha Reddy - AIE22144 [https://github.com/aasritha22144]


### Pseudo Code

```plaintext
FUNCTION euclidean_distance(x, y):
    SET euclid_dist = 0
    FOR EACH element i IN RANGE(length of x):
        UPDATE euclid_dist BY ADDING (x[i] - y[i])^2
    RETURN square root of euclid_dist

FUNCTION manhattan_distance(x, y):
    SET manhattan_dist = 0
    FOR EACH element i IN RANGE(length of x):
        UPDATE manhattan_dist BY ADDING ABS(x[i] - y[i])
    RETURN manhattan_dist

FUNCTION euclidean_dist(point1, point2):
    RETURN square root of ((point1[0] - point2[0])^2 + (point1[1] - point2[1])^2)

FUNCTION KNN(k, coordinates):
    SET distance = empty list
    FOR i FROM 1 TO length of coordinates:
        SET calculated_distance = euclidean_distance(coordinates[0], coordinates[i])
        APPEND (calculated_distance, coordinates[i][2]) TO distance
    FOR j FROM 0 TO length of distance:
        FOR l FROM 0 TO (length of distance - j - 1):
            IF distance[l][0] > distance[l+1][0]:
                SWAP distance[l] WITH distance[l+1]
    SET k_nearest = first k elements of distance
    SET frequency1 = 0
    FOR EACH (a, label) IN k_nearest:
        IF label == 1:
            INCREMENT frequency1
    SET frequency2 = k - frequency1
    IF frequency1 > frequency2:
        RETURN "Belongs to the first class"
    ELSE:
        RETURN "Belongs to the second class"

FUNCTION label_encode(labels):
    SET unique_label = set of unique labels in labels
    SET label_to_code = empty dictionary
    SET code = 0
    FOR EACH label IN unique_label:
        ASSIGN code TO label_to_code[label]
        INCREMENT code
    FOR EACH label IN labels:
        ASSIGN encoded_label = label_to_code[label]
    RETURN encoded_label, label_to_code

FUNCTION hot_encode(labels):
    SET unique_labels = sorted set of unique labels in labels
    SET one_hot_coding = empty dictionary
    FOR EACH label IN unique_labels:
        ASSIGN list of zeros with length equal to number of unique labels TO one_hot_coding[label]
    FOR EACH index i, label IN enumerate unique_labels:
        SET one_hot_coding[label][i] = 1
    SET encoded_labels = empty list
    FOR EACH label IN labels:
        one_hot_coding[label]
    RETURN encoded_labels, one_hot_coding

SET labels = ['small','medium','large','medium','large']
CALL label_encode(labels)
PRINT hot_encode(labels)
SET coordinates = [(4.0, 6.0, 1),(7.0, 4.0, 1),(11.0, 8.0, 1),(13.0, 6.0, 2),(12.0, 20.0, 2),(31.0, 36.0, 2)]
SET k = 3
CALL KNN(k, coordinates)
PRINT "Classification result:", result

```


### Code Explanation

The codes main motive is to find to which class the parameters of a particular dataset belongs to using KNN algorithm. To do so the code we have used two functions `euclidean_dist`,`manhattan_dist`. Here the `e3ulcid_dist` calculates the distance between two points using the formula $sqrt((x2-x1)^2 + (y2-y1)^2)$.
Manhattan distance calculates the distance between two points , which will be the sum of the absolute difference of their coordinates $(∣x2−x1∣ + ∣y2−y1∣)$.

After calculating the distances the next step towards classifying to which class the dataset belongs to we  start implementing the `KNN` function the uses the k-nearest neighbor algorithm for classification. We first initializes an empty list, which stores the values of distances based on which the classification shall further go ahead. The k-nearest neighbors (KNN) algorithm used in this code classifies a new data point by considering the class labels of its k nearest neighbors in the feature space. As mentioned before it calculates distances for a first data point. Here we have preffered to use Euclidian Distance to calculate distances of data points in the dataset. It then selects the k data points with the smallest Euclidean distances to the new data point. These k points are considered the "nearest neighbors" of the new data point. The algorithm assigns the class label that appears most frequently among the k nearest neighbors to the new data point. If there is a tie, it may choose the class label randomly or by some predefined rule. The algorithm returns the predicted class label for the new data point based on the majority vote of its k nearest neighbors

To further take the code to next level we have implemented  a function named  `label_encode`  for encoding categorical variables into numerical representations. The `label_encode` function assigns a unique numerical code to each distinct label. **‘unique_labels’** Identifies the unique labels present in the target_variables list. `label_to_code` Initializes an empty dictionary to map each unique label to a numerical code. The loop assigns a unique numerical code to each label and increments the code. ‘encoded_labels’ Creates a list where each element is replaced with its corresponding numerical code. Returns both the encoded labels and the mapping from labels to codes.

 We have also defined a function named `one_hot_coding` that generates a one-hot encoding for each label, creating binary vectors where each element corresponds to the presence or absence of a particular label. ‘unique_labels’ Identifies and sorts the unique labels present in the target_variables list. ‘label_to_one_hot’ Initializes a dictionary with each label mapped to a binary vector of zeros.The loop assigns a one-hot encoding to each label, with a value of 1 at the corresponding index. ‘encoded_labels’ Creates a list where each element is replaced with its one-hot encoding. Returns both the one-hot encoded labels and the mapping from labels to one-hot encodings.

For checking if the model that we used is working properly and giving accurate answers, we have used the python library `pytest` that is used for unit testing. WE have tried to implement test cases for each of the functions and thus have come to the conclusion that the model is working perfectly fine.
