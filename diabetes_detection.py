#pip install streamlit
#pip install pandas
#pip install sklearn

import streamlit as st
import pandas as pd
from PIL import Image 
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv(r'C:\Users\lenovo\OneDrive\Desktop\P4 diabetes prediction ml\diabetes.csv')

st.title('Diabetes Checkup')

st.subheader('Training Data')
st.write(df.describe())

st.subheader('Visualisation')
st.bar_chart(df)

x = df.drop(['Outcome'], axis = 1)
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 0)

def user_report():
    pregnancies = st.sidebar.slider('Pregnancies', 0,17,3 )
    glucose = st.sidebar.slider('Glucose', 0,200, 120 )
    bp = st.sidebar.slider('Blood Pressure', 0,122, 70 )
    skinthickness = st.sidebar.slider('Skin Thickness', 0,100, 20 )
    insulin = st.sidebar.slider('Insulin', 0,846, 79 )
    bmi = st.sidebar.slider('BMI', 0, 67, 20 )
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.0,2.4, 0.47 )
    age = st.sidebar.slider('Age', 21,88, 33 )
    
    user_report_data = {
        'pregnancies':pregnancies,
        'glucose':glucose,
        'bp':bp,
        'skinthickness':skinthickness,
        'insulin':insulin,
        'bmi':bmi,
        'dpf':dpf,
        'age':age,
    }
    report_data =pd.DataFrame(user_report_data,index=[0])
    return report_data

user_data = user_report()

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

st.subheader('Accuracy:')
st.write(str(accuracy_score(y_test, rf.predict(x_test))*100)+'%')

# Make a prediction for the user
user_result = rf.predict(user_data.values)
# Display the prediction to the user
st.subheader('Your report:')
output=''
if user_result[0] == 0:
  output = """You are not at high risk of diabetes. However, it is still important to maintain a healthy lifestyle to reduce your risk in the future. This includes eating a healthy diet, exercising regularly, and maintaining a healthy weight."""
else:
  output = """You are at high risk of diabetes. It is important to see a doctor to get tested for diabetes and to discuss your risk factors. There are things you can do to reduce your risk of diabetes, such as eating a healthy diet, exercising regularly, and maintaining a healthy weight."""

st.write(output)
