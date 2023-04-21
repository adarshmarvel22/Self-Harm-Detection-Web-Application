# lab-flask

<!-- ![image](https://user-images.githubusercontent.com/115451707/196919992-edcfea8b-e3f6-4f35-9398-43be66b5622d.png) -->


To run flask application 

```
python app.py
```


To access your flask application open new tab in and paste the url:
```
https://{your_url}.pwskills.app:5000/
```
Project Title: Self-Harm Detection Web Application

Github link: https://github.com/adarshmarvel22/Self-Harm-Detection-Web-Application

Project Description: 
- The Self-Harm Detection Web Application is a Flask-based web application that uses Machine Learning models to analyze and detect whether a given input text contains self-harm words or not. This project aims to provide an automated way to detect self-harm behavior by analyzing the text used in messages, social media posts, or other online communications.
Technologies Used:
- I have used the pwskills lab (iNeuron.ai lab) which is the lab of course I am currently pursuing. I can host the Web App on AWS if need be. Do let me know on my mail: adarshmsd1@gmail.com
Flask: Flask is a web framework that enables the development of web applications using Python. I have used flask here but very well versed with Django( another python Web framework) also.
Machine Learning Models: The two models used in this project are MultinomialNB and Logistics Regression. These models are commonly used for text classification tasks.
CountVectorizer: CountVectorizer is a method for extracting features from text data.

Folder structure of the App:
![folder_structure](https://user-images.githubusercontent.com/87609950/233452949-6a325e9e-4946-4b7b-a672-84d4a79a9224.jpg)

 

How the Project Works: 
- The Self-Harm Detection Web Application works by using the MultinomialNB and Logistics Regression models, which have been trained on a dummy dataset of self-harm and non-self-harm words, to analyze the input text and determine if it contains any self-harm words. The dataset has been created manually by collecting various self-harm words from multiple sources.
- The CountVectorizer is used to extract features from the text data. It converts the input text into a matrix of token counts, which is then used as input for the Machine Learning models. A pickle file has been created that contains the trained models to be used in the web application. The accuracy score of the Multinomial naïve Bayes of the trained model is 66.66% higher than its Logistic Regression model. So Multinomial Naïve Bayes has been used int this project.
66.66% accuracy of the Multinomial Naïve Bayes:
![modelAcc](https://user-images.githubusercontent.com/87609950/233453239-c0a68fdf-2359-4c16-8dd6-6137be140485.jpg)

 
The following input/output of the model training part of jupyter file shows the working/prediction from the text inputs:
![output1](https://user-images.githubusercontent.com/87609950/233452990-60d98982-070c-4c1b-a8fe-13c13af14775.jpg)

  ![output0](https://user-images.githubusercontent.com/87609950/233453118-2bc05b75-f289-443a-8387-71bc5cddcc79.jpg)

An API endpoint called "analyze_data" has been created that takes input as a text and applies the Machine Learning model to predict whether the input sentence contains self-harm words or not. If the input text contains self-harm words, the web application will display a warning message and recommend the user to seek help from professionals or call emergency helpline numbers.
 
![input text page for analysis](https://user-images.githubusercontent.com/87609950/233453154-1f167eac-587e-45e9-a7fc-7c3b01095697.jpg)


Conclusion: The Self-Harm Detection Web Application is a useful tool that can be used to automatically detect self-harm behavior from input text. The use of Flask, Machine Learning models, and CountVectorizer make the application robust and efficient. By analyzing the input text, the application can provide an early warning sign and recommend necessary help to the users.

Hence the system architecture diagram for the project is:
1.	User enters text input into the user interface.
2.	The input text is sent to the server-side via an API endpoint called "analyze_data."
3.	The input text is passed through the CountVectorizer to extract features from the text data.
4.	The extracted features are passed through the MultinomialNB and Logistics Regression Machine Learning models to analyze the input text and determine if it contains any self-harm words.
5.	If the input text contains self-harm words, the web application displays a warning message and recommends the user to seek help from professionals or call emergency helpline numbers.
6.	The output is sent back to the user interface, where the result is displayed to the user.
- More precidsely:  Input -> API Endpoint (analyze_data) -> CountVectorizer -> MultinomialNB/Logistic Regression models -> Output (contains self-harm words or not) -> Display warning message and recommendations in the web application


