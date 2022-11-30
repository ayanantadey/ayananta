import numpy as np
import pandas as pd
import streamlit as st


def main():
  st.title("Pintu dar - Boyosh")
  html_temp = """
  <div style="background-color:black;padding:10px">
  <h2 style="color:black;text-align:center;">Division of 2 Numbers</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Enter Number")
  if(num1==52):
    result = 'Sathik Uttar'
  elseif(num1<52):
    result='Punaray chesta korun, ektu kom hoye gelo'
  else(num1>52):
    result='Etotao noy, aapni barabari kore felechen'
  st.success('The output is {}'.format(result))
  
if __name__=='__main__':
  main()
