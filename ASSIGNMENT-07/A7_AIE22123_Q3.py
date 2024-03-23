from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.naive_bayes import GaussianNB
from scipy.stats import uniform, randint

# Generate a random classification dataset
X, y = make_classification(n_samples=100, n_features=10, random_state=42)


#storing all the necessary classifiers that are required
classifiers = [
    LogisticRegression(random_state=42),
    SVC(probability=True),
    DecisionTreeClassifier(random_state=42),
    RandomForestClassifier(random_state=42),
    CatBoostClassifier(random_state=42, verbose=0),
    AdaBoostClassifier(random_state=42),
    XGBClassifier(random_state=42, use_label_encoder=False),
    GaussianNB()
]

#setting the parameter descreptions 
param_dists = [
    {'C': uniform(loc=0, scale=4), 'penalty': ['l2']},  # Only 'l2' penalty for Logistic Regression
    {'C': uniform(loc=0, scale=4), 'gamma': uniform(loc=0, scale=1), 'kernel': ['rbf', 'poly', 'sigmoid']},
    {'max_depth': randint(low=1, high=20), 'min_samples_leaf': randint(low=1, high=10), 'min_samples_split': randint(low=2, high=10)},
    {'max_depth': randint(low=1, high=20), 'n_estimators': randint(low=50, high=200), 'min_samples_split': randint(low=2, high=10)},
    {'depth': randint(low=4, high=10), 'iterations': randint(low=50, high=200), 'learning_rate': uniform(loc=0.01, scale=0.5)},
    {'n_estimators': randint(low=50, high=200), 'learning_rate': uniform(loc=0.1, scale=5)},
    {'max_depth': randint(low=3, high=10), 'n_estimators': randint(low=50, high=200), 'learning_rate': uniform(loc=0.01, scale=0.5)},
    {'var_smoothing': uniform(loc=1e-11, scale=1e-7)}
]

print("{:<30} {:<50} {:<15}".format('Classifier', 'Best Hyperparameters', 'Best Score'))
print("="*100)

for model, param_dist in zip(classifiers, param_dists):
    random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=25, cv=5, random_state=42, n_jobs=-1, verbose=0)
    random_search.fit(X, y)
    print("{:<30} {:<50} {:<15}".format(model.__class__.__name__, str(random_search.best_params_), "{:.4f}".format(random_search.best_score_)))
