# BASICS OF PANDAS

import pandas as pd

school = {
    'Name': ['A', 'B', 'C'],
    'Math': [30, 70, 95],
    'Science': [31, 81, 92],
    'English': [25, 80, 88]
}

df = pd.DataFrame(school)     # Question Number one - Create a Data Frame

df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)     # Question Number Two - Find the Average of each students

print("Average marks of each student:","\n",df[['Name', 'Average']])    

print("Highest Average:","\n",df.max())# Question Number Three - Find the  Student with highest Average


df.loc[df['Average'] >= 40, 'Result'] = 'Pass'   # Question Number Four - New Column with Condition of Fail & Pass
df.loc[df['Average'] < 40, 'Result'] = 'Fail'

print(df)


# ABOUT GROUPBY FUNCTION

import pandas as pd

df = pd.DataFrame({
    'Department': ['HR','IT','IT','Finance'],
    'Name': ['John', 'Mary', 'David','Harry'],
    'Salary': [30000,50000,45000,48000],
    'Years': [4,1,3,7]
})

result = df.groupby('Department')['Salary'].agg(['mean','min','max','count'])

print(result)


# MERGING TWO DATA FRAMES

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'City': ['Mumbai', 'Pune', 'Delhi']
})

result = pd.merge(df1, df2, on='ID', how='inner')

print(result)


# DATA CLEANING

import pandas as pd

df = pd.DataFrame({
    'Email': ['Alice@Gmail.com', 'bob@Yahoo.cOm', 'charlie@OUTLOOK'],
    'Phone': [7998511525, 8879563622, 7895214522]
})

result = df['Email'] = df['Email'].str.strip().str.lower()

print(result)