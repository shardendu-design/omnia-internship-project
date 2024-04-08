# from src.models import model_test_with_live_data
import model_test_with_live_data
# from src.air_cooler_integration import air_cooler
# from src.WiFi_Socket import tapo_info

from datetime import datetime

import time
import psycopg2
import csv
import os
import pandas as pd

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT")


predicted_csv = os.environ.get('predicted_data')

def model_execution_with_live_data():

    while True:

        model_test_with_live_data.temp_test_prediction()
        
        model_test_with_live_data.humid_test_prediction()
        
        model_test_with_live_data.co2_test_prediction()
        
        model_test_with_live_data.voc_test_prediction()
        
        model_test_with_live_data.pm25_test_prediction()
        
        predicted_values = model_test_with_live_data.predicted_data
        # print(predicted_values)

        
        pred_temp_value = predicted_values[2]
        
        pred_temp_humid = predicted_values[5]
        
        pred_temp_co2 = predicted_values[8]
        pred_temp_voc = predicted_values[11]
        predicted_temp_pm25 = predicted_values[14]
        
        pred_temp_value_only = []
        for k,temp in pred_temp_value.items():  
            pred_temp_value_only.append(round(temp, 2))

        

        pred_humid_value_only = []

        for k,humid in pred_temp_humid.items():
            pred_humid_value_only.append(round(humid, 2))
            
        
        pred_co2_value_only = []

        for k,co2 in pred_temp_co2.items():
            pred_co2_value_only.append(co2)
        
        pred_voc_value_only = []
        for k,voc in pred_temp_voc.items():
            pred_voc_value_only.append(voc)

        pred_pm25_value_only = []

        for k,pm25 in predicted_temp_pm25.items():
            pred_pm25_value_only.append(pm25)

        # Air cooler integration
        # air_cooler.air_coller_integration(temp,humid)

        
        conn1 = psycopg2.connect(
            host='localhost',
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
        
        )

        conn1.autocommit=True

        cur1 = conn1.cursor()
        cur1.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'awair'")
        exists = cur1.fetchone()

        if not exists:
            cur1.execute("CREATE DATABASE awair")

        conn1.set_session(autocommit=True)

        try:

            conn = psycopg2.connect(
            host='localhost',
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_password
            )
        except psycopg2.Error as e:
            print(e)

        try:
            cur = conn.cursor()
        except psycopg2.Error as e:

            print("Error: Could not get the cursor to the database")
            print(e)

        conn.set_session(autocommit=True)

        try:
            cur.execute("CREATE TABLE IF NOT EXISTS predicted_data (id SERIAL PRIMARY KEY,\
                                            DateTime TIMESTAMP,\
                                            Tempe_Test_S NUMERIC,\
                                            Temp_Pred NUMERIC,\
                                            Humid_Test_S NUMERIC,\
                                            Humid_Pred NUMERIC,\
                                            Co2_Test_S NUMERIC,\
                                            Co2_Pred NUMERIC,\
                                            VOC_Test_S NUMERIC,\
                                            VOC_Pred NUMERIC,\
                                            Pm25_Test_S NUMERIC,\
                                            Pm25_Pred NUMERIC);")
        
        except psycopg2.Error as e:
            print("Error: Issue creating table")
            print(e)

        record = {}
        for item in predicted_values:
            key = list(item.keys())[0]
            value = item[key]
            record[key] = value

        columns = ', '.join(record.keys())
        placeholders = ', '.join(['%s'] * len(record))

        sql = f"INSERT INTO predicted_data ({columns}) VALUES ({placeholders})"

        try:
            cur.execute(sql, list(record.values()))
            conn.commit()
        except psycopg2.Error as e:
            print("Error:", e)
            conn.rollback()
        
        # CSV file writing
        merged_data = {}
        for item in predicted_values:
            merged_data.update(item)

        # Check if the file exists and write data accordingly
        with open(predicted_csv, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=merged_data.keys())
            if csvfile.tell() == 0:  # If the file is empty, write header
                writer.writeheader()
            writer.writerow(merged_data)
        
        
        time.sleep(600)

model_execution_with_live_data()