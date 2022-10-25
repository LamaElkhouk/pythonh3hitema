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
st.markdown("#heatmap et matrice de correlation")
st.sidebar.markdown("# heatmap et matrice de correlation")


#J'ai remplacé les 'yes' et 'No' par 1 et 0
df['depression']= df['depression'].replace(['Yes','No'],[1,0])
df['anxiety']= df['anxiety'].replace(['Yes','No'],[1,0])
df['panic attack']= df['panic attack'].replace(['Yes','No'],[1,0])
df['specialist for a treatment']= df['specialist for a treatment'].replace(['Yes','No'],[1,0])
df['Marital status']= df['Marital status'].replace(['Yes','No'],[1,0])



code=''' 
matrice=df.corr()
matrice'''
st.code(code, language='python')

matrice=df.corr()
st.write(matrice)


code='''
plt.figure(figsize=(15,6))
sb.heatmap(matrice, annot=True)'''
st.code(code, language='python')

fig=plt.figure(figsize=(15,6))
sb.heatmap(matrice, annot=True)

st.write(fig)

st.write(""" 
il est vrai que la note n'a pas d'influence sur l'anxité, la depression et la crise de panique..mais de ce qu'on peut en conclure de notre heatmap ! la santé mentale est plus relier a sa vie sentimentale et non lié a ses études, les étudiants souffrent de dépression à cause de leur celiba... mais cela n'influe en aucun cas les notes..
""")