import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
file = pd.read_csv(r'Food Ingredients and Recipe Dataset with Image Name Mapping.csv')
X_text = file['Cleaned_Ingredients']
y = file['Title']  
class_counts = file['Title'].value_counts()
valid_classes = class_counts[class_counts >= 3].index
if len(valid_classes) < 2:
    print("Not enough classes with sufficient samples. Please choose a different column.")
else:
    selected_classes = valid_classes[:2]
    subset_df = file[file['Title'].isin(selected_classes)]
    X_train_text, X_test_text, y_train, y_test = train_test_split(
        subset_df['Cleaned_Ingredients'], subset_df['Title'], test_size=0.3, random_state=42
    )
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X_train, y_train)
    y_pred = neigh.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)