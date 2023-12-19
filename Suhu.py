import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
 
# Header
st.header('Fariq :sparkles:')
st.subheader('Plot')

c1, c2 = st.columns(2)
 
with c1:
   x = st.number_input('Suhu = ',value=100)
   st.write('Dikonversi ke: ')
with c2:
   satuan =  st.selectbox(
     'satuan',
     ('C', 'F', 'R', 'K'), key='k1')
   konversi =  st.selectbox(
     'konversi',
     ('C', 'F', 'R', 'K'), key='k2')

st.caption('Copyright © Nugroho Adi Pramono 2023')
