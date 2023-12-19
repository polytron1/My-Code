import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
 
# Header
st.header('Fariq :sparkles:')
st.subheader('Plot')

nama = st.text_input('Nama', 'Fariq', label_visibility='collapsed')
st.write('Halo', nama)

f1 = st.number_input('Nilai f1 = ',value=1)

st.caption('Copyright © Nugroho Adi Pramono 2023')
