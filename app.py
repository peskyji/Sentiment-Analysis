import requests
import streamlit as st
import json

st.header("hi")
data = {'num1':123, 'num2':0.01}
ans = requests.post(url='http://127.0.0.1:8000/calculate', data = json.dumps(data))

st.write(f"recieved response - {ans.text}")