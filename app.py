import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.set_page_config(page_title="Attrition Dashboard", layout="wide")

st.title("Workforce Attrition Analysis Dashboard")
st.markdown("Analyze employee attrition patterns and key risk factors")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Palo Alto Networks.csv")

df = load_data()

# Create AgeGroup
df['AgeGroup'] = pd.cut(df['Age'],
                       bins=[18,30,40,50,60],
                       labels=['18-30','30-40','40-50','50-60'])

# Sidebar filters
st.sidebar.header("Filters")

department = st.sidebar.selectbox(
    "Select Department",
    options=["All"] + list(df['Department'].unique())
)

overtime = st.sidebar.selectbox(
    "Select Overtime",
    options=["All"] + list(df['OverTime'].unique())
)

# Apply filters
filtered_df = df.copy()

if department != "All":
    filtered_df = filtered_df[filtered_df['Department'] == department]

if overtime != "All":
    filtered_df = filtered_df[filtered_df['OverTime'] == overtime]

# Metrics
st.subheader("Key Metrics")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Employees", len(df))

with col2:
    st.metric("Attrition Rate (%)", f"{df['Attrition'].mean() * 100:.2f}")

# Filtered metric
st.subheader("Filtered Attrition Rate")
st.write(f"{filtered_df['Attrition'].mean() * 100:.2f}%")

# Charts

# 1. Department
st.subheader("Attrition by Department")
fig1, ax1 = plt.subplots()
sns.barplot(x='Department', y='Attrition', data=df, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# 2. Job Role
st.subheader("Attrition by Job Role")
fig2, ax2 = plt.subplots()
sns.barplot(x='JobRole', y='Attrition', data=filtered_df, ax=ax2)
plt.xticks(rotation=90)
st.pyplot(fig2)

# 3. Overtime
st.subheader("Overtime Impact")
fig3, ax3 = plt.subplots()
sns.barplot(x='OverTime', y='Attrition', data=df, ax=ax3)
st.pyplot(fig3)

# 4. Work-Life Balance
st.subheader("Work-Life Balance Impact")
fig4, ax4 = plt.subplots()
sns.barplot(x='WorkLifeBalance', y='Attrition', data=df, ax=ax4)
st.pyplot(fig4)

# 5. Age Group
st.subheader("Attrition by Age Group")
fig5, ax5 = plt.subplots()
sns.barplot(x='AgeGroup', y='Attrition', data=df, ax=ax5)
st.pyplot(fig5)
