import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import io
df= pd.read_csv('Student_Mental_health.csv')
#J'ai renommé les noms de variables
df.rename(columns = {'Choose your gender':'gender','What is your course?':'course','Your current year of Study':'current year','What is your CGPA?':'CGPA','Do you have Depression?':'depression', 'Do you have Anxiety?':'anxiety','Do you have Panic attack?':'panic attack','Did you seek any specialist for a treatment?':'specialist for a treatment'}, inplace = True)
note_moyenne=[]
for i in df['CGPA']:
    i=i.split()
    moyenne=(float(i[0])+float(i[2]))/2
    note_moyenne.append(moyenne)
#df.insert(6,"note moyenne",1)
df['note moyenne']=note_moyenne


st.markdown("# suppression des valeurs aberrantes")
st.sidebar.markdown("# suppression des valeurs aberrantes")


sup_anxiety = st.checkbox("supression des valeurs aberrantes pour la variable Anxiety")
sup_depression =st.checkbox("supression des valeurs aberrantes pour la variable Depression")
sup_panic_attack=st.checkbox("supression des valeurs aberrantes pour la variable Panic attack")

if sup_depression:

    code=''' 
    new_df = df[ df['note moyenne'] > 2.5] 
    sb.catplot(x="note moyenne", y="depression", data = new_df, kind= "box", height=7)'''
    st.code(code, language='python')
    new_df = df[ df['note moyenne'] > 2.5] 
    fig=sb.catplot(x="note moyenne", y="depression", data = new_df, kind= "box", height=7)
    st.pyplot(fig)
    st.write(""" 
    absence de mediane => 50 % souffrent de depression et les autres 50% non

    50% ont des bonnes notes se situant entre 3.6 et 3.8 !

    """)
if sup_anxiety:
    code='''
    sb.catplot(x="note moyenne", y="anxiety", data = new_df, kind= "box", height=7)'''
    st.code(code, language='python')

    fig=sb.catplot(x="note moyenne", y="anxiety", data = new_df, kind= "box", height=7)
    st.pyplot(fig)

    st.write(""" 
    absence de mediane => 50 % souffrent d'anxiété et les autres 50% non

    50% ont des bonnes notes se situant entre 3.6 et 3.8 !

    """)
if sup_panic_attack:
    code='''sb.catplot(x="note moyenne", y="panic attack", data = new_df, kind= "box", height=7)'''
    st.code(code, language='python')

    fig=sb.catplot(x="note moyenne", y="panic attack", data = new_df, kind= "box", height=7)
    st.pyplot(fig)

    st.write(""" 
    absence de mediane => 50 % souffrent de crise de panique et les autres 50% non

    50% ont des bonnes notes se situant entre 3.6 et 3.8 !

    J'ai converti mes variables quantitatives en variables qualitatives

    """)
