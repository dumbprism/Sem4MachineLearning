import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')
print("Column names in the dataset:", file.columns)
y_column_name = 'Instructions'  
X = file['Cleaned_Ingredients']
y = file[y_column_name]
file.dropna(subset=['Ingredients', 'Instructions'], inplace=True)
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(file['Instructions'])
X_train, X_test, y_train, y_test = train_test_split(
    X_tfidf, file['Title'], test_size=0.3, random_state=42
)
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
accuracy_test = accuracy_score(y_test, y_pred)
print("Accuracy on the test set:", accuracy_test)