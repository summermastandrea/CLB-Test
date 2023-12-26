# CLB-Test
Requirements: Assumes python and pip are previously installed, install the other resources below. These installation commands are for ubuntu, google the respective commands for your OS.

flask = pip install Flask

flask-cors = pip install flask-cors

xmltodict = pip install xmltodict

A google cloud platform account will also be required in order to generate an API key for the google maps API used in this project. 

Steps for Part 1 & 2: steps are for Ubuntu, google alternative commands for other OSs
1. Download the Code Test folder. 
2. Install all required dependencies.
3. For the Google Maps API to work. You will need to create your API Key via the Google Cloud platform. Once done, this key can be copied and inserted into the front-end.html file at line 7 where the URL says [Your API KEY]. Save this change and the file will be ready to be loaded locally. 
4. Open the Code Test folder in the command line. 
5. Run "python3 dataStream.py" to start the application
6. Go to http://127.0.0.1:5000/parcel_data?parcel=[INSERT PARCEL NUMBER HERE]. The parcel number inserted should be the parcel number whose information you'd like to view. Now you can view the JSON formatted data provided by the XML file. 
7. Now go to your browser and go to "http://127.0.0.1:5000/". This loads the HTML in the browser and will display a blank page that only asks the user to insert what parcel number they would like to view.
8. Once the parcel number is inserted and the button is clicked the data will be displayed on the html. To try other parcels, go to the top of the page and enter a new parcel number.  

Steps for Part 3: steps are for Windows, SQL should be previously installed and the root user should be logged in
1. Go to the command line and type "mysql -u root -p". You will be prompted for a password and then click enter. Once logged in, the SQL command line will appear. 
2. Now create a database using "CREATE DATABASE [insert database name here];", click enter. Now the database was crreated, but before loading the sql_test.sql file, you but use the command "USE [insert database name here];". 
3. Now copy your file path for the sql_test.sql file and use the command "source [insert file path here]" then enter. Make sure the file path is using forward slashes and not back slashes. This will load the contents of the dump into the new database. 
4. Now copy the queries from the sql_test_queries.txt file and paste them one by one into the command line. Run each independently and view the results. These results should be the same as the results mentioned in the file as well. 
