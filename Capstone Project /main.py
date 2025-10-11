import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="climate_data",
    user="postgres",
    password="newpassword"
)
cur = conn.cursor()

df = pd.read_csv(r"C:\Users\samruddhi kaule\.cache\kagglehub\datasets\viveksingh2400\indias-state-and-district-wise-weather-data\versions\1\weather-1.csv")

df['last_updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')

df['Temperature (°C)'] = pd.to_numeric(df['Temperature (°C)'], errors='coerce')
df['Humidity (%)'] = pd.to_numeric(df['Humidity (%)'], errors='coerce')
df['Wind Speed (km/h)'] = pd.to_numeric(df['Wind Speed (km/h)'], errors='coerce')

df = df.where(pd.notnull(df), None)

for index, row in df.iterrows():
    cur.execute("""
        INSERT INTO state_climate (state_ut, district, temperature_c, condition, humidity_percent, wind_speed_kmh, last_updated)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row['State/UT'],
            row['District'],
            row['Temperature (°C)'],
            row['Condition'],
            row['Humidity (%)'],
            row['Wind Speed (km/h)'],
            row['last_updated']
        )
    )

conn.commit()
cur.close()
conn.close()

print("Data inserted successfully!")
