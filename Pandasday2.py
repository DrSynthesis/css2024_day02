# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:56:50 2024

@author: Admin
"""

import pandas as pd

file = pd.read_csv("C:/Users/Admin/css2024_day1/data_01/iris.csv")

"""
Absolute path:
C:/Users/Admin/css2024_day1/data_01/iris.csv
Relative path:
data_01/iris.csv
"""

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

print(file)

"""
file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

file = pd.read_excel("data_02/residentdoctors.xlsx")

file = pd.read_json("data_02/student_data.json")
print(file)
"""
"""
file = pd.read_csv("data_02/country_data_index.csv")
print(file)
"""

file = pd.read_excel("data_02/residentdoctors.xlsx")
print(file)

print(file.info())

file["LOWER_AGE"] = file["AGEDIST"].str.extract('(\d+)-')
print(file)

file["LOWER_AGE"] = file["LOWER_AGE"].astype(int)

print(file.info())

file = pd.read_csv("data_02/time_series_data.csv",index_col=0)
print(file)

file['Date'] = pd.to_datetime(file['Date'], format="%Y-%m-%d")

print(file.info())

file['Year'] = file['Date'].dt.year
file['Month'] = file['Date'].dt.month
file['Day'] = file['Date'].dt.day


file = pd.read_csv("data_02/patient_data_dates.csv", index_col=0)

file.drop(index=26, inplace=True)

file['Date'] = pd.to_datetime(file['Date'])

print(file.info)

file.dropna(inplace = True)

file.loc[7, 'Duration'] = 45

print(file)

"""
Data Transformations
"""

file = pd.read_csv("data_02/iris.csv")

print(file.columns)

col_names = file.columns.tolist()

print(col_names)

file["sepal_length_sq"] = file["sepal_length"]**2

file["sepal_length_sq_2"] = file["sepal_length"].apply(lambda x: x**2)

grouped = file.groupby("class")

mean_square_value = grouped['sepal_length_sq'].mean()

print(mean_square_value) 

###################

file1 = pd.read_csv("data_02/person_split1.csv")
file2 = pd.read_csv("data_02/person_split2.csv")

file = pd.concat([file1,file2], ignore_index=True)


#####################


file1 = pd.read_csv("data_02/person_education.csv")
file2 = pd.read_csv("data_02/person_work.csv")

#inner join/ combining columns

file_merge_inner = pd.merge(file1,file2, on="id")

print(file_merge_inner)

file = pd.read_csv("data_02/iris.csv")

file["class"] = file["class"].str.replace("Iris-","")

file = file[file['sepal_length'] >5]

file = file[file["class"] =="virginica"]

print(file)

file.to_csv("pulsar.csv")































