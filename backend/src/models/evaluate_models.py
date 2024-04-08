from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import os
import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor

def perform_linear_regression():

    # Load data
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    
    # Select required columns and remove rows with missing values
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    
    # Extract features (X) and target variables (y)
    X = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Features
    y = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Target variables
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = MultiOutputRegressor(LinearRegression())
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    
    # Generate evaluation result
    evaluation_result = f"Evaluation result for Linear Regression: MSE = {mse:.2f}"


    return evaluation_result

def perform_random_forest():
    # Load data
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    
    # Select required columns and remove rows with missing values
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    
    # Extract features (X) and target variables (y)
    X = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Features
    y = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Target variables
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42))
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    
    # Generate evaluation result
    evaluation_result = f"Evaluation result for Random Forest: MSE = {mse:.2f}"

    return evaluation_result

# Define similar functions for other machine learning models...
def perform_support_vector_machine():
    # Load data
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    
    # Select required columns and remove rows with missing values
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    
    # Extract features (X) and target variables (y)
    X = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Features
    y = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Target variables
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = MultiOutputRegressor(SVR(kernel='linear'))  # You can choose different kernels like 'linear', 'poly', 'rbf', etc.
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    
    # Generate evaluation result
    evaluation_result = f"Evaluation result for Support Vector Machine: MSE = {mse:.2f}"
    
    return evaluation_result

def perform_k_nearest_neighbors():
    # Load data
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    
    # Select required columns and remove rows with missing values
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    
    # Extract features (X) and target variables (y)
    X = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Features
    y = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Target variables
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = MultiOutputRegressor(KNeighborsRegressor(n_neighbors=5))  # You can adjust the number of neighbors as needed
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    
    # Generate evaluation result
    evaluation_result = f"Evaluation result for K-Nearest Neighbors: MSE = {mse:.2f}"
    
    return evaluation_result

from sklearn.tree import DecisionTreeRegressor

def perform_decision_trees():
    # Load data
    row_data = os.environ.get('CSV_FILE')
    awair_csv_data = pd.read_csv(row_data, low_memory=False)
    
    # Select required columns and remove rows with missing values
    selected_required_columns = awair_csv_data[['temp', 'humid', 'co2', 'voc', 'pm25']].dropna().drop_duplicates()
    
    # Extract features (X) and target variables (y)
    X = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Features
    y = selected_required_columns[['temp', 'humid', 'co2', 'voc', 'pm25']]  # Target variables
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = MultiOutputRegressor(DecisionTreeRegressor(random_state=42))
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    
    # Generate evaluation result
    evaluation_result = f"Evaluation result for Decision Trees: MSE = {mse:.2f}"
    
    return evaluation_result
