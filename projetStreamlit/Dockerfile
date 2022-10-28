FROM python:3.10

#RUN apt-get update
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8501
		  		 
CMD ["streamlit","run","projet.py"]