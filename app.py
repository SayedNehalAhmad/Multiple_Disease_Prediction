import pickle
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Multiple Disease Prediction")

# loading the saved models

diabetes_model = pickle.load(open('D:/G-7_Major_Project/G-7_Major_Project/project/module1/diabetese.sav', 'rb'))

heart_disease_model = pickle.load(open('D:/G-7_Major_Project/G-7_Major_Project/project/module2/heartDisease.sav', 'rb'))

hypertension_model = pickle.load(open('D:/G-7_Major_Project/G-7_Major_Project/project/module3/hypertension.sav', 'rb'))

parkinsons_model = pickle.load(open('D:/G-7_Major_Project/G-7_Major_Project/project/module4/parkinsons_model.sav', 'rb'))

asthama_model = pickle.load(open('D:/G-7_Major_Project/G-7_Major_Project/project/module5/asthama_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                            ['Heart Disease Prediction',
                           'Diabetes Prediction',
                            'Hypertension',
                            'Parkinsons Prediction',
                            'Asthama Prediction'],
                           menu_icon='hospital',
                           icons=['heart', 'capsule','heart-pulse', 'person','lungs'],
                           default_index=0)


#1 Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')
    
    st.write("You will need do following tests to get the required data :- ")
    # Sample data: list of features
    tests_list = [
        ["Blood Sugar Test", "Blood Pressure Test", "A1C Test"],
        ["C-Peptide Test", "Family Medical History"]
    ]


    # Create columns 
    cols = st.columns(2)

    # Distribute list items across columns
    for i, feature_set in enumerate(tests_list):
        with cols[i % 3]:  # Distributes items evenly across columns
            for feature in feature_set:
                st.markdown(f"- {feature}")  # Bullet points

    st.markdown("---")
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

#2 Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    # with st.container():
    #     st.write("This is inside the container")

    # Sample data containing lists
    st.write("You will need do following tests to get the required data :- ")
    
    tests_list = [
        ["Electrocardiogram (ECG)", "Blood Pressure Test", "Lipid Profile Test"],
        ["Blood Sugar Test", "Coronary Angiography (Fluoroscopy Test)", "Thallium Stress Test"]
    ]

    # Create columns 
    cols = st.columns(2)

    # Distribute list items across columns
    for i, feature_set in enumerate(tests_list):
        with cols[i % 3]:  # Distributes items evenly across columns
            for feature in feature_set:
                st.markdown(f"- {feature}")  # Bullet points

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


#3 Hypertension Prediction Page
if selected == 'Hypertension':

    # page title
    st.title('Hypertension Prediction using ML')

    # Sample data containing lists
    st.write("You will need do following tests to get the required data :- ")
    
    tests_list = [
        ["Sphygmomanometer Measurement", "Liver Function Test (LFT)", "Lipid Profile Test"],
        ["Blood Sugar Test"]
    ]

    # Create columns 
    cols = st.columns(2)

    # Distribute list items across columns
    for i, feature_set in enumerate(tests_list):
        with cols[i % 3]:  # Distributes items evenly across columns
            for feature in feature_set:
                st.markdown(f"- {feature}")  # Bullet points

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        waist = st.text_input('Waist size')

    with col1:
        BP_HIGH = st.text_input('BP_HIGH')

    with col2:
        BP_LWST = st.text_input('BP_LWST')

    with col3:
        BLDS = st.text_input('BLDS')

    with col1:
        TOT_CHOLE = st.text_input('TOT_CHOLE')

    with col2:
        SGOT_ASL = st.text_input('SGOT_ASL')

    with col3:
        SGPT_ALT = st.text_input('SGPT_ALT')

    with col1:
        GAMMA_GPT = st.text_input('GAMMA_GPT')

    


    # code for Prediction
    hypertension_diagnosis = ''

    # creating a button for Prediction

    if st.button('Hypertension Test Result'):

        user_input = [age, gender, waist, BP_HIGH, BP_LWST, BLDS, TOT_CHOLE, SGOT_ASL, SGPT_ALT, GAMMA_GPT]

        user_input = [float(x) for x in user_input]

        hypertension_prediction = hypertension_model.predict([user_input])

        if hypertension_prediction[0] == 1:
            hypertension_diagnosis = 'The person is having hypertension'
        else:
            hypertension_diagnosis = 'The person does not have hypertension'

    st.success(hypertension_diagnosis)


