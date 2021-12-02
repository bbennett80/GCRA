# https://bcrisktool.cancer.gov/about.html

import streamlit as st
import streamlit.components.v1 as components


def pedigree_chart():
    with open('devel/docs/index.html') as p:
        pedigree = p.read()

    return components.html(pedigree, height=500)


st.title('Genetic Cancer Risk Assessment')

#sidebar elements
model = st.sidebar.selectbox('Risk Model', ('BOADICEA','Tyrer-Cusick', 'Gain', 'Claus', 'General Population', 'BRCAPro'))
st.subheader(model)


# pedigree
pedigree_chart()


def risk_factors():
    """idea from https://github.com/CCGE-BOADICEA/bws"""
    menarche_age = st.sidebar.slider('Age of First Menstruation', min_value=0, max_value=45, step=1, value=14, help='use "0" if never had period')
    parity = st.sidebar.slider('Number of Children', min_value=0, max_value=20, step=1)
    age_first_live_birth = st.sidebar.slider('Age of First Live Birth', 16, 50, 1)
    oral_contraceptive_use = st.sidebar.selectbox('Have you used oral birth control?', ('Yes', 'No'), help='This refers to birth control pill')
    hrt = st.sidebar.selectbox('Have you used post-menopause hormone replacement?', ('Yes', 'No'))

    height = st.sidebar.number_input('Height (inches)', min_value=40, value=60, step=1)
    weight = st.sidebar.number_input('Weight (pounds)', min_value=50, value=120, step=1)
    bmi = round(703 * (weight/height**2), 1)

    alcohol_intake = st.sidebar.selectbox('Do you drink alcohol?', ('Yes', 'No'))
    age_menopause = st.sidebar.number_input('Age of menopause', min_value=30, value=55, step=1, help='use "0" if not menopausal')
    breast_density = st.sidebar.number_input('BIRADS score', min_value=0, max_value=4, help='Breast density score/value')
    tubal_ligation = st.sidebar.selectbox('Have you had a tubal ligation?', ('Yes', 'No'))
    endometriosis = st.sidebar.selectbox('Have you had endometriosis?', ('Yes', 'No'))

    risk_factors = {
        'menarche': menarche_age,
        'parity': parity,
        'age_first_live_birth': age_first_live_birth,
        'oral_contraceptive_use': oral_contraceptive_use,
        'hrt' :hrt,
        'bmi': bmi,
        'alcohol_intake' :alcohol_intake,
        'age_menopause': age_menopause,
        'breast_density': breast_density,
        'tubal_ligation': tubal_ligation,
        'endometriosis': endometriosis
    }
    return risk_factors


st.write(risk_factors())



def tyrer_cusick(age, height, weight, menarche):
    pass



def BOADICEA():
    """https://www.nature.com/articles/6602175.pdf"""
    pass


