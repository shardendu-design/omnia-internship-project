from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

# Let's create multiple model to predict different parameters

# model for temprature prediction

def temp_pred_model():
    
    model_temp = LinearRegression()
    
    return model_temp

def humid_pred_model():
    
    model_humid = LinearRegression()
        
    return model_humid

def co2_pred_model():
    
    model_co2 = RandomForestRegressor(random_state=42)
    
    return model_co2

def voc_pred_model():

    # Initialize and train the RandomForest model
    model_voc = RandomForestRegressor(random_state=42)
    
    return model_voc

def pm25_pred_model():
    
    # Initialize and train the RandomForest model
    model_pm25 = RandomForestRegressor(random_state=42)
    
    return model_pm25

