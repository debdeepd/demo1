import streamlit as st
import pandas as pd
import numpy as np
import time
a=[1,2,3,4,5,6,7,8]

n=np.array(a)
nd=n.reshape((2,4))

data = pd.read_csv('C:\\Users\\Debjit Dutta\\OneDrive\\Desktop\\project\\attachment_Salary-Data_lyst.csv')

st.dataframe(data,width = 500,height = 1000)
st.table(data)
st.write(data)

@st.cache_data
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())

if st.checkbox("2"):
    st.write(ret_time())    