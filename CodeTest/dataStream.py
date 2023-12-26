from flask import Flask, jsonify, request, render_template
import xmltodict
import requests
import sys
from flask_cors import CORS


#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)
CORS(app)


@app.route('/')
def front_end():
    return render_template('front-end.html')
#flask provides this this endpoint

@app.route('/parcel_data', methods=['POST', 'GET'])
def parcel_data():
    try:
        #post handles addressing the parcel number parameter to pull the right data to the html
        #access HTML at http://127.0.0.1:5000
        if request.method=='POST':
            #gets parcel number from form
            parcel_No = request.form['parcelNo']
            
            #grabs link provided to command-line when running script
            xml_link = f'http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel={parcel_No}'
            response = requests.get(xml_link)

             # Finds the start of XML content since most xml documents used <?xml
            xml_start = response.text.find('<')

            # Parse XML to python dictionary which represents the XML structure
            json_data = xmltodict.parse(response.text[xml_start:])

            #flasks jsonify used to convert python dictionary to json response, return responses to client
            return jsonify(json_data)

        #get handles displaying of data from links provided on github
        #access json response http://127.0.0.1:5000/parcel_data?parcel=[INSERT PARCEL NUMBER HERE]
        elif request.method =='GET':
            #gets the parcel number provided to the URL via the web browser
            parcel_No = request.args.get('parcel')

             #grabs link provided to command-line when running script
            xml_link = f'http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel={parcel_No}'
            response = requests.get(xml_link)

            # Parse XML to python dictionary which represents the XML structure
            xml_start = response.text.find('<')
            json_data = xmltodict.parse(response.text[xml_start:])

            #flasks jsonify used to convert python dictionary to json response, return responses to client
            return jsonify(json_data)
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    #runs flask application
    app.run()

