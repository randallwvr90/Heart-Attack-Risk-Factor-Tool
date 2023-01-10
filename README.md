# Heart-Attack-Risk-Factor-Tool

## Table of Contents
* [Disclaimer](#disclaimer)
* [Background](#background)
* [Models](#models)
* [Modeling - lessons learned](#modeling---lessons-learned)
* [Web Deployment](#project-deployment-on-heroku)
* [Data](#data)
* [Repository Organization](#repository-organization)

## Disclaimer!
* flesh out

## Background
* add "proposal" info:
	* use info below but write a new section and delete these bullet points
	* We will use heart attack risk factor data
	* We will create a machine learning model that can predict (to some extent) heart attack risk based on risk factors. We will use several different machine learning techniques and pick the most accurate technique to use for our model.
	* In this process, we will also attempt to determine the most significant risk factors - does cholesterol level matter more than age, for example.
	* Finally, we will create a web-based tool based on our model.
	* heart attack background info
* Heart attack background info
	* flesh out

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

