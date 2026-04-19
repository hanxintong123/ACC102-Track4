import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Financial Analysis Tool")
st.subheader("Data Source: WRDS Compustat Exported CSV File")

df = pd.read_csv("wrds_tech_data.csv")
companies = df['tic'].unique().tolist()
metrics = ['Revenue','NetIncome','GrossProfitMargin','ROE']

view_mode = st.radio("Select View Mode", ["Single Company Analysis", "Multi-Company Comparison"])
selected_companies = st.multiselect("Select Companies", companies, default=companies)
selected_metric = st.selectbox("Select Financial Metric", metrics)

df_filter = df[df['tic'].isin(selected_companies)]

plt.figure(figsize=(10,6))

if view_mode == "Single Company Analysis":
    single_company = st.selectbox("Select Single Company", selected_companies)
    temp = df_filter[df_filter['tic'] == single_company]
    plt.plot(temp['fyear'], temp[selected_metric], marker='o', label=single_company)
else:
    for tick in selected_companies:
        temp = df_filter[df_filter['tic'] == tick]
        plt.plot(temp['fyear'], temp[selected_metric], marker='o', label=tick)

plt.title(f"{selected_metric} Trend Comparison")
plt.xlabel("Year")
plt.ylabel(selected_metric)
plt.legend()

st.pyplot(plt)
st.subheader("WRDS Exported Raw Data")
st.dataframe(df_filter.round(2))