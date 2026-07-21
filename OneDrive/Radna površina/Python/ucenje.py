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