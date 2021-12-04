# https://bcrisktool.cancer.gov/about.html

import streamlit as st
import streamlit.components.v1 as components


st.title('Genetic Cancer Risk Assessment')

# sidebar elements
model = st.sidebar.selectbox('Risk Model', ('BOADICEA','Tyrer-Cusick', 'Gain', 'Claus', 'General Population', 'BRCAPro'))
st.subheader(model)

def upload_pedigree():
    return st.sidebar.file_uploader('Upload Pedigree', type=['PED', 'LINKAGE', 'GEDCOM', 'BOADICEA'])

def menarche_age():
    return st.sidebar.slider('Age of First Menstruation', min_value=0, max_value=45, step=1, value=14, help='use "0" if never had period')

def parity():
    return st.sidebar.slider('Number of Children', min_value=0, max_value=20, step=1)

def age_first_live_birth():
     return st.sidebar.slider('Age at First Live Birth', min_value=16, max_value=50, step=1)

def oral_contraceptive_use():
    return st.sidebar.selectbox('Have you used oral birth control?', ('No', 'Yes'), help='This refers to birth control pill')

def oral_contraceptive_use_duration():
    return st.sidebar.number_input('Years of oral birth control use', min_value=0, step=1)

def hrt():
    return st.sidebar.selectbox('Have you used post-menopause hormone replacement?', ('No', 'Yes'))

def hrt_duration():
    return st.sidebar.number_input('Years of hormone replacement therapy use', min_value=0, step=1)

def height():
    return st.sidebar.number_input('Height (inches)', min_value=40, value=60, step=1)

def weight():
    return st.sidebar.number_input('Weight (pounds)', min_value=50, value=120, step=1)

def bmi(height, weight):
    return round(703 * (weight/height**2), 1)

def alcohol_intake():
    return st.sidebar.selectbox('Do you drink alcohol?', ('No', 'Yes'))

def alcohol_intake_quantity():
    return st.sidebar.number_input('How many "standard drinks" do you have per month?', min_value=0, step=1,
            help='''In the United States, one "standard drink" (or one alcoholic drink equivalent) contains roughly 14 grams of pure alcohol, which is found in:

            12 ounces of regular beer, which is usually about 5% alcohol
            5 ounces of wine, which is typically about 12% alcohol
            1.5 ounces of distilled spirits, which is about 40% alcohol''')

def age_menopause():
    return st.sidebar.number_input('Age of menopause', min_value=30, value=55, step=1, help='use "0" if not menopausal')

def breast_density():
    return st.sidebar.number_input('BIRADS score', min_value=0, max_value=4, help='Breast density score/value')

def tubal_ligation():
    return st.sidebar.selectbox('Have you had a tubal ligation?', ('No', 'Yes'))

def endometriosis():
    return st.sidebar.selectbox('Have you had endometriosis?', ('No', 'Yes'))

upload_pedigree = upload_pedigree()
menarche_age = menarche_age()
parity = parity()
age_first_live_birth = age_first_live_birth()
oral_contraceptive_use = oral_contraceptive_use()
if oral_contraceptive_use == 'Yes':
    oral_contraceptive_use_duration = oral_contraceptive_use_duration()
hrt = hrt()
if hrt == 'Yes':
    hrt_duration = hrt_duration()
else:
    hrt_duration = 0
height = height()
weight = weight()
bmi = bmi(height, weight)
alcohol_intake = alcohol_intake()
if alcohol_intake == 'Yes':
    alcohol_intake_quantity = alcohol_intake_quantity()
else:
    alcohol_intake_quantity = 0
age_menopause = age_menopause()
breast_density = breast_density()
tubal_ligation = tubal_ligation()
endometriosis = endometriosis()

def risk_factors():
    risk_factors = {
        'menarche': menarche_age,
        'parity': parity,
        'age_first_live_birth': age_first_live_birth,
        'oral_contraceptive_use': oral_contraceptive_use,
        'oral_contraceptive_use_duration': oral_contraceptive_use_duration,
        'hrt' :hrt,
        'hrt_duration': hrt_duration,
        'bmi': bmi,
        'alcohol_intake' :alcohol_intake,
        'alcohol_intake_quantity': alcohol_intake_quantity,
        'age_menopause': age_menopause,
        'breast_density': breast_density,
        'tubal_ligation': tubal_ligation,
        'endometriosis': endometriosis
    }
    return risk_factors



# pedigree
def pedigree_chart():
    with open('./src/index.html') as p:
        pedigree = p.read()

    return pedigree 

st.write(risk_factors())
#pedigree_chart = pedigree_chart()
#components.html(pedigree_chart, height=500)


def tyrer_cusick(age, height, weight, menarche):
    pass

def BOADICEA():
    """https://www.nature.com/articles/6602175.pdf"""
    pass
















# def risk_factors():
    # """idea from https://github.com/CCGE-BOADICEA/bws"""
    # menarche_age = st.sidebar.slider('Age of First Menstruation', min_value=0, max_value=45, step=1, value=14, help='use "0" if never had period')
    # parity = st.sidebar.slider('Number of Children', min_value=0, max_value=20, step=1)
    # age_first_live_birth = st.sidebar.slider('Age of First Live Birth', 16, 50, 1)
    # oral_contraceptive_use = st.sidebar.selectbox('Have you used oral birth control?', ('Yes', 'No'), help='This refers to birth control pill')
    # hrt = st.sidebar.selectbox('Have you used post-menopause hormone replacement?', ('Yes', 'No'))

    # height = st.sidebar.number_input('Height (inches)', min_value=40, value=60, step=1)
    # weight = st.sidebar.number_input('Weight (pounds)', min_value=50, value=120, step=1)
    # bmi = round(703 * (weight/height**2), 1)

    # alcohol_intake = st.sidebar.selectbox('Do you drink alcohol?', ('Yes', 'No'))
    # age_menopause = st.sidebar.number_input('Age of menopause', min_value=30, value=55, step=1, help='use "0" if not menopausal')
    # breast_density = st.sidebar.number_input('BIRADS score', min_value=0, max_value=4, help='Breast density score/value')
    # tubal_ligation = st.sidebar.selectbox('Have you had a tubal ligation?', ('Yes', 'No'))
    # endometriosis = st.sidebar.selectbox('Have you had endometriosis?', ('Yes', 'No'))
