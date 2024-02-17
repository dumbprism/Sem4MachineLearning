import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

# read the excel file
file = pd.read_excel(r"C:\Users\navee\Downloads\Lab Session1 Data.xlsx",sheet_name="Purchase data")
file['Customer'] = file['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')

# define features X and target variables Y
X = file[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']]
Y = file['Customer'] 

# split the dataset into training and testing
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=70)

# create a KNeighborsclassifier
classifier = KNeighborsClassifier(n_neighbors=5)
# train the classifier on the training data
classifier.fit(X_train,Y_train)

# prediction on dataset
prediction = classifier.predict(X_test)
 
# print the classification report
print("Classification Report")
print(classification_report(Y_test,prediction))