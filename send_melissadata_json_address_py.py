###Date: March 26, 2019

###this Python program sends addresses to MelissaData (a paid service) to get latitude and longitude information

###a MelissaData account is needed to use MelissaData

###took guidance from
###https://stackoverflow.com/questions/37062868/call-a-list-variable-from-a-for-loop-in-python

###how to run Python syntax files
###use windows command window
###goto (the folder where your syntax file is)
###type into windows command window (location of your Python)\python.exe (the name of this Python syntax file)

###import the needed packages
import requests
import json


###additional information about MelissaData

###from 
###http://wiki.melissadata.com/index.php?title=Personator%3AJSON

###their online devconsole is at
###http://devconsole.melissadata.com/personator/



###their header
###Content-Type: application/json; charset=utf-8
###Accept: application/json
###Host: personator.melissadata.net
###Expect: 100-continue
###Connection: Keep-Alive

url="https://personator.melissadata.net/v3/WEB/ContactVerify/doContactVerify"

headers= {'Content-Type': 'application/json', 'Accept': 'application/json',
'Expect': '100-continue', 'Connection': 'Keep-Alive'}

###the list of addresses to check
###can choose the recordID, so that you can identity the record when it returns from MelissaData
address_list=[	

{"RecordID":"(an identifier that you choose yourself)","AddressLine1":"123 Main St","City":"Anytown","State":"PA","PostalCode":"12345"}, 
{"RecordID":"Citi Field","AddressLine1":"120–01 Roosevelt Avenue","City":"Flushing","State":"NY","PostalCode":"11368"}, 
{"RecordID":"United Center","AddressLine1":"1901 West Madison St","City":"Chicago","State":"IL","PostalCode":"60612"}, 
{"RecordID":"Prudential Center","AddressLine1":"25 Lafayette St","City":"Newark","State":"NJ","PostalCode":"07102"}, 
{"RecordID":"Fort Worth Convention Center","AddressLine1":"	12 Houston St","City":"Fort Worth","State":"TX","PostalCode":"76102-6432"}, 
{"RecordID":"Oracle Arena","AddressLine1":"7000 Coliseum Way","City":"Oakland","State":"CA","PostalCode":"94621"}, 
{"RecordID":"Staples Center","AddressLine1":"1111 South Figueroa St","City":"Los Angeles","State":"CA","PostalCode":"90015"}, 
{"RecordID":"Troubadour","AddressLine1":"9081 Santa Monica Blvd","City":"West Hollywood","State":"CA","PostalCode":"90069"}]

###put the information about this batch of addresses
###into a log file of your choosing
###can give a name to this batch of addresses (the TransmissionReference) to be able to identify this batch of addresses
for i in range(len(address_list)):
    #print (my_list[i])
	
	reqdata1={
  "TransmissionReference":"(title that you want to give to this batch of addresses)",
  "Actions":"Check",
  "Columns":"PostalCode, GrpGeocode",
  "CustomerID":"(insert your CustomerID here)",
  "Records":[  address_list[i]	]
}

	reqsent = requests.post(url, data=json.dumps(reqdata1), headers=headers)

	###append into log f
	with open('(location of where to put the log file)/logname_log.txt', 'a') as f:
		print('', reqsent.text, file=f)
 
	