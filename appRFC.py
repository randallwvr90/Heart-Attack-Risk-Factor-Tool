# This Flask app uses data input by the user to predict if they have heart disease or not.
# The app requires a Random Forest Classifier and its scaler to have been previously saved into pickle files.
# If those files do not exist, please create them using heart_attack_risk_rfc_model.ipynb before running this app.


# External dependencies:
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle


# Create an instance of Flask:
app=Flask(__name__)


# Define initial descriptive text:
start_text = "Please complete the above information and then click the predict button."


# Index route (the home/start page):
@app.route("/")
def index():

    # Status message to terminal
    print("Index route activated.")    

    return render_template("index.html", prediction=start_text)


# Heart disease prediction route:
@app.route("/pred", methods=["POST"])
def predict():

    # Status message to terminal
    print("Prediction route activated.")

    # Load the model and scaler from their external folder/files:
    model_file = "static/rfc_model.pkl"
    scaler_file = "static/rfc_scaler.pkl"
    loaded_model = pickle.load(open(model_file, "rb"))
    loaded_scaler = pickle.load(open(scaler_file, "rb"))
    print(f"Model loaded from file: {model_file}")
    print(f"Scaler loaded from file: {scaler_file}")

    # Create column headers to match the ones used in the model's training dataset:
    column_headers = ["Age","RestingBP","Cholesterol","FastingBS","MaxHR","Oldpeak",
                    "Sex_F", "Sex_M",
                    "ChestPainType_ASY","ChestPainType_ATA","ChestPainType_NAP","ChestPainType_TA",
                    "RestingECG_LVH","RestingECG_Normal","RestingECG_ST",
                    "ExerciseAngina_N", "ExerciseAngina_Y",
                    "ST_Slope_Down","ST_Slope_Flat","ST_Slope_Up"]

    """
    # Testing data to use if index.html is unavailable:
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
    """
    # Get data from posted form:
    if request.method != "POST":
        return render_template("index.html", prediction="Error: Please try again.")
    else:
        Age = request.form.get("Age")
        Sex = request.form.get("Gender")
        ChestPainType = request.form.get("ChestPainType")
        RestingBP = request.form.get("RestingBP")
        Cholesterol = request.form.get("Cholesterol")
        FastingBS = request.form.get("FastingBS")
        RestingECG = request.form.get("RestingECG")
        MaxHR = request.form.get("MaxHR")
        ExerciseAngina = request.form.get("ExerciseAngina")
        Oldpeak = 0.6
        ST_Slope = request.form.get("STslope") 

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
    print(input_data)

    # Scale the input data: 
    input_data_scaled = loaded_scaler.transform(input_data)

    # Get prediction from model:
    y = loaded_model.predict(input_data_scaled)
    print(y)

    # Go back to the index route and execute index() function:
    if y == 1:
        print("You are at risk for having a heart attack.")
        return render_template("index.html", prediction="You are at risk for having a heart attack.")
    else:
        print("You seem to have a healthy heart.")
        return render_template("index.html", prediction="You seem to have a healthy heart.")

 
# Run the Flask app:
if __name__=="__main__":
    app.debug=True
    app.run()