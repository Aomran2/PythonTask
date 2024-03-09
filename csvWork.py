import csv
import math
import statistics
import pandas as object

df = object.read_csv('Employees.csv')
fileData = object.DataFrame(df)

# remove any duplications from table
df = df.drop_duplicates()

# convert age to integer value
df['Age'] = df['Age'].astype(int)

# convert $ to egp
df['Salary(USD)'] = df['Salary(USD)']*(49.60)

print(df)

print("Average age is " + str(df['Age'].mean()))

print("median salaries are ", df['Salary(USD)'].median())

gender_count = df['Gender'].value_counts()
males_count = gender_count.get('M',0)
females_count = gender_count.get('F',0)
if males_count == 0:
    ration = "all employees are females"
else:
    ration = males_count/females_count
print("ration between males and female employees is ", ration)

df.to_csv('cleaned_file.csv' , index =False)
