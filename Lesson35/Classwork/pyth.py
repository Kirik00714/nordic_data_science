import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px



st.title("Hello world!!!")
# df = pd.DataFrame({
#     'возраст': [10,21,45,32,76,11,45,66,23,99],
#     'рост': [165,150,178,185,190,210,158,129,163,177],
#     'вес': [55,47,70,79,92,103,51,32,49,66],
#     'пол': [0,0,0,1,0,1,1,0,1,0]
# })

df = pd.read_csv('telecom_churn.csv')
df["Churn"] = df["Churn"].astype(int)

st.text('Наши данные')
st.write(df)

st.text('Рассмотрим распределение голосовой почты от звонков')
st.bar_chart(df.groupby('Voice mail plan')['Total day calls'].count())

st.text('Рассмотрим гистограмму по лояльности')
fig = sns.displot(data=df, x='Customer service calls',color='red')
st.pyplot(fig)

option = st.selectbox('Выберете лояльность', df['Churn'].unique())
st.text(f'\nРассмотрим гистограмму по звонкам в сервис и коду области ={option}\n')
fig = sns.displot(data=df.query(f'Churn =={option}'), x='Area code',color='green')
st.pyplot(fig)

st.text(f'\nРассмотрим зависимость звонков в сервис от минут днем\n')
fig = px.scatter(df, x='Total day calls', y='Customer service calls',color_discrete_sequence=['purple'])
st.plotly_chart(fig,use_container_width=True)





