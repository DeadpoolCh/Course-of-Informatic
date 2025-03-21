import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('titanic.csv')
colomns=['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']


st.dataframe(df.describe())
st.dataframe(df.dtypes)
num_rows = st.slider("Number of rows", 1, len(df), 25)
st.dataframe(df.iloc[:num_rows])

gender_survival = df.groupby(['Sex', 'Survived']).size().unstack().fillna(0)
gender_survival.index = gender_survival.index.map({'male': 'Мужчины', 'female': 'Женщины'})
gender_survival.columns = gender_survival.columns.map({0: 'Не выжил/а', 1: 'Выжил/а'})
st.title("Выживаемость от пола")
st.bar_chart(gender_survival, stack="normalize")

st.title('Распределение возраста по полу')
gender = st.selectbox("Выберите пол", ["Все", "Мужчины", "Женщины"])
age_min, age_max = st.slider("Выберите диапазон возрастов", 0, 80, (0, 80))
if gender == "Мужчины": df_filtered = df[(df['Sex'] == 'male') & (df['Age'] >= age_min) & (df['Age'] <= age_max)]
elif gender == "Женщины": df_filtered = df[(df['Sex'] == 'female') & (df['Age'] >= age_min) & (df['Age'] <= age_max)]
else: df_filtered = df[(df['Age'] >= age_min) & (df['Age'] <= age_max)]
age_counts = df_filtered.groupby('Age').size().reset_index(name='Count')
plt.figure(figsize=(10, 6))
sns.barplot(data=age_counts, x='Age', y='Count', color='lightblue')
plt.title(f'Количество пассажиров по возрасту ({gender})')
plt.xlabel('Возраст')
plt.ylabel('Количество')
plt.xticks(rotation=90)
st.pyplot(plt)

st.title('Половая диаграмма')
gender_counts = df['Sex'].value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'yellow'])
ax.axis('equal')
st.pyplot(fig)

gender_class_counts = pd.crosstab(df['Sex'], df['Pclass'])
plt.figure(figsize=(8, 6))
sns.heatmap(gender_class_counts, annot=True, fmt='d', cmap='Blues', cbar=True, linewidths=0.5)
plt.title('Тепловая карта: Пол и Класс Пассажира')
plt.xlabel('Класс Пассажира')
plt.ylabel('Пол')
st.pyplot(plt)

df_age = df.dropna(subset=['Age'])
age_groups = df_age.groupby('Age')['Survived'].agg(['sum', 'count']).reset_index()
age_groups['SurvivalRate'] = (age_groups['sum'] / age_groups['count']) * 100
plt.figure(figsize=(12, 6))
sns.lineplot(data=age_groups, x='Age', y='SurvivalRate')
plt.ylabel('Процент выживших (%)')
plt.xlabel('Возраст')
plt.title('Процент выживших от возраста')
plt.grid(True)
st.title("Процент выживших от возраста")
st.pyplot(plt)
