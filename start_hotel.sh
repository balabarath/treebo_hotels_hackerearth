#!/bin/sh
PYTHON="python"
WEBAPP_PATH="treebo"
WEBAPP_PROJECT_NAME="hotel"


#pip install djangorestframework

if ! mysql -u root -e 'use hotel_db' > /dev/null 2>&1; then

	#database_initialization
    	mysql -u root -e 'create database hotel_db'
    	
    	$PYTHON ./$WEBAPP_PROJECT_NAME/manage.py makemigrations >> $SERVER_LOG 2>$SERVER_LOG
	   	$PYTHON ./$WEBAPP_PROJECT_NAME/manage.py migrate >> $SERVER_LOG 2>$SERVER_LOG
    	
    	mysql -u root -p 'hotel_db' < ./resources/hotel_deals.sql
fi
