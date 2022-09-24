import streamlit as st
import plotly.express as px
import seaborn as sn
df_iris = sn.load_dataset('iris')
fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',color='species',symbol='species')
st.write("""# 3d scatter plot for the IRIS dataset using plotly""")
st.plotly_chart(fig)