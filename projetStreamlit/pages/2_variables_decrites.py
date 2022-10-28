
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


st.markdown("# variables décrites par rapport a la moyenne des notes")
st.sidebar.markdown("# variables décrites par rapport a la moyenne des notes")


anxiety = st.checkbox("Anxiety")
depression =st.checkbox("Depression")
panic_attack=st.checkbox("Panic attack")

if anxiety:
   
    code=''' 
    #sb.catplot(y="note moyenne", x="anxiety", data= df, kind="bar", height=5, aspect=1)
    sb.catplot(y="anxiety", x="note moyenne", data = df, kind= "box", height=4)'''
    st.code(code, language='python')

    #sb.catplot(y="note moyenne", x="anxiety", data= df, kind="bar", height=5, aspect=1)
    fig=sb.catplot(y="anxiety", x="note moyenne", data = df, kind= "box", height=4)
    st.pyplot(fig)
    st.write("on a deux valeurs aberrantes => il existe des individus ne souffrant d'anxiété et n'ayant pas de bonnes notes")
if depression:
    code=''' 

    sb.catplot(y="depression", x="note moyenne", data = df, kind= "box", height=7)'''
    st.code(code, language='python')
    fig=sb.catplot(y="depression", x="note moyenne", data = df, kind= "box", height=7)
    st.pyplot(fig)
    st.write("on a deux valeurs aberrantes => deux individus ayant une note inferieur a 2.5 et ne souffre pas d'anxiété ...")
if panic_attack:
    code=''' 
    sb.catplot(y="panic attack", x="note moyenne", data = df, kind= "box", height=7)'''
    st.code(code, language='python')

    fig=sb.catplot(y="panic attack", x="note moyenne", data = df, kind= "box", height=7)
    st.pyplot(fig)
    st.write("quatres valeurs aberrantes => il existe des étudiants ayant des notes inferieur a 2.5 , certain d'entre eux souffre de crise de panic d'autres non")
