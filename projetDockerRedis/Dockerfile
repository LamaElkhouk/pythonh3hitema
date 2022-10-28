FROM php:8.1.2
#RUN apt-get update
WORKDIR /app
COPY . .
RUN apt-get update

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

EXPOSE 8080
		  		 
CMD ["php", "compteur.php"]