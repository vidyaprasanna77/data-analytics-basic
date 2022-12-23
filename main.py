import pandas as pd
# small r is used to remove unicode error, reading csv file
data = pd.read_csv(
    r"C:\Users\admin\weather-dataanlysis-firstproject\1. Weather Data.csv")
# print(data)
# head shows first n rows in the data default , N=5
# print(data.head())
# shape- it shows total number of rows and columns in the dataframe
# print(data.shape)
# index - provides the index of the dataframe
# print(data.index)
# columns - shows the name of the each column
# print(data.columns)
# dtypes - shows the datatype of each column
# print(data.dtypes)
# unique - shows all unique values.it can be applied on sinlge column only
# print(data['Weather'].unique())
# nunique - shows total number of values in each column
# print(data.nunique())
# count- it shows total number of non null values in each column.(can be applied to single column or whole database)
# print(data.count())
# value_counts - it shows all the unique values with their count. applied to single column only
# print(data['Weather'].value_counts())
# info - provides basic information about the dataframe
# print(data.info())

# Q1. Find all the unique "Wind speed" values in the data
# data.head()
# data.nunique()
# data['Wind Speed_km/h'].nunique()
# print(data['Wind Speed_km/h'].unique())

# Q2.Find the number of times when the "Weather is exactly clear"
# data.head(2)
# data.Weather.value_counts()
# data[data.Weather == 'Clear']
# print(data.groupby('Weather').get_group('Clear'))

# Q3.Find the number of times when the 'Wind speed was exactly 4km/h'
# data['Wind Speed_km/h'] == 4
# print(data[data['Wind Speed_km/h'] == 4])


# Q4.Find out the null values in data
# data.isnull().sum()
# print(data.isnull().sum())


# Q5.Rename the column name 'Weather' of the dataframe to 'Weather condition'.
# a = data.rename(columns= {'Weather' : 'Weather Condition'},inplace = True)
# # to rename column permanently use rename is equal to true
# print(a)
# data.head()

# Q6.What is the mean 'visibility'?
# data.head()
# a = data.Visibility_km.mean()
# print(a)

# Q7.what is the standard deviation of 'pressure' in this data?
# data.Press_kPa.std()

# Q8. what is the variance of 'relative humidity ' in this data?
# data['Rel Hum_%']
# if there is no space in the column name we use . notation , if there is space we use [] notation
# data['Rel Hum_%'].var()

# # Q9. Find all instances when 'Snow ' was recorded
# data['Weather Condition'].value_counts()
# data[data['Weather Condition'] == 'snow']
# data[data['Weather Condition'].str.contains('snow')]
# to know last 20 values
# data[data['Weather Condition'].str.contains('snow')].tail(50)

# Q10. Find all instances when 'wind speed is above 24' and 'visibility is 25'.
# data.head()
a = data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
print(a)
