# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 05:37:41 2023

@author: mughilan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

prostate_model=pickle.load(open('C:/Users/mughilan/OneDrive/Desktop/Multiple disease prediction/saved models/prostate.sav','rb'))
hepatitis_model=pickle.load(open('C:/Users/mughilan/OneDrive/Desktop/Multiple disease prediction/saved models/hepatitis.sav','rb'))


#sidebar for navigation

with st.sidebar:
    selected=option_menu('Multiple disease prediction System',
                         ['Prostate cancer prediction','Hepatitis-C prediction'],
                         icons=['heart pulse fill','activity'],
                         default_index=0)
    

# Prostate prediction page
if (selected=='Prostate cancer prediction'):
    
    # page title
    st.title('Prostate cancer prediction using ML')
    
    # getting the input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        radius=st.text_input('Radius of tumour')
     
    with col2:
        texture=st.text_input('Texture of tumour')
        
    with col3:
        perimeter=st.text_input('Perimeter of tumour')
    
    with col1:
        area=st.text_input('Area of tumour')
     
    with col2:
        smoothness=st.text_input('Smoothness of tumour')
        
    with col3:
        compactness=st.text_input('Compactness of tumour')
        
    with col1:
          symmetry=st.text_input('Symmetry of tumour')
       
    with col2:
          fractal_dimension=st.text_input('Fractal Dimension of tumour')
          
    with col3:
          aspect_ratio=st.text_input('Aspect Ratio of tumour')
          
    with col1:
        perimeter_to_area_ratio=st.text_input('Perimeter to area ratio of tumour')
        
    #code for prediction
    prostate_diagnosis=''
    
    #creating button for prediction
    if st.button('Prostate cancer result'):
        prostate_prediction=prostate_model.predict([[radius,texture,perimeter,area,smoothness,compactness,symmetry,fractal_dimension,aspect_ratio,perimeter_to_area_ratio]]) 
        
        if(prostate_prediction[0]=='M'):
            prostate_diagnosis='The person has malignant tumour'
            
        if(prostate_prediction[0]=='B'):
            prostate_diagnosis='The person has benign tumour'
            
            
    st.success(prostate_diagnosis)        
        
        
    
    
        
           
          
        
        
# Hepatitis prediction page 
if(selected=='Hepatitis-C prediction'):
    
    #page title
    st.title('Hepatitis-C prediction using ML')
    
    # getting the input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        Age=st.text_input('Age of patient')
    
    
    with col2:
        ALB=st.text_input('Albumin level')
     
    with col3:
        ALP=st.text_input('Alkaline phosphatase level')
        
    with col1:
        ALT=st.text_input('Alanine transaminase level')
    
    with col2:
        AST=st.text_input('Aspartate transaminase level')
     
    with col3:
        BIL=st.text_input('Bilirubin level')
        
    with col1:
        CHE=st.text_input('Cholinesterase level')
        
    with col2:
          CHOL=st.text_input('Cholestral level')
       
    with col3:
          CREA=st.text_input('Creatinine level')
          
    with col1:
          GGT=st.text_input('Gamma-GLutamyl transferase level')
          
    with col2:
        PROT=st.text_input('Protein level')
        
    with col3:
        EnzymeRatio=st.text_input('Enzyme Ratio level')
        
        
    #code for prediction
    hepatitis_diagnosis=''
     
    #creating button for prediction
    if st.button('Hepatitis-C cancer result'):
         hepatitis_prediction=hepatitis_model.predict([[Age,ALB,ALP,ALT,AST,BIL,CHE,CHOL,CREA,GGT,PROT,EnzymeRatio]]) 
         
         if(hepatitis_prediction[0]=='Blood Donor'):
             hepatitis_diagnosis_diagnosis='The patient was found to be healthy'
             
         if(hepatitis_prediction[0]=='Cirrhosis'):
             hepatitis_diagnosis_diagnosis='The patient has cirrhosis'
             
         if(hepatitis_prediction[0]=='Fibrosis'):
             hepatitis_diagnosis_diagnosis='The patient has fibrosis'
         
         if(hepatitis_prediction[0]=='Hepatitis'):
             hepatitis_diagnosis_diagnosis='The patient has hepatitis-c'
                 
         else:
             hepatitis_diagnosis='The patient was suspected to have hepatitis-c during blood donation'
             
             
    st.success(hepatitis_diagnosis)      
      
           