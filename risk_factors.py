import streamlit as st


def models():
    return (st.sidebar.multiselect('Risk Models for Analysis', 
            ['BOADICEA','Tyrer-Cusick', 'Gain', 
            'Claus', 'General Population', 'BRCAPro'])
            )
    
def pedigree_have_need():
    return st.sidebar.selectbox('Pedigree options', ('Choose an option', 'Create new pedigree', 'Upload pedigree'))

def upload_pedigree():
     return st.sidebar.file_uploader('Upload Pedigree', type=['PED', 'LINKAGE', 'GEDCOM', 'BOADICEA'])

def menarche_age():
    return st.sidebar.slider('Age of First Menstruation', min_value=0, max_value=45, step=1, value=14, help='use "0" if never had period')

def parity():
    return st.sidebar.slider('Number of Children', min_value=0, max_value=20, step=1)

def age_first_live_birth():
    return st.sidebar.slider('Age at First Live Birth', min_value=12, max_value=50, step=1)

def oral_contraceptive_use():
    return st.sidebar.selectbox('Oral birth control?', ('No', 'Yes'), help='This refers to birth control pill')

def oral_contraceptive_use_duration():
    return st.sidebar.number_input('Years of oral birth control use', min_value=0, step=1)

def hrt():
    return st.sidebar.selectbox('Post-menopause hormone replacement?', 
                               ('No', 'Current user', '< 5 years ago','5+ years ago' ))

def height():
    return st.sidebar.number_input('Height (inches)', min_value=40, value=60, step=1)

def weight():
    return st.sidebar.number_input('Weight (pounds)', min_value=50, value=120, step=1)

def bmi(height, weight):
    return round(703 * (weight/height**2), 1)

def alcohol_intake():
    return st.sidebar.selectbox('Drinks alcohol?', ('No', 'Yes'))

def alcohol_intake_quantity():
    return st.sidebar.number_input('How many "standard drinks" per month?', min_value=0, step=1,
    help='''In the United States, one "standard drink" (or one alcoholic drink equivalent) contains roughly 14 grams of pure alcohol, which is found in:
          12 ounces of regular beer, which is usually about 5% alcohol
          5 ounces of wine, which is typically about 12% alcohol
          1.5 ounces of distilled spirits, which is about 40% alcohol''')

def age_menopause():
    return st.sidebar.number_input('Age of menopause', max_value=80, value=55, step=1, help='use "0" if not menopausal')

def breast_density():
    return st.sidebar.number_input('BIRADS score', min_value=0, max_value=4, help='Breast density score/value')

def tubal_ligation():
    return st.sidebar.selectbox('Tubal ligation?', ('No', 'Yes'))

def endometriosis():
    return st.sidebar.selectbox('Endometriosis?', ('No', 'Yes'))

def brca_status():
    return st.sidebar.selectbox('BRCA1/2 status',
                               ('No test', 'Negative', 'BRCA1 +', 'BRCA2 +'))

def breast_biopsy():
    return st.sidebar.selectbox('Breast biopsy', 
            ('No prior biopsy', 'Prior biopsy, results unknown',
            'Hyperplasia', 'Atypical Hyperplasia', 'LCIS')
            )

def ovarian_cancer():
    return st.sidebar.selectbox('Prior/concurrent ovarian cancer?', ('No', 'Yes'))


def ashkenazi_jewish():
    return st.sidebar.selectbox('Ashkenazi Jewish ancestry?', ('No', 'Yes'))








