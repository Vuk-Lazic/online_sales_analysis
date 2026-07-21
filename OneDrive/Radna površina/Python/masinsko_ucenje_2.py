#VALIDACIJA

"""
import pandas as pd
from sklearn.model_selection import train_test_split

# Load labeled dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")

# Separate features (X) and labels (y)
X = df["review"]
y = df["sentiment"]

# Split the data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y                           #PRIMER TRENERIANJA I TESTIRANJA PODATAKA
)

# Display sizes of the resulting sets
print("Training set size:", len(X_train))
print("Test set size:", len(X_test))

# Display class distribution in the training and test sets
print("Training set class distribution:")
print(y_train.value_counts())

print("Test set class distribution:")
print(y_test.value_counts())
"""

#METRIKE EVALUACIJE

"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")
X = df["review"]
y = df["sentiment"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(                                      #PROVERA DA LI JE DOBRO PODELJENI SKUP PODATAKA NA TRENING I TESTIRANJE
    X, y, test_size=0.2, random_state=42, stratify=y
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train) #OBAVLJA SAMO KREIRANJE VOKABULARA NA SKUPU PODATAK I ONDA TAKO NAUCEN SKUP ON FORMIRA VEKTORE SVIH RECENZIJA
X_test_tfidf = vectorizer.transform(X_test) #OBAVLJA SAMO KREIRANJE MATRICE, PRETVARANJE TEKSTA U VEKTORSKI OBLIK NA OSNOVU VEC NAUCENOG VOKABULARA KOJI SMO NAUCILI U (FIT_TRANSFORM) METODI NA TRENING SKUPU PODATAKA

# Train logistic regression
model = LogisticRegression(max_iter=1000) #SPECJALNO NAMENJENI ZA TRENIRANJE A NE ZA TESTIRANJE
model.fit(X_train_tfidf, y_train)

# Predict on test set
y_pred = model.predict(X_test_tfidf)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
"""

"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")
X = df["review"]
y = df["sentiment"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(                                      
    X, y, test_size=0.2, random_state=42, stratify=y
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)               #VIZUALIZACIJA MATRICA POMOCU MATPLOTLIBA
X_test_tfidf = vectorizer.transform(X_test) 

# Train logistic regression
model = LogisticRegression(max_iter=1000) 
model.fit(X_train_tfidf, y_train)

# Predict on test set
y_pred = model.predict(X_test_tfidf)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)

disp  = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot()
plt.show()
"""

"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load and split the dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")
X = df["review"]
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Vectorization and model training
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)                   #PRIKAZIVANJE MATRICA POMOCU SEABORN BIBLIOTEKE
X_test_tfidf = vectorizer.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)

# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=["negative", "positive"])

# Plot using seaborn
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["negative", "positive"], yticklabels=["negative", "positive"])
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()
"""

#POREDJENJE MODELA I ODABIR NAJBOLJEG

"""
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
 
# Load dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")
X = df["review"]
y = df["sentiment"]
 
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
 
# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier(),
    "Support Vector Machine": LinearSVC()
}
 
# Train, predict, and evaluate
for name, model in models.items():
    model.fit(X_train_vec, y_train)
    y_pred = model.predict(X_test_vec)
    print(f"\n{name} - Classification Report:")
    print(classification_report(y_test, y_pred))
"""
"""
Kratak zaključak:

Najbolje ukupne rezultate pokazali su Logistička regresija i SVM, sa 96% i 95% tačnosti.

Naive Bayes daje dobre rezultate, ali nešto lošije u balansu odziva i preciznosti.

Decision Tree ima najniže metrike, ali i dalje vrlo dobre.

Svi modeli rade solidno, ali Logistička regresija pruža najbolji balans između tačnosti i F1 mere.

Koji se algoritam najbolje pokazao, a koji najlošije?

Najbolje: Logistic Regression
Najlošije: Decision Tree

---------------------------------------

Na osnovu čega ste utvrdili koji je algoritam najbolji, a koji najlošiji?

Na osnovu:

Ukupne tačnosti (accuracy) – Logistic Regression ima najvišu tačnost (96%), dok Decision Tree ima najnižu (93%).

F1 mere – Logistic Regression ima najvišu F1 vrednost (0.96), a Decision Tree najnižu (0.93).

Balansa između preciznosti i odziva – Logistic
"""