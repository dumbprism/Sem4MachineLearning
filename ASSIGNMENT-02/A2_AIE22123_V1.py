def euclidean_distance(x,y):
    euclid_dist = 0
    for i in range(len(x)):
        euclid_dist += (x[i]  - y[i])**2
    return euclid_dist**0.5

def manhattan_distance(x,y):
    manhattan_dist = 0
    for i in range(len(x)):
        manhattan_dist += abs(x[i] - y[i])
    
    return manhattan_dist

def euclidean_dist(point1, point2):
   
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def KNN(k,coordinates):
    distance = []

    for i in range(1,len(coordinates)):
        calculated_distance = euclidean_distance(coordinates[0],coordinates[i])
        distance.append((calculated_distance,coordinates[i][2]))
    
    for j in range(len(distance)):
        for l in range(0,len(distance)-j-1):
            if(distance[l][0] > distance[l+1][0]) : 
                temp = distance[l]
                distance[l] = distance[l+1]
                distance[l+1] = temp
        
    k_nearest = distance[:k]

    frequency1 = 0
    for a, label in k_nearest : 
        if label == 1:
            frequency1 += 1
    
    frequency2 = k - frequency1

    if frequency1 > frequency2 : 
        return "Belongs to the first class"
    
    else : 
        return "Belongs to the second class"
    

def label_encode(labels):
    
    unique_label = set(labels)
    label_to_code = {}
    code = 0

    for  i in unique_label:
        label_to_code[i] = code
        code += 1
    
    for label in labels:
        encoded_label = label_to_code[label]
    
    return encoded_label,label_to_code

def hot_encode(labels):
    unique_labels = sorted(set(labels)) 
    one_hot_coding = {}
    for label in unique_labels:
        one_hot_coding[label] = [0] * len(unique_labels)
   
    for i, label in enumerate(unique_labels):
        one_hot_coding[label][i] = 1
    encoded_labels = []
    for label in labels:
        one_hot_coding[label]
    
    return encoded_labels, one_hot_coding

def read_file(file_path):
    with open(file_path,'r') as f:
        text = f.readline()
    
    attributes = []
    data = []
    labels = []
    read_data = False

    for line in text:
        line = text.strip()

        if not line or text.startswith('%'):
            continue
        
        if line.lower().startswith('@attribute'):
            attribute_name = line.split()[1]
            attributes.append(attribute_name)
        
        elif line.lower().startswith('@data'):
            read_data = True
        
        elif read_data:
            data.append(line.split(','))
        
        elif line.lower().startswith('@relation'):
            relation_name = line.split()[1]
        
        elif line.lower().startswith('{'):
            labels.extend(line.strip('{}').split(','))
    
    return data,attributes,labels



file_path = 'IMDB-F.arff'
data,attriburtes,label = read_file(file_path)

coordinates = []
for row in data : 
    for value in row[:-1]:
        featured_value  = float(value)
        tuple(featured_value)
        label = int(row[-1])

        coordinates.append((featured_value,label))


k = int(input("Enter a certain value of k = "))

result = KNN(k, coordinates)
print("Classification result:", result)



