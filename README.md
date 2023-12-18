# CLB-Test
Requirements: Assumes python and pip are previously installed, install the other resources below. These installation commands are for ubuntu, google the respective commands for your OS.

flask = pip install Flask
flask-cors = pip install flask-cors
xmltodict = pip install xmltodict


Steps for Part 1 & 2: steps are for Ubuntu, google alternative commands for other OSs
1. Download the Code Test folder. 
2. Install all required dependencies.
3. Open the Code Test folder in the command line. 
4. Run "python3 dataStream.py <url link>" for the URL link you want to test
5. Go to http://127.0.0.1:5000/convert_xml_to_json?parcel=[INSERT PARCEL NUMBER HERE]. The parcel number inserted should be the same as defined in the URL. Now you can view the JSON formatted data provided by the XML stream. The script is now running locally. 
6. Now the front-end.html file can be opened in the browser. By opening this document, Javascript and jQuery are used to fetch and load the data into the HTML. This may take a few seconds. 
7. Now the data will be displayed on the html. To try other links. Go to the terminal and use Control C to close the server. Now re-run it using the step 4 command, but change the url. Now re-fresh the HTML and the data updated for the parcel number in the new URL. 

Steps for Part 3: steps are for windows, SQL should be previously installed and root user should be logged in
1. Go to the command line and type "mysql -u root -p". You will be prompted for a password and then click enter. Once logged in, the SQL command line will appear. 
2. Now create a database using "CREATE DATABASE [insert database name here];", click enter. Now the database was crreated, but before loading the sql_test.sql file, you but use the command "USE [insert database name here];". 
3. Now copy your file path for the sql_test.sql file and use the command "source [insert file path here]" then enter. Make sure the file path is using forward slashes and not back slashes. This will load the contents of the dump into the new database. 
4. Now copy the queries from the sql_test_queries.txt file and paste them one by one into the command line. Run each independently and view the results. These results should be the same as the results mentioned in the file as well. 
