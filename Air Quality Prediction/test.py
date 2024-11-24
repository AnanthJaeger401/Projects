import pandas as pd
df = pd.read_csv('C:\\Users\\venka\\OneDrive\\Documents\\GitHub\\Projects\\Air Quality Prediction\\Air-Quality-Prediction\\Data\\Real-Data\\Real_Combine.csv')
df = df.dropna()
print("Minimum AQI in the dataset:", df['PM 2.5'].min())
print("Maximum AQI in the dataset:", df['PM 2.5'].max())
print("Summary Statistics for AQI:")
print(df['PM 2.5'].describe())
