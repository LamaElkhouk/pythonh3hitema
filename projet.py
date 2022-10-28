# import modules
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import io


st.markdown("# Project")
st.sidebar.markdown("# project")

st.write("Mon projet consiste à étudier un jeu de données présentant des individus, des étudiants pour étudier et analyser leur santé mental et je souhaite savoir si il y'a un lien entre les differents resultats de ses étudiants et leurs note moyenne !Si oui, serait-il possible d'identifier quels sont le/le(s) groupe(s) d'étudiant(s) le(s) plus toucher par cette influence")
df= pd.read_csv('Student_Mental_health.csv')
code = '''
# import modules
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import io

df= pd.read_csv('Student_Mental_health.csv')

 '''
st.code(code, language='python')

# number of rows
rows = len(df.axes[0])
# number of columns
cols = len(df.axes[1])


st.write("Number of Rows: ", rows)
st.write("Number of Columns: ", cols)

value = st.slider(
    'Selectionnez le nombre de lignes du df à afficher',
    2.0, 101.0)
st.write('Values:', value)
st.write(df.head(int(value)))


st.write("Les données (variables) constituant mon dataframe")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

code='''
df= pd.read_csv('Student_Mental_health.csv')
# number of rows
rows = len(df.axes[0])
# number of columns
cols = len(df.axes[1])


st.write("Number of Rows: ", rows)
st.write("Number of Columns: ", cols)
st.write(df)


st.write("Les données (variables) constituant mon dataframe")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)'''
st.code(code, language='python')

st.write("""
On étudie un échantillon de 101 étudiants ayant 11 caractéristiques:

=> personnelles :

age, domaine d'études, son année d'étude, sa moyenne globale (CGPA = A=4 B=3 C=2 D=1 et F=0) et son état civil.

=> En rapport avec leur santé mentale:

Est ce qu'ils sont en dépression? ressent-ils de l'anxiété ? ont-ils déja eu une crise de panique? ont-ils consulté un spécialiste pour un traitement?

=> Il y'a également la toute premiere caractéristique "timestamp",qui selon n'est pas une variable pertinente pour l'étude, elle représente la date et heure à laquel chaque étudiant à été interroger.

Le dataframe est constitué principalement de variables qualitatives de type Object (string) et d'une variable quantitative "l'age", qui est de type float.
""")

st.write("Dataframe en version plus simplifier")


code ='''
#J'ai renommé les noms de variables
df.rename(columns = {'Choose your gender':'gender','What is your course?':'course','Your current year of Study':'current year','What is your CGPA?':'CGPA','Do you have Depression?':'depression', 'Do you have Anxiety?':'anxiety','Do you have Panic attack?':'panic attack','Did you seek any specialist for a treatment?':'specialist for a treatment'}, inplace = True)

note_moyenne=[]

for i in df['CGPA']:
    i=i.split()
    moyenne=(float(i[0])+float(i[2]))/2
    note_moyenne.append(moyenne)



#df.insert(6,"note moyenne",1)

df['note moyenne']=note_moyenne

df.head(5)


#sb.catplot(x="note_moyenne", y="depression", data = df, kind= "box", height=7)

'''
st.code(code, language='python')


#J'ai renommé les noms de variables
df.rename(columns = {'Choose your gender':'gender','What is your course?':'course','Your current year of Study':'current year','What is your CGPA?':'CGPA','Do you have Depression?':'depression', 'Do you have Anxiety?':'anxiety','Do you have Panic attack?':'panic attack','Did you seek any specialist for a treatment?':'specialist for a treatment'}, inplace = True)



note_moyenne=[]

for i in df['CGPA']:
    i=i.split()
    moyenne=(float(i[0])+float(i[2]))/2
    note_moyenne.append(moyenne)



#df.insert(6,"note moyenne",1)

df['note moyenne']=note_moyenne
st.write(df.head(5))
#sb.catplot(x="note_moyenne", y="depression", data = df, kind= "box", height=7)

st.write("Peut-on décrire la note moyenne par rapport à depression ? panic attack et anxiety?")

code=''' df['note moyenne'].describe() '''
st.code(code, language='python')
st.write(df['note moyenne'].describe())


st.write("""
la moyenne des notes est de 3.35

l'écart-type : 0.58

donc les notes vont de 2.77 à 3.93 qui sont plutot de bonne notes!

max => 3.75 == 100% 0.58 represente 15.46% de 3.75% qui est plutot faible mais on ne peut pas vraiment conclure qu'elle soit significative

Correlation entre la variable qui décrit la note_moyenne de chaque étudiant avec la variable chacune des variables qui décrit si oui ou non il est anxieux, anxiety, si oui ou non il est en depression et si oui ou non il a des crises de panique, panic attack

 """)



code=''' 
#J'ai remplacé les 'yes' et 'No' par 1 et 0
df['depression']= df['depression'].replace(['Yes','No'],[1,0])
df['anxiety']= df['anxiety'].replace(['Yes','No'],[1,0])
df['panic attack']= df['panic attack'].replace(['Yes','No'],[1,0])
df['specialist for a treatment']= df['specialist for a treatment'].replace(['Yes','No'],[1,0])
df['Marital status']= df['Marital status'].replace(['Yes','No'],[1,0])
'''
st.code(code, language='python')


