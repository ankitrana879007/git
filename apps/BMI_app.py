import streamlit as st  #BMI = body mass index check wether a person have healthy weight according to there body mass
st.title('BMI CALCULATOR')  #BMI formula= weight/height **2 *1000

st.write('Here you can calculate your BMI')

height = st.number_input('Enter your height in cm: ')
weight = st.number_input('Enter your weight in kg: ')

if st.button('Calculate BMI'):
    if height > 0 and weight > 0:
        bmi = weight/height**2 *1000
        st.success(f'Your Bmi is {bmi:2f}')    #2f = show it to only 2 digit after decimal, st.success= show bmi in green color
        if bmi < 18.5:
            st.warning('You are underweight')   #st.warning = make text in yellow color
        elif 18.5 <= bmi < 25:
            st.info('You have a normal weight') #st.info = make text in blue color
        else:
            st.error('YOu are overweight')
    else:
        st.error('Please enter valid height and weight')    #st.error = make text in red color

    # for code work write --
    #python -m streamlit run BMI_app.py

