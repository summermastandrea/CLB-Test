from flask import Flask, jsonify
import xmltodict
import requests
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#flask provides this this endpoint
#access json response http://127.0.0.1:5000/convert_xml_to_json?parcel=INSERT PARCEL NUMBER HERE
@app.route('/convert_xml_to_json', methods=['GET'])
def convert_xml_to_json():
    try:
        #grabs link provided to command-line when running script
        xml_link = sys.argv[1]
        response = requests.get(xml_link)
        
        # Finds the start of XML content since most xml documents used <?xml
        xml_start = response.text.find('<')

        # Parse XML to python dictionary which represents the XML structure
        json_data = xmltodict.parse(response.text[xml_start:])

        #flasks jsonify used to conver python dictionary to json response, return responses to client
        return jsonify(json_data)
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    #runs flask application
    app.run()

