import numpy as np
import pandas as pd
import streamlit as st


def main():
  st.title("Odd Even")
  html_temp = """
  <div style="background-color:black;padding:10px">
  <h2 style="color:black;text-align:center;">Division of 2 Numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Enter Number")
  
  if(num1%2==0):
    result = 'Even'
  else:
    result='Odd'
    
  st.success('The output is {}'.format(result))
  
if __name__=='__main__':
  main()
