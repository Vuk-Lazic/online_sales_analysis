#PROVERA PODATAKA

"""
import pandas as pd

# Load the unlabeled dataset
df = pd.read_csv("reviews_unlabeled.csv")                       #OBRATI PAZNJU NA KOJI FAJL SE ODNOSI PUTANJA
 
# 1. Print dataset shape (rows and columns)
print("Dataset shape (rows, columns):", df.shape)

# 2. Check for missing values
print("\nMissing values per column:")                         #PRIMER PROVERE PODATAKA
print(df.isna().sum()) 

# 3. Preview a few example reviews
print("\nSample reviews:")
print(df['review'].sample(5, random_state=42))

# 4. Calculate average review length in number of words
df['review_length'] = df['review'].astype(str).apply(lambda x: len(x.split())) #DELI CELU RECENICU NA POJEDICANE RECI
average_length = df['review_length'].mean()
print(f"\nAverage review length (in words): {average_length:.2f}")
"""

"""
import pandas as pd

df = pd.read_csv("reviews_labeled.csv")

# 1. Print the shape of the dataset (number of rows and columns)
print("Dataset shape (rows, columns):", df.shape)
 
# 2. Check for missing (NaN) values in each column
print("\nMissing values per column:\n", df.isna().sum())                                       #PRIMER PROVERE PODATAKA

# 3. Display distribution of 'sentiment' values (count)
print("\nDistribution of 'sentiment' values:\n", df['sentiment'].value_counts())

# 4. Display sentiment distribution as percentages
print("\nSentiment distribution (percentage):\n", df['sentiment'].value_counts(normalize=True) * 100)
"""

"""
import pandas as pd

# Step 1: Load the labeled dataset
df = pd.read_csv("reviews_labeled.csv")

# Step 2: Drop rows with missing values
df = df.dropna()

# Step 3: Standardize sentiment column to lowercase                                       #CISCENJE PODATAKA I PRIPREMA ZA DALJU ANALIZU
df['sentiment'] = df['sentiment'].str.strip().str.lower()

# Optional: Check unique values to confirm
print("Unique sentiment values after standardization:", df['sentiment'].unique())

# Step 4: Save the cleaned dataset
df.to_csv("reviews_labeled_cleaned.csv", index=False)
"""

#RULE-BASED

"""
import pandas as pd

# Define simple keyword lists
positive_words = ["great", "excellent", "amazing", "love", "perfect", "good", "fantastic", "happy", "recommend"]
negative_words = ["bad", "terrible", "worst", "broken", "poor", "disappointed", "awful", "hate", "slow"]

# Define a simple rule-based sentiment classifier (binary only)
def classify_sentiment(text):
    text = str(text).lower()
    pos_hits = sum(word in text for word in positive_words)                                  #RAZVRSTAVANJE RECENZIJA
    neg_hits = sum(word in text for word in negative_words)

    if pos_hits >= neg_hits:
        return "positive"
    else:
        return "negative"
    
# Load labeled dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")

# Apply the classifier
df['predicted_sentiment'] = df['review'].apply(classify_sentiment)

# Save the results to a new CSV file
df.to_csv("reviews_with_predicted_sentiment.csv", index=False)

# Display sample output in the terminal (only selected columns)
print(df[['review', 'sentiment', 'predicted_sentiment']].head(20))
"""

#MASINKO UCENJE

##SKLEARN DATASET

"""
from sklearn import datasets

iris = datasets.load_iris()                                              #PROVERA RADA (DA LI JE SVE LEPO NAMESTENO)

print("Dataset name:", iris['target_names'])
print("Feature names:", iris['feature_names'])
print("Number of instances:", len(iris['data']))
"""

"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer  #PRETVARA TEKSTUALNE PODATKE U NUMERICKE VREDNOSTI
from sklearn.linear_model import LogisticRegression   #ALGORITAM ZA UCENJE

# Load the labeled dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")

# Separate features and labels
x = df['review']  #KAO ULAZ
y = df['sentiment']   #ODGOVOR KOJI MODEL TREBA DA PREDVIDI

# Vectorize all input reviews
vectorizer = TfidfVectorizer()    #PREVODI RECENICU U NIZ BROJEVA KOJI SE KORISTE ZA UCENJE              #PRIMER AUTOMATIZACIJE
x_tfidf = vectorizer.fit_transform(x)   

# Train the logistic regression model on the full dataset
model = LogisticRegression()    #PROCES UCENJA MODELA
model.fit(x_tfidf, y)

print("\nModel is ready. Enter a review to classify its sentiment.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter a review: ")
    if user_input.lower() == 'exit':
        print("Exiting sentiment classifier.")
        break
    
    # Transform user input to match TF–IDF vector format
    user_tfidf = vectorizer.transform([user_input])
    prediction = model.predict(user_tfidf)[0]

    print(f"Predicted sentiment: {prediction}\n")
"""

###VEKTORIZACIJA TEKSTA

"""
from sklearn.feature_extraction.text import CountVectorizer

# Mini dataset of sample reviews
corpus = [
    "I love this product",
    "This product is not good",
    "Absolutely fantastic experience",
    "Terrible, I hate it",
    "Not great, not terrible"
]

# Create and fit the vectorizer
bow_vectorizer = CountVectorizer()
X_bow = bow_vectorizer.fit_transform(corpus)                                   #PRETVARANJE TEKSTA U NUMERICKE VREDNOSTI (BAG OF WORDS)

# Show feature names (vocabulary)
print("Vocabulary:", bow_vectorizer.get_feature_names_out())

# Convert sparse matrix to array for readability
print("\nBoW Matrix (Document-Term Matrix):\n", X_bow.toarray())
"""

"""
from sklearn.feature_extraction.text import TfidfVectorizer

# Mini dataset of sample reviews
corpus = [
    "I love this product",
    "This product is not good",
    "Absolutely fantastic experience",
    "Terrible, I hate it",
    "Not great, not terrible"
]

# Create and fit the TF–IDF vectorizer                                   #PRETVARANJE TEKSTA U NUMERICKE VREDNOSTI (TF–IDF)
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(corpus)

# Show feature names
print("Vocabulary:", tfidf_vectorizer.get_feature_names_out())

# Convert to array and print
print("\nTF–IDF Matrix:\n", X_tfidf.toarray())
"""

###ALGORITMI

"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

# Load labeled dataset
df = pd.read_csv("reviews_labeled_cleaned.csv")
X = df['review']
y = df['sentiment']

# Convert text to TF-IDF
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# Train different algorithms on the same data
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),             #OPREDJIVANJE TRI ALGORITMA ZA UCENJE
    "Naive Bayes": MultinomialNB(),
    "Decision Tree": DecisionTreeClassifier()
}

trained_models = {}
for name, model in models.items():
    model.fit(X_tfidf, y)
    trained_models[name] = model

# Interactive testing
print("\nModels are trained. Type a review to classify it.")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("Enter a review: ")
    
    if user_input.lower() == 'exit':
        print("Exiting.")
        break

    user_tfidf = vectorizer.transform([user_input])

    for name, model in trained_models.items():
        prediction = model.predict(user_tfidf)[0]
        print(f"{name} → {prediction}")

    print("-" * 40)
"""