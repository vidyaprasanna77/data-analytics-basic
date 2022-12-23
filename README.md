# data-analytics-basic
head shows first n rows in the data default , N=5
print(data.head())
shape- it shows total number of rows and columns in the dataframe
print(data.shape)
index - provides the index of the dataframe
print(data.index)
columns - shows the name of the each column
print(data.columns)
dtypes - shows the datatype of each column
print(data.dtypes)
unique - shows all unique values.it can be applied on sinlge column only
print(data['Weather'].unique())
nunique - shows total number of values in each column
print(data.nunique())
count- it shows total number of non null values in each column.(can be applied to single column or whole database)
print(data.count())
value_counts - it shows all the unique values with their count. applied to single column only
print(data['Weather'].value_counts())
info - provides basic information about the dataframe
print(data.info())
