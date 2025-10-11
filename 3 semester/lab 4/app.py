import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Анализ данных Titanic", layout="wide")

df = pd.read_csv('titanic.csv')



st.title("Анализ данных о пассажирах Titanic")
st.markdown("---")


st.header("1. Описательная статистика")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Форма таблицы и типы данных")
    st.dataframe(df.dtypes.rename("Тип данных"))

with col2:
    st.subheader("Основная статистика")
    st.dataframe(df.describe())

st.markdown("---")


st.header("2. Просмотр данных")
num_rows = st.slider("Выберите количество строк для отображения", 1, len(df), 25)
st.dataframe(df.head(num_rows))

st.markdown("---")


st.header("3. Выживаемость по полу")
gender_survival = df.groupby(['Sex', 'Survived']).size().unstack().fillna(0)
gender_survival.index = gender_survival.index.map({'male': 'Мужчины', 'female': 'Женщины'})
gender_survival.columns = gender_survival.columns.map({0: 'Не выжил/а', 1: 'Выжил/а'})
st.bar_chart(gender_survival, use_container_width=True,stack='normalize')


st.header("4. Распределение возраста по полу")
gender = st.selectbox("Выберите пол", ["Все", "Мужчины", "Женщины"])
age_min, age_max = st.slider("Выберите диапазон возрастов", 0, 80, (0, 80))
if gender == "Мужчины":
    df_filtered = df[(df['Sex'] == 'male') & (df['Age'] >= age_min) & (df['Age'] <= age_max)]
elif gender == "Женщины":
    df_filtered = df[(df['Sex'] == 'female') & (df['Age'] >= age_min) & (df['Age'] <= age_max)]
else:
    df_filtered = df[(df['Age'] >= age_min) & (df['Age'] <= age_max)]

age_counts = df_filtered.groupby('Age').size().reset_index(name='Количество')
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(data=age_counts, x='Age', y='Количество', color='lightblue', ax=ax1)
ax1.set_title(f'Количество пассажиров по возрасту ({gender})')
ax1.set_xlabel('Возраст')
ax1.set_ylabel('Количество')
ax1.tick_params(axis='x', rotation=90)
st.pyplot(fig1)


st.header("5. Половая структура пассажиров")
gender_counts = df['Sex'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(gender_counts, labels=['Мужчины', 'Женщины'], autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightpink'])
ax2.axis('equal')
st.pyplot(fig2)


st.header("6. Зависимость пола от класса")
gender_class_counts = pd.crosstab(df['Sex'], df['Pclass'])
fig3, ax3 = plt.subplots()
sns.heatmap(gender_class_counts, annot=True, fmt='d', cmap='Blues', cbar=True, linewidths=0.5, ax=ax3)
ax3.set_title('Тепловая карта: Пол и Класс Пассажира')
ax3.set_xlabel('Класс Пассажира')
ax3.set_ylabel('Пол')
st.pyplot(fig3)


st.header("7. Процент выживших от возраста")
df_age = df.dropna(subset=['Age'])
age_groups = df_age.groupby('Age')['Survived'].agg(['sum', 'count']).reset_index()
age_groups['Процент выживших'] = (age_groups['sum'] / age_groups['count']) * 100
fig4, ax4 = plt.subplots(figsize=(12, 5))
sns.lineplot(data=age_groups, x='Age', y='Процент выживших', ax=ax4)
ax4.set_ylabel('Процент выживших (%)')
ax4.set_xlabel('Возраст')
ax4.set_title('Процент выживших от возраста')
ax4.grid(True)
st.pyplot(fig4)

st.markdown("---")

