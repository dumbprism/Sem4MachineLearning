import pytest
from A2_AIE22115_V1 import KNN, read_file

def test_KNN_with_dataset_values():
    file_path = 'chess.arff'
    data, _, _ = read_file(file_path)
    
   
    coordinates = [(tuple(map(int, row[:-1])), int(row[-1])) for row in data]

    
    assert KNN(1, coordinates) == "Belongs to the second class"