#4 Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    st.write("You will need do following tests to get the required data :- ")
    
    tests_list = [
        [" Voice Acoustic Analysis (MDVP/Praat Software)", "Nonlinear Speech Signal Processing (MATLAB/Praat)", " Neurological Examination"]
    ]

    # Create columns 
    cols = st.columns(1)

    # Distribute list items across columns
    for i, feature_set in enumerate(tests_list):
        with cols[i % 3]:  # Distributes items evenly across columns
            for feature in feature_set:
                st.markdown(f"- {feature}")  # Bullet points

    st.markdown("---")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


#5 Asthama Prediction Page
if selected == 'Asthama Prediction':

    # page title
    st.title('Asthama Prediction using ML')

    # Sample data containing lists
    st.write("You will need do following tests to get the required data :- ")
    
    tests_list = [
        ["Spirometry (FEV1 & FVC)", "Bronchial Challenge Test", "Skin Prick / IgE Blood Test"],
        ["Peak Flow Measurement", " pH Monitoring"]
    ]

    # Create columns 
    cols = st.columns(2)

    # Distribute list items across columns
    for i, feature_set in enumerate(tests_list):
        with cols[i % 3]:  # Distributes items evenly across columns
            for feature in feature_set:
                st.markdown(f"- {feature}")  # Bullet points

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        EducationLevel = st.text_input('Education Level')

    with col4:
        BMI = st.text_input('BMI')

    with col1:
        Smoking = st.text_input('Smoking')

    with col2:
        PhysicalActivity = st.text_input('Physical Activity')

    with col3:
        DietQuality = st.text_input('Diet Quality')

    with col4:
        SGOT_ASL = st.text_input('SGOT_ASL')

    with col1:
        SleepQuality = st.text_input('Sleep Quality')

    with col2:
        PollutionExposure = st.text_input('Pollution Exposure')

    with col3:
        PollenExposure = st.text_input('Pollen Exposure')
    
    with col4:
        DustExposure = st.text_input('Dust Exposure')

    with col1:
        PetAllergy = st.text_input('Pet Allergy')

    with col2:
        FamilyHistoryAsthma = st.text_input('Family History Asthma')

    with col3:
        HistoryOfAllergies = st.text_input('History Of Allergies')

    with col4:
        Eczema = st.text_input('Eczema')

    with col1:
        HayFever = st.text_input('Hay Fever')

    with col2:
        GastroesophagealReflux = st.text_input('Gastroesophageal Reflux')

    with col3:
        LungFunctionFEV1 = st.text_input('Lung Function FEV1')

    with col4:
        LungFunctionFVC = st.text_input('Lung Function FVC')

    with col1:
        Wheezing = st.text_input('Wheezing')

    with col2:
        ShortnessOfBreath = st.text_input('Shortness Of Breath')

    with col3:
        ChestTightness = st.text_input('Chest Tightness')

    with col4:
        Coughing = st.text_input('Coughing')

    with col1:
        NighttimeSymptoms = st.text_input('Nighttime Symptoms')

    with col2:
        ExerciseInduced = st.text_input('Exercise Induced')




    # code for Prediction
    asthama_diagnosis = ''

    # creating a button for Prediction

    if st.button('Asthama Test Result'):

        user_input = [age, gender, EducationLevel, BMI, Smoking, PhysicalActivity, DietQuality, SleepQuality, PollutionExposure, PollenExposure, DustExposure, PetAllergy, FamilyHistoryAsthma, HistoryOfAllergies, Eczema, HayFever, GastroesophagealReflux, LungFunctionFEV1, LungFunctionFVC, Wheezing, ShortnessOfBreath, ChestTightness, Coughing, NighttimeSymptoms, ExerciseInduced]

        user_input = [float(x) for x in user_input]

        asthama_prediction = asthama_model.predict([user_input])

        if asthama_prediction[0] == 1:
            asthama_diagnosis = 'The person is having hypertension'
        else:
            asthama_diagnosis = 'The person does not have hypertension'

    st.success(asthama_diagnosis)

