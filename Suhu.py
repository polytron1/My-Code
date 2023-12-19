import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
 
# Header
st.header('Fariq :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)
 
with c1:
   x = st.number_input('Suhu = ',value=100)
with c2:
   satuan =  st.selectbox(
     'satuan',
     ('C', 'F', 'R', 'K'))

st.caption('Copyright © Nugroho Adi Pramono 2023')
