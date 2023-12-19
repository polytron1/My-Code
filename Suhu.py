import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
 
# Header
st.header('Fariq :sparkles:')
st.subheader('Plot')


option =  st.selectbox(
 'satuan',
 ('C', 'F', 'R', 'K')
)

f1 = st.number_input('Nilai f1 = ',value=1)

st.caption('Copyright © Nugroho Adi Pramono 2023')
