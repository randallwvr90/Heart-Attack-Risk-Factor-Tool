# Heart-Attack-Risk-Factor-Tool

## Table of Contents
* [Web Hosting Note](#web-hosting-note)
* [Disclaimer](#disclaimer)
* [Background](#background)
* [ML Prediction Project - Answering a Question](#ml-prediction-project---answering-a-question)
* [Models](#models)
* [Tools](#tools)
* [Web Deployment](#web-deployment)
* [Data](#data)
* [Repository Organization](#repository-organization)

## Web Hosting Note
We are currently selecting a new web hosting service for our tool! The machine learning back end is large enough to preclude us from the free services we have found so far. Thank you for your patience - this is a personal project for us so we want to keep our costs as low as possible. In the meantime, if you would like to try the tool, please clone this repo and run app.py locally!

## Disclaimer!
This product IS ABSOLUTELY NOT meant for use in a medical or clinical or diagnostic way! DO NOT use this tool or the website for ANY medical or real-world reason!

All mentions of the accuracy of our model refer ONLY to the model's ability to match new inputs to our [Existing Data Set](#data). We have NO IDEA and NO WAY TO FIND OUT how these predictions would compare to "real life"!

Any use other than for fun and interest in data analytics runs counter to our purpose and our wishes so JUST DON'T DO IT. 

This project is simply a fun and interesting application of data analytics and is meant as an exercise and portfolio project for those of us who worked on it. We hope you enjoy taking a look and trying it out - only for fun! 

## Background
* Heart Disease: What is it?
	* This term refers to a range of conditions that involve narrow or blocked blood vessels and can lead to a heart attack. Conditions under this umbrella include:
		* blood vessel diseases
		* coronary artery disease
		* heart rhythm problems (arrhythmias)
		* congenital heart defects
	* Heart disease is the leading cause of death globally. It is estimated that 17.9 million people died from heart disease in 2019, representing 32% of global deaths. 85% of these deaths were due to heart attack and stroke. 
* Doctors often use a non-invasive, basic form of screening to identify patients likely to develop heart disease in the near future. 11 health attributes are commonly used, and the data are collected during an exercise electrocardiogram (ECG), also known as a "stress test". The 11 attributes are:
	* Age
	* Sex
	* Presence of Exercise-Induced Angina
	* Chest Pain Type - typical angina, atypical angina, non-angina pain, or asymptomatic
	* Resting Blood Pressure
	* Cholesterol
	* Fasting Blood Sugar
	* Resting Electrocardiogram (ECG) Results
	* Max Heart Rate Achieved
	* "Old Peak" - a feature of the ECG waveform
	* "ST Slope" - a feature of the ECG waveform

## ML Prediction Project - Answering a Question
Our team attempted to answer the question: Is it possible to train a machine learning (ML) model to reliably assign a set of inputs to one of two buckets: heart disease present, or heart disease not present? And how reliably could the ML model do this task? Again, this is simply a data analysis exercise - [SEE DISCLAIMER!](#disclaimer)
The second question we wanted to answer: Can the ML model we create be used to find the health attributes most correlated with heart disease risk and which of the eleven attributes are they? For example, does cholesterol level matter more than age? 

To answer these questions, we used several types of ML model and selected from among them the one we determined did the best job at predicting risk for a set of health attributes. See [Models](#models) for information on the models we used and on our evaluation criteria. 

Finally, we will deploy our model as a web-based tool where users can play with different health attribute values and see the model's risk prediction. 

## Models

We created, trained, and tested several types of ML model and selected from among them. The list of models we tried is below. 
* Neural Network - Keras-tuned - this is the model we selected based on our selection criteria. 
* Nerual Network 
* Random Forest
* Logistic Regression
* K-Nearest Neighbors

## Tools
* Kaggle - data source
* Jupyter Notebook
	* data preprocessing
	* ML model development
	* model training and testing
	* model evaluation (with an eye to selection)
* Tensorflow Python Library
	* ML model development
* SKLearn Python Library
	* model training and testing
* Flask - web development
* Heroku - web hosting

## Web Deployment
We are in the process of finding a hosting service - see [the note above](#web-hosting-note). Thank you for your patience!

## Data
Data source: https://www.kaggle.com/fedesoriano/heart-failure-prediction/version/1

## Repository Organization
* app.py (flask application)
* Procfile (file needed for Heroku)
* requirement.txt (file needed for Heroku)
* Heart Disease Prediction_Machine Learning Integration.pdf (presentation slides)
* **static**
	* best_model.h5 (neural network model file)
	* best_nn_scaler.pkl (data scaling file)
	* style.css (webpage style sheet)
* **templates**
	* index.html (landing page)
	* form_page.html (form input page)
	* prediction_page.html (model output page)
* **model_investigation**
	* heart_attack_risk_knn_model.ipynb (k-nearest neighbors investigation)
	* heart_attack_risk_logistic.ipynb (logistical regression investigation)
	* heart_attack_risk_rfc_model.ipynb (random forest investigation)
	* NN.ipynb (tensorflow investigation)
	* NN_keras.ipynb (tensorflow with keras investigation)
	* **data**
		* heart.csv (raw data file used for training and testing)

