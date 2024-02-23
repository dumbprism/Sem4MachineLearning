import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')
y_column_name = 'Instructions'  
X = file['Cleaned_Ingredients']
y = file[y_column_name]
file.dropna(subset=['Ingredients', 'Instructions'], inplace=True)
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(file['Ingredients'])
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, file['Title'], test_size=0.5, random_state=40
)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
test_vector_index = 0  
test_vector = X_test[test_vector_index]
test_vector_dense = test_vector.toarray().reshape(1, -1)

predicted_class = neigh.predict(test_vector_dense)
print("Predicted class for the test vector:", predicted_class)