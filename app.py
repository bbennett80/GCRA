# https://bcrisktool.cancer.gov/about.html
# https://ems-trials.org/riskevaluator/documents/Breast_cancer_prediction_model.pdf

import streamlit as st
import streamlit.components.v1 as components

import risk_factors as risk


st.title('Genetic Cancer Risk Assessment')

# pedigree
def draw_pedigree_chart():
    with open('./src/index.html') as p:
        pedigree = p.read()

    return components.html(pedigree, height=500)


# sidebar elements
models = risk.models()
pedigree_have_need = risk.pedigree_have_need()

if pedigree_have_need == 'Choose an option':
    pass
elif pedigree_have_need == 'Create new pedigree':
    draw_pedigree_chart = draw_pedigree_chart()
else:
    upload_pedigree = risk.upload_pedigree()

menarche_age = risk.menarche_age()
parity = risk.parity()
age_first_live_birth = risk.age_first_live_birth()
oral_contraceptive_use = risk.oral_contraceptive_use()

if oral_contraceptive_use == 'Yes':
    oral_contraceptive_use_duration = risk.oral_contraceptive_use_duration()
else:
    oral_contraceptive_use_duration = 0

hrt = risk.hrt()
height = risk.height()
weight = risk.weight()
bmi = risk.bmi(height, weight)
alcohol_intake = risk.alcohol_intake()

if alcohol_intake == 'Yes':
    alcohol_intake_quantity = risk.alcohol_intake_quantity()
else:
    alcohol_intake_quantity = 0

age_menopause = risk.age_menopause()
breast_density = risk.breast_density()
tubal_ligation = risk.tubal_ligation()
endometriosis = risk.endometriosis()
brca_status = risk.brca_status()
breast_biopsy = risk.breast_biopsy()
ovarian_cancer = risk.ovarian_cancer()
ashkenazi_jewish = risk.ashkenazi_jewish()


def risk_factors():
    risk_factors = {
        'menarche': menarche_age,
        'parity': parity,
        'age_first_live_birth': age_first_live_birth,
        'oral_contraceptive_use': oral_contraceptive_use,
        'oral_contraceptive_use_duration': oral_contraceptive_use_duration,
        'hrt': hrt,
        'bmi': bmi,
        'alcohol_intake': alcohol_intake,
        'alcohol_intake_quantity': alcohol_intake_quantity,
        'age_menopause': age_menopause,
        'breast_density': breast_density,
        'tubal_ligation': tubal_ligation,
        'endometriosis': endometriosis,
        'brca_status': brca_status,
        'breast_biopsy': breast_biopsy,
        'ovarian_cancer': ovarian_cancer,
        'ashkenazi_jewish': ashkenazi_jewish
    }
    return risk_factors



def tyrer_cusick(age, height, weight, menarche_age, parity, age_menopause, hrt, 
                brca_status, breast_biopsyi, ovarian_cancer, ashkenazi_jewish):
    pass

def BOADICEA():
    """https://www.nature.com/articles/6602175.pdf"""
    pass


