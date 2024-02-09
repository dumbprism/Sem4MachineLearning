def euclidean_distance(x,y):
    distance = 0
    for i in range(len(x)):
        distance += (x[i]  - y[i])**2
    return distance**0.5

def manhattan_distance(x,y):
    manhattan_distance = 0
    for i in range(len(x)):
        manhattan_distance += abs(x[i] - y[i])
    
    return manhattan_distance

def euclidean_dist(point1, point2):
   
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def KNN(k,coordinates):
    dist = []

    for i in range(1,len(coordinates)):
        calculate_distance = euclidean_distance(coordinates[0],coordinates[i])
        dist.append((calculate_distance,coordinates[i][2]))
    
    for j in range(len(dist)):
        for l in range(0,len(distance)-j-1):
            if(dist[l][0] > dist[l+1][0]) : 
                temp = dist[l]
                dist[l] = dist[l+1]
                dist[l+1] = temp
        
    k_nearest = dist[:k]

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
    
    uniquelabel = set(labels)
    label_tocode = {}
    code = 0

    for  i in uniquelabel:
        label_tocode[i] = code
        code += 1
    
    for label in labels:
        encoded_label = label_tocode[label]
    
    return encoded_label,label_tocode

def hot_encode(labels):
    unique_label = sorted(set(labels)) 
    onehotcoding = {}
    for label in unique_label:
        onehotcoding[label] = [0] * len(unique_label)
   
    for i, label in enumerate(unique_label):
        onehotcoding[label][i] = 1
    encoded_labels = []
    for label in labels:
        onehotcoding[label]
    
    return encoded_labels, onehotcoding

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



file_path = 'bookmarks.arff'
data,attriburtes,label = read_file(file_path)

coordinates = []
for row in data : 
    for value in row[:-1]:
        featured_value  = float(value)
        tuple(featured_value)
        label = int(row[-1])

        coordinates.append((featured_value,label))


k = int(input("Enter a  value of k = "))

result = KNN(k, coordinates)
print("Classification result:", result)



