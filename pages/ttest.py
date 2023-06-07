import streamlit as st
import pandas as pd
from scipy.stats import t
from scipy.stats import ttest_1samp


st.set_page_config(page_title = "Ttest")
st.title("Ttest")

df = pd.read_csv("https://raw.githubusercontent.com/ethanweed/pythonbook/main/Data/zeppo.csv")

with st.expander('view data'):
    st.dataframe(df.transpose())

with st.expander('view statistics'):
    st.dataframe(df.describe().transpose())

st.write('##  Constructing Hypothesis')

alpha = 0.05
alpha_t = t.ppf(q=1-alpha, df=34)

null_mean = 67.5
t_score, p_value = ttest_1samp(a=df['grades'], popmean=null_mean)

clicked = st.button('do the T test')

if clicked:
    if t_score<alpha_t:
        st.write('#### reject H0')       
    else:
        st.write('#### can not reject H0')