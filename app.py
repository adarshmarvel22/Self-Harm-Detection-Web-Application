from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

with open('models/model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route('/analyze-text', methods=['GET', 'POST'])
def analyze_text():
    if request.method == 'POST':
        text = request.form['text']
        # perform analysis on the text here // here i am not using nlp as i haven't learned it yet but will surely learn it
        # Load the saved model from the pickle file

        # words = text.split()
        # save words to a text file
        # with open('words.txt', 'a') as f:
        #     f.write('\n'.join(words) + '\n')

        # Preprocess the input text
        input_text = text
        vectorizer = CountVectorizer()
        preprocessed_text = vectorizer.transform([input_text])

        # Use the trained model to predict the label
        predicted_label = model.predict(preprocessed_text)[0]

        # Print the predicted label
        # print("Predicted label:", predicted_label)

        if predicted_label == 1:
            return 'The Text Contains References to self-harm'
        else:
           return 'Text analyzed successfully and it has no self-harm text'
    return render_template('text_input_form.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
