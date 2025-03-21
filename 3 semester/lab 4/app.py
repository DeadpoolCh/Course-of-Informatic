import streamlit as st
import pandas as pd
import numpy as np


df=pd.read_csv('titanic.csv')
num_rows = st.slider("Number of rows", 1, len(df), 25)
data=[]
colomns=['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
st.dataframe(df.iloc[:num_rows])