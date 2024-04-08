from models import model
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import os
import time
from datetime import datetime
import pandas as pd
import os
import csv
import time
current_directory = os.path.dirname(os.path.abspath(__file__))


def temp_pred_model():
            
            # Load the collected data into a DataFrame
            row_data = os.environ.get('CSV_FILE')
            awair_csv_data = pd.read_csv(row_data, low_memory=False)
            selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
            # Split the data into input features (X) and target variable (y)
            X = selected_required_columns.drop('temp', axis=1)
            y = selected_required_columns ['temp']

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            # Initialize and train the linear regression model
            model_temp = model.temp_pred_model()
            # # Fit the model on the training data
            model_temp.fit(X_train, y_train)

            #Make predictions using the trained model on the test set.

            y_pred = model_temp.predict(X_test)


            # print(f"Y_pred : {y_pred}")
            # # Evaluate the model on the testing data
            # score = model_temp.score(X_test, y_test)
            mse = mean_squared_error(y_test, y_pred)

            # print('Test Score for temperature')
            # print("===========================================================")
            # print(f"test_score_temperature: {score}")
            # print("===========================================================")
            # Round the MSE to 2 decimal places
            mse_rounded = round(mse, 2)

            return model_temp, mse_rounded 


       
def humid_pred_model():

            # Load the collected data into a DataFrame
            row_data = os.environ.get('CSV_FILE')
            awair_csv_data = pd.read_csv(row_data, low_memory=False)
            selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
            # Split the data into input features (X) and target variable (y)
            # Split the data into input features (X) and target variable (y)
            X = selected_required_columns.drop('humid', axis=1)
            y = selected_required_columns ['humid']


            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            # Initialize and train the linear regression model
            model_humid = model.humid_pred_model()
            # # Fit the model on the training data
            model_humid.fit(X_train, y_train)

            #Make predictions using the trained model on the test set.

            y_pred = model_humid.predict(X_test)

            # print(f"Y_pred : {y_pred}")


            # # Evaluate the model on the testing data
            # score = model_humid.score(X_test, y_test)
            mse = mean_squared_error(y_test, y_pred)
            # print('Test Score for humidity')
            # print("===========================================================")
            # print(f"R-squared score humidity: {score}")
            # print("===========================================================")
            # Round the MSE to 2 decimal places
            mse_rounded = round(mse, 2)

            return model_humid, mse_rounded

def co2_pred_model():

    # Load the collected data into a DataFrame
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    # Split the data into input features (X) and target variable (y)
    
    # Split the data into input features (X) and target variable (y)
    X = selected_required_columns.drop('co2', axis=1)
    y = selected_required_columns ['co2']


    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the RandomForest model
    model_co2 = model.co2_pred_model()

    # # Fit the model on the training data
    model_co2.fit(X_train, y_train)


    #Make predictions using the trained model on the test set.

    y_pred = model_co2.predict(X_test)

    # print(f"Y_pred : {y_pred}")

    # # Evaluate the model on the testing data
    mse = mean_squared_error(y_test, y_pred)
    # print('Test Score for co2')
    # print("===========================================================")
    # print(f"Mean Squared Error co2: {mse}")
    # print("===========================================================")
    # Round the MSE to 2 decimal places
    mse_rounded = round(mse, 2)
    return model_co2, mse_rounded

def voc_pred_model():
    # Load the collected data into a DataFrame
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    # Split the data into input features (X) and target variable (y)

    # Split the data into input features (X) and target variable (y)
    X = selected_required_columns.drop('voc', axis=1)
    y = selected_required_columns ['voc']


    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train the RandomForest model
    model_voc = model.voc_pred_model()
    # # Fit the model on the training data
    model_voc.fit(X_train, y_train)

    #Make predictions using the trained model on the test set.

    y_pred = model_voc.predict(X_test)

    # print(f"Y_pred : {y_pred}")

    # # Evaluate the model on the testing data
    mse = mean_squared_error(y_test, y_pred)
    # print('Test Score for voc')
    # print("===========================================================")
    # print(f"R-squared score voc: {mse}")
    # print("===========================================================")

    # Round the MSE to 2 decimal places
    mse_rounded = round(mse, 2)

    return model_voc, mse_rounded

def pm25_pred_model():
    # Load the collected data into a DataFrame
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    # Split the data into input features (X) and target variable (y)
    
    # Split the data into input features (X) and target variable (y)
    X = selected_required_columns.drop('pm25', axis=1)
    y = selected_required_columns ['pm25']


    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train the RandomForest model
    model_pm25 = model.pm25_pred_model()
    # # Fit the model on the training data
    model_pm25.fit(X_train, y_train)

    #Make predictions using the trained model on the test set.

    y_pred = model_pm25.predict(X_test)

    # print(f"Y_pred : {y_pred}")

    # # Evaluate the model on the testing data
    mse = mean_squared_error(y_test, y_pred)
    # print('Test Score for pm25')
    # print("===========================================================")
    # print(f"R-squared score pm25: {mse}")
    # print("===========================================================")
    # Round the MSE to 2 decimal places
    mse_rounded = round(mse, 2)

    return model_pm25, mse_rounded


