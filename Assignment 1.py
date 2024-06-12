from google.colab import files
uploaded=files.upload()

import pandas as pd

Q1
import io
df=pd.read_csv(io.BytesIO(uploaded['data.csv']))

df.head()

Q2
description=df.describe()
description

Q3
print( 'Are there any null values: ', df. isnull().values.any ())

# Checking for null values in the Dataframe
null_values = df. isnull(). sum()

# Printing the number of null values for each column
null_values

Q3(a)
#Replacing null values with the mean of the respective column
mean_values = df.mean()
df. fillna(mean_values, inplace=True)
print('Are there any null values after replacing: ', df.isnull().values.any())

# Checking for null values in the Dataframe (shguld return all 0s)
null_values= df.isnull().sum()

# Printing the number of null values for each column
null_values

Q4
#Selecting two columns maxpulse,calories and aggregating using min, max, count, and mean

agg_df=df.agg({'Maxpulse': ['min', 'max', 'count', 'mean'],
                 'Calories': ['min', 'max', 'count', 'mean']})


# Printing the aggregated data
agg_df

Q5
#Filtering the Dataframe to select rws with calorie values between 500 and 1000
filtered_df=df.loc[(df['Calories']>=500) & (df['Calories']<=1000)]

filtered_df

Q6
#Filtering the Dataframe to select rows with calorie values >500 and values pulse < 100
filtered_df=df.loc[(df['Calories']>500) & (df['Pulse']<100)]

filtered_df

Q7
# Dropping the 'Maxpulse' column and creating a new Dataframe
df_modified=df.drop(columns=['Maxpulse'])

#Printing the first 5 rows of new Dataframe
df_modified.head()

Q8
# Dropping the 'Maxpulse' column from the orginal  Dataframe
df.drop(columns=['Maxpulse'], inplace=True)

#Printing the first 5 rows of new Dataframe
df.head()

Q9
#astype() function is used to convert the data type
df['Calories']=df['Calories'].astype('int64')
df.dtypes
