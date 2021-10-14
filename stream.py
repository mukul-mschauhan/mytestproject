import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as pl
import plotly.express as pel
# All the remaining libraries that are needed to solve the Mini Projects
# Sklearn, Scipy...
st.sidebar.subheader("Mini Project Questions")
st.header("Exploratory Data Analysis – Mini Project")
st.subheader("Learning how to explore data...")

st.write('''
        **Data:**The bigcity data frame has 49 rows and 2 columns. The measurements are the population (in 1000's) of 49 U.S. cities in 1920 and 1930. The 49 cities are a random sample taken from the 196 largest cities in 1920.
         ''')
city = pd.read_csv("data/bigcity.csv")

data = st.sidebar.checkbox("Data", True)
if data:
    city = pd.read_csv("data/bigcity.csv")
    st.markdown("**Preview of the Data**")
    st.write(city.head())

# exploring the data
#st.markdown("**Statistical Summary of the Data**")
#st.write(city.describe())
#st.markdown("---")

# Form of Question
q1 = st.sidebar.checkbox("Question1", True)
if q1:
    st.write("**Q.1. Measure spread – variance and standard deviation**")
    pressed = st.button("Q.1. Solution", True)
    if pressed:
        #plt.figure(figsize=(12,4))
        #plt.subplot(1, 2, 1)
        fig = plt.figure()
        sns.boxplot(y='u',data=city,palette='inferno')
        #plt.subplot(1, 2, 2)
        fig2 = plt.figure()
        sns.boxplot(y='x',data=city,palette='inferno')
        #plt.tight_layout()
        st.pyplot(fig)
        st.pyplot(fig2)
    st.markdown("---")

# Q.2
# Form of Question
q2 = st.sidebar.checkbox("Question2", True)
if q2:
    st.write("**Q.2. Provide Statistical Summary**")
    st.caption("Approach - Find the Mean, Standard Deviation of the Data..")
    pressed = st.button("Q.2. Solution", True)
    if pressed:
        st.subheader("Summary Statistics of the Data")
        with st.echo():
            pop_1920_mean = city['u'].mean() # Calculating the Mean
            pop_1920_std  = city['u'].std()
        pop_1920_var  = city['u'].var()
        pop_1930_mean = city['x'].mean()
        pop_1930_std = city['x'].std()
        pop_1930_var = city['x'].var()    
        st.write('**Mean 1920 Population:** '+str(round(pop_1920_mean,2)))
        st.write('**Std 1920 Population:** '+str(round(pop_1920_std,2)))
    st.markdown("---")

# Q.3.
q3 = st.sidebar.checkbox("Question3", True)
if q3:
    st.write("**Q.3. Explore relationships between variables using scatterplots and two-way cross tabulations**")
    pressed = st.button("Q.3. Solution", True)
    if pressed:
        with st.echo():
            # Tip - Install Plotly...
            fig = pel.scatter(city, x = 'x', 
                        y ='u', color = "u").\
                            update_layout(title = "My Title",
                                            xaxis_title = "Xaxis",
                                            yaxis_title = "Yaxis")
        st.plotly_chart(fig)