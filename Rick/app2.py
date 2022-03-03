# This Flask app is still in development!!
#
# Done: it will load the saved model and scaler when the predict button is clicked and return a message back to the user
#
# Still to do: change the model from RFC to NN
# Still to do: retrieve the user data from the index.html page before making prediction


# External dependencies:
from flask import Flask, render_template, redirect, url_for, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import tensorflow as tf
import pickle


# Create an instance of Flask:
app=Flask(__name__)


# Define initial descriptive text:
start_text = "Click the predict button."


# Home (index) route:
@app.route("/")
def index():

    # Status message to terminal
    print("Index route activated.")    

    return render_template("index.html", prediction=start_text)


# Heart disease prediction route:
@app.route("/pred", methods=["GET", "POST"])
def predict():

    # Status message to terminal
    print("Prediction route activated.")

    # Load the model and scaler from their external files:
    model_folder = "static/best_model"
    scaler_file = "static/best_nn_scaler.pkl"
    loaded_model = tf.keras.models.load_model(model_folder)
    loaded_scaler = pickle.load(open(scaler_file, "rb"))
    print(f"Model loaded from folder: {model_folder}")
    print(f"Scaler loaded from file: {scaler_file}")

    # Create column headers to match the ones in the one hot encoded and scaled "heart_df":
    column_headers = ["Age","RestingBP","Cholesterol","FastingBS","MaxHR","Oldpeak",
                    "Sex_F","Sex_M",
                    "ChestPainType_ASY","ChestPainType_ATA","ChestPainType_NAP","ChestPainType_TA",
                    "RestingECG_LVH","RestingECG_Normal","RestingECG_ST",
                    "ExerciseAngina_N","ExerciseAngina_Y",
                    "ST_Slope_Down","ST_Slope_Flat","ST_Slope_Up"]

    # Make some testing data for a fictitious patient:
    # (ultimately this data should come from the input fields on index.html)
    Age = 65
    Sex = "M"
    ChestPainType = "ATA"
    RestingBP = 125
    Cholesterol = 100
    FastingBS = 0
    RestingECG = "Normal"
    MaxHR = 150
    ExerciseAngina = "N"
    Oldpeak = 1.5
    ST_Slope = "Flat"                

    # Put the input data into a row:
    data_row = []
    data_row.append(Age)
    data_row.append(RestingBP)
    data_row.append(Cholesterol)
    data_row.append(FastingBS)
    data_row.append(MaxHR)
    data_row.append(Oldpeak)
    if Sex == "F":
        data_row.append(1)
        data_row.append(0)
    else:
        data_row.append(0)
        data_row.append(1)
    if ChestPainType == "ASY":
        data_row.append(1)
        data_row.append(0)
        data_row.append(0)
        data_row.append(0)
    elif ChestPainType == "ATA":
        data_row.append(0)
        data_row.append(1)
        data_row.append(0)
        data_row.append(0)
    elif ChestPainType == "NAP":
        data_row.append(0)
        data_row.append(0)
        data_row.append(1)
        data_row.append(0)    
    else:
        data_row.append(0)
        data_row.append(0)
        data_row.append(0)
        data_row.append(1)
    if RestingECG == "LVH":
        data_row.append(1)
        data_row.append(0)
        data_row.append(0)
    elif RestingECG == "Normal":
        data_row.append(0)
        data_row.append(1)
        data_row.append(0)
    else:
        data_row.append(0)
        data_row.append(0)
        data_row.append(1)
    if ExerciseAngina == "N":
        data_row.append(1)
        data_row.append(0)
    else:
        data_row.append(0)
        data_row.append(1)
    if ST_Slope == "Down":
        data_row.append(1)
        data_row.append(0)
        data_row.append(0)
    elif ST_Slope == "Flat":
        data_row.append(0)
        data_row.append(1)
        data_row.append(0)
    else:
        data_row.append(0)
        data_row.append(0)
        data_row.append(1)
        
    # Create a single row dataframe to pass as input to the model:
    input_data = pd.DataFrame([data_row], columns=column_headers)

    # Scale the input data: 
    input_data_scaled = loaded_scaler.transform(input_data)

    # Get prediction from model:
    y = loaded_model.predict(input_data_scaled)
    print(y)

    # Go back to the index route and execute index() function
    if y == 1:
        print("You are at risk for having a heart attack.")
        return render_template("index.html", prediction="You are at rick for having a heart attack.")
    else:
        print("You are not at risk for having a heart attack.")
        return render_template("index.html", prediction="You seem to have a healthy heart.")

 
# Run the Flask app:
if __name__=="__main__":
    app.debug=True
    app.run()