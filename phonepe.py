import mysql.connector as mc
import pandas as pd
import numpy as np
import os
import streamlit as st
import plotly.express as px

st.title('phonepe_pulse_dataset')
st.title('phonepe_pulse_dataset')
st.markdown("Visit the [Link](https://github.com/sethukrish6420/sethuraman/blob/main/project.ipynb) for extract the data and store the data into mysql.")
value = ['agg_tran','agg_user','map_tran','map_user','top_tran','top_tran_pin','top_user','top_user_pin']
selected_option = st.sidebar.selectbox('Choose an option:', value)

import mysql.connector
mydb = mysql.connector.connect(
         host = 'localhost',
         user = 'root',
         password = '6420',
         database = 'mydatabase')
mycursor = mydb.cursor()
mycursor.execute(f'SELECT * FROM {selected_option}')
data = mycursor.fetchall()

if selected_option == 'agg_tran':
    df = pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transacion_type','Transacion_count','Transacion_amount'])
if selected_option == 'agg_user':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','User_brand','User_count','User_percentage'])
if selected_option == 'map_tran':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transacion_district','Transacion_count','Transacion_amount'])
if selected_option == 'map_user':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transacion_district','registeredUsers'])
if selected_option == 'top_tran':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transaction_district','dis_tran_count','dis_tran_amount'])
if selected_option == 'top_tran_pin':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transaction_pincode','pin_tran_count','pin_tran_amount'])
if selected_option == 'top_user':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transaction_district','registeredUsers'])
if selected_option == 'top_user_pin':
    df= pd.DataFrame(data, columns=['serial_no','State','Year','Quater','Transaction_pincode','registeredUsers'])
    
if selected_option == 'agg_tran':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    Transaction_type = st.selectbox('choose an Transaction_type',['Recharge & bill payments', 'Peer-to-peer payments',
       'Merchant payments', 'Financial Services', 'Others'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['Transacion_type'] == Transaction_type)]
    st.dataframe(filtered_df)
if selected_option == 'agg_user':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    brand = st.selectbox('choose a brand',['Xiaomi', 'Samsung', 'Vivo', 'Oppo', 'OnePlus', 'Realme', 'Apple',
       'Motorola', 'Lenovo', 'Huawei', 'Others', 'Tecno', 'Gionee',
       'Asus', 'Micromax', 'Infinix', 'HMD Global', 'Lava', 'COOLPAD',
       'Lyf'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['User_brand'] == brand)]
    st.dataframe(filtered_df) 
if selected_option == 'map_tran':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['State'] == state)]
    st.dataframe(filtered_df)
    
if selected_option == 'map_user':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['State'] == state)]
    st.dataframe(filtered_df) 

if selected_option == 'top_tran':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['State'] == state)]
    st.dataframe(filtered_df) 
    
if selected_option == 'top_tran_pin':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['State'] == state)]
    st.dataframe(filtered_df) 

if selected_option == 'top_user':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['State'] == state)]
    st.dataframe(filtered_df) 
    
if selected_option == 'top_user_pin':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['State'] == state)]
    st.dataframe(filtered_df) 

