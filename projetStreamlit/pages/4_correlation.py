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

st.markdown("# y'a t-il correlation entre les notes et les  variables depression, anxiety et panic attack?")
st.sidebar.markdown("# correlation entre chacune des varibles avec la note moyenne")


cor_anxiety = st.checkbox("correlation avec Anxiety")
cor_depression =st.checkbox("correlation avec Depression")
cor_panic_attack=st.checkbox("correlation avec Panic attack")
if cor_anxiety:
    code='''
    sb.catplot(x="note moyenne", y="anxiety", data= df, kind="bar", height=10)
    '''
    st.code(code, language='python')

    fig=sb.catplot(x="note moyenne", y="anxiety", data= df, kind="bar", height=10)
    st.pyplot(fig)

    st.write(""" 
    36 % ont des notes se situant aux alentours de 3.75

    les ecarts-types sont énormes donc les deux variables ne sont pas correler

    plus un étudiant à de bonnes notes, plus il souffre anxiété

    """)
if cor_depression:
    code=''' sb.catplot(x="note moyenne", y="depression", data= df, kind="bar", height=10)'''
    st.code(code, language='python')

    fig=sb.catplot(x="note moyenne", y="depression", data= df, kind="bar", height=10)
    st.pyplot(fig)

    st.write("""
    30 % ont des notes se situant aux alentours de 3.75

    les ecarts-types sont énormes donc les deux variables ne sont pas correler

    plus un étudiant à de bonnes notes, plus il souffre de depression

    """)

if cor_panic_attack:
    code=''' sb.catplot(x="note moyenne", y="panic attack", data= df, kind="bar", height=10)'''
    st.code(code, language='python')

    fig=sb.catplot(x="note moyenne", y="panic attack", data= df, kind="bar", height=10)
    st.pyplot(fig)

    st.write(""" 
    40 % ont des notes se situant aux alentours de 3.75

    les ecarts-types sont énormes donc les deux variables ne sont pas correler

    qu'ils aient de bonne notes ou pas , il y'a des etudiant qui souffre crise de panique

    """)

