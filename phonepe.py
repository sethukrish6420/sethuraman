import mysql.connector as mc
import pandas as pd
import numpy as np
import os
import streamlit as st
import plotly.express as px

st.title('phonepe_pulse_dataset')
st.image('phonepe.png',width=500)
st.markdown("Visit the [Link](https://github.com/sethukrish6420/sethuraman/blob/main/project.ipynb) for extract the data and store the data into mysql.")

st.header('Choose any one option in the menu bar') 
lines = ('agg_tran = Aggregated transaction data',
        'agg_user = Aggregated user data',
        'map_tran = Map transaction data',
        'map_user = Map user data',
        'top_tran = Top_transaction based on district',
        'top_tran_pin = Top_transaction based on pincodes',
        'top_user = Top user data based on district',
        'top_user_pin = Top user data based on pincodes')

for line in lines:
    st.write(line)   

value = ['agg_tran','agg_user','map_tran','map_user','top_tran','top_tran_pin','top_user','top_user_pin']
selected_option = st.sidebar.selectbox('Menu bar:', value)


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
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['Transacion_type'] == Transaction_type) & (df['State'] == state)]
    st.dataframe(filtered_df)
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)

if selected_option == 'agg_user':
    year = st.selectbox('choose an year',['2018', '2019', '2020', '2021', '2022'])
    Quater = st.selectbox('choose an Quater',[1,2,3,4])
    brand = st.selectbox('choose a brand',['Xiaomi', 'Samsung', 'Vivo', 'Oppo', 'OnePlus', 'Realme', 'Apple',
       'Motorola', 'Lenovo', 'Huawei', 'Others', 'Tecno', 'Gionee',
       'Asus', 'Micromax', 'Infinix', 'HMD Global', 'Lava', 'COOLPAD',
       'Lyf'])
    state = st.selectbox('choose a state',['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
       'assam', 'bihar', 'chandigarh', 'chhattisgarh',
       'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
       'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
       'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
       'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
       'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
       'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
       'uttarakhand', 'west-bengal'])
    filtered_df = df[(df['Year'] == year) & (df['Quater'] == Quater) & (df['User_brand'] == brand) & (df['State'] == state)]
    st.dataframe(filtered_df)
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)

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
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)

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
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)

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
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)

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
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)
    
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
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)
    
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
    if state == 'andaman-&-nicobar-islands':
        city = pd.DataFrame({
                     'lat':[11.66],
                     'lon':[92.73]})
        st.map(city)

    if state == 'andhra-pradesh':
        city = pd.DataFrame({
                     'lat':[14.75],
                     'lon':[78.57]})
        st.map(city)
    if state == 'arunachal-pradesh':
        city = pd.DataFrame({
                     'lat':[27.10],
                     'lon':[93.61]})
        st.map(city)
    if state == 'assam':
        city = pd.DataFrame({
                     'lat':[26.74],
                     'lon':[94.21]})
        st.map(city)
    if state == 'bihar':
        city = pd.DataFrame({
                     'lat':[25.78],
                     'lon':[87.47]})
        st.map(city)
    if state == 'chandigarh':
        city = pd.DataFrame({
                     'lat':[30.71],
                     'lon':[76.78]})
        st.map(city)
    if state == 'chhattisgarh':
        city = pd.DataFrame({
                     'lat':[22.09],
                     'lon':[82.15]})
        st.map(city)
    if state == 'dadra-&-nagar-haveli-&-daman-&-diu':
        city = pd.DataFrame({
                     'lat':[20.26],
                     'lon':[73.01]})
        st.map(city)
    if state == 'delhi':
        city = pd.DataFrame({
                     'lat':[28.66],
                     'lon':[77.23]})
        st.map(city)
        
    if state == 'goa':
        city = pd.DataFrame({
                     'lat':[15.49],
                     'lon':[73.81]})
        st.map(city)    
        
    if state == 'gujarat':
        city = pd.DataFrame({
                     'lat':[22.67],
                     'lon':[71.57]})
        st.map(city)  
        
    if state == 'haryana':
        city = pd.DataFrame({
                     'lat':[28.45],
                     'lon':[77.01]})
        st.map(city)    
        
    if state == 'himachal-pradesh':
        city = pd.DataFrame({
                     'lat':[31.10],
                     'lon':[77.16]})
        st.map(city)    
        
    if state == 'jammu-&-kashmir':
        city = pd.DataFrame({
                     'lat':[34.29],
                     'lon':[74.46]})
        st.map(city)    
        
    if state == 'jharkhand':
        city = pd.DataFrame({
                     'lat':[23.80],
                     'lon':[86.41]})
        st.map(city)
        
    if state == 'karnataka':
        city = pd.DataFrame({
                     'lat':[12.57],
                     'lon':[76.91]})
        st.map(city)   
        
    if state == 'kerala':
        city = pd.DataFrame({
                     'lat':[8.90],
                     'lon':[76.56]})
        st.map(city)    
        
    if state == 'ladakh':
        city = pd.DataFrame({
                     'lat':[34.22],
                     'lon':[77.56]})
        st.map(city)    
        
    if state == 'lakshadweep':
        city = pd.DataFrame({
                     'lat':[10.56],
                     'lon':[72.63]})
        st.map(city)     
        
    if state == 'madhya-pradesh':
        city = pd.DataFrame({
                     'lat':[21.30],
                     'lon':[76.13]})
        st.map(city)     
        
    if state == 'maharashtra':
        city = pd.DataFrame({
                     'lat':[19.25],
                     'lon':[73.16]})
        st.map(city)   
    if state == 'manipur':
        city = pd.DataFrame({
                     'lat':[24.79],
                     'lon':[93.95]})
        st.map(city)    
        
    if state == 'meghalaya':
        city = pd.DataFrame({
                     'lat':[25.57],
                     'lon':[91.88]})
        st.map(city)    
    if state == 'mizoram':
        city = pd.DataFrame({
                     'lat':[23.71],
                     'lon':[92.72]})
        st.map(city)    
    if state == 'nagaland':
        city = pd.DataFrame({
                     'lat':[25.66],
                     'lon':[94.11]})
        st.map(city)
        
    if state == 'odisha':
        city = pd.DataFrame({
                     'lat':[19.82],
                     'lon':[85.90]})
        st.map(city)    
    if state == 'puducherry':
        city = pd.DataFrame({
                     'lat':[11.93],
                     'lon':[79.83]})
        st.map(city)    
    if state == 'punjab':
        city = pd.DataFrame({
                     'lat':[31.51],
                     'lon':[75.98]})
        st.map(city)    
    if state == 'rajasthan':
        city = pd.DataFrame({
                     'lat':[26.44],
                     'lon':[74.63]})
        st.map(city)  
    if state == 'sikkim':
        city = pd.DataFrame({
                     'lat':[27.33],
                     'lon':[88.61]})
        st.map(city)   
    if state == 'tamil-nadu':
        city = pd.DataFrame({
                     'lat':[12.92],
                     'lon':[79.15]})
        st.map(city)    
    if state == 'telangana':
        city = pd.DataFrame({
                     'lat':[18.11],
                     'lon':[79.01]})
        st.map(city)    
    if state == 'tripura':
        city = pd.DataFrame({
                     'lat':[23.83],
                     'lon':[91.27]})
        st.map(city)    
    if state == 'uttar-pradesh':
        city = pd.DataFrame({
                     'lat':[27.59],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'uttarakhand':
        city = pd.DataFrame({
                     'lat':[30.32],
                     'lon':[78.05]})
        st.map(city)    
    if state == 'west-bengal':
        city = pd.DataFrame({
                     'lat':[22.58],
                     'lon':[88.32]})
        st.map(city)
    
        
