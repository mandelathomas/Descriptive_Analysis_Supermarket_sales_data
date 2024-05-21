#Project analyst Name: Mandela Philip Thomas
#Project Name: Predicting Hospital Readmission Rates
#Date:  May 21, 2024
#Focus: Analyze factors that contribute to patients being readmitted to the hospital shortly after discharge.


"""
What is a descriptive analysis
Python Descriptive Statistics process describes
the basic features of data in a study.
"""

#import various modules
import statistics as st
import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv("/content/healthcare_dataset.csv")

#check the average age for the healthcare data and round up to 2
stat_mean = st.mean(file['Age'].round(1))
print(f"Average patient age: {stat_mean}")

#check the most common billing amount cost paid for care
stat_mode = st.mode(file['Billing Amount'].round(2))
print(f"Most common Billing Amount: {stat_mode}")
