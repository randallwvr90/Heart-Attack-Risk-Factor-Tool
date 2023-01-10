# Heart-Attack-Risk-Factor-Tool

## Table of Contents
* [Disclaimer](#disclaimer)
* [Background](#background)
* [ML Prediction Project - Answering a Question](#ml-prediction-project---answering-a-question)
* [Models](#models)
* [Tools](#tools)
* [Modeling - lessons learned](#modeling---lessons-learned)
* [Web Deployment](#project-deployment-on-heroku)
* [Data](#data)
* [Repository Organization](#repository-organization)

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
* Neural Network
	* flesh out
* Nerual Network - Keras tuned
	* flesh out
* Random Forest
	* flesh out
* Logistic Regression
	* flesh out
* K-Nearest Neighbors
	* flesh out 
* Model selection
	* criteria (refer to lessons learned!!)
	* models - evaluation and selection
	* flesh out

## Tools
* Kaggle - data source
* Jupyter Notebook
	* data preprocessing
	* training and testing of each model
	* model evaluation (with an eye to selection)
* Flask - how do I say this?
* Heroku - web hosting

## Modeling - lessons learned
* flesh out

## Project Deployment on Heroku
Website where our application can be accessed:
* https://bootcamp-project-4.herokuapp.com

## Data
* the data set
	* flesh out
* Something about cleaning
	* flesh out
* Data Sources 
	* https://www.kaggle.com/fedesoriano/heart-failure-prediction/version/1

## Repository Organization
	- do we need this?
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

