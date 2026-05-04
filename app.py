import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Workforce Attrition Analysis Dashboard")

# Load data
df = pd.read_csv("Palo Alto Networks.csv")

# Sidebar filters
st.sidebar.header("Filters")

department = st.sidebar.selectbox("Select Department", df['Department'].unique())
overtime = st.sidebar.selectbox("OverTime", df['OverTime'].unique())

filtered_df = df[(df['Department'] == department) & (df['OverTime'] == overtime)]

# Overall attrition
st.subheader("Overall Attrition Rate")
st.write(f"{df['Attrition'].mean() * 100:.2f}%")

# Filtered attrition
st.subheader("Filtered Attrition Rate")
st.write(f"{filtered_df['Attrition'].mean() * 100:.2f}%")

# Chart 1: Department
st.subheader("Attrition by Department")
fig1, ax1 = plt.subplots()
sns.barplot(x='Department', y='Attrition', data=df, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Chart 2: Job Role
st.subheader("Attrition by Job Role")
fig2, ax2 = plt.subplots()
sns.barplot(x='JobRole', y='Attrition', data=filtered_df, ax=ax2)
plt.xticks(rotation=90)
st.pyplot(fig2)

# Chart 3: Overtime
st.subheader("Overtime Impact")
fig3, ax3 = plt.subplots()
sns.barplot(x='OverTime', y='Attrition', data=df, ax=ax3)
st.pyplot(fig3)

# Chart 4: Work-Life Balance
st.subheader("Work-Life Balance Impact")
fig4, ax4 = plt.subplots()
sns.barplot(x='WorkLifeBalance', y='Attrition', data=df, ax=ax4)
st.pyplot(fig4) 
