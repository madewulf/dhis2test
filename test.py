from dhis2 import Api
import csv

credentials = {
     "url":"https://dhis2.somewhere.org",
     "login":"", 
     "password":""
}

api = Api(credentials["url"], credentials["login"], credentials["password"])

#posting the data

response = api.post("dataValueSets",{'dataValues': [{'value': 12, 'period': '2020Q4', 'comment': '32969 12 CS_QUALITE_RDC_11_total_max', 'orgUnit': 'xRqMkXZpsLE', 'dataElement': 'UQo71m7kpHe', 'categoryOptionCombo': 'Mm0YLGTPdv8'}, {'value': 9.25, 'period': '2020Q4', 'comment': '32969 9.25 CS_QUALITE_RDC_11_total_point', 'orgUnit': 'xRqMkXZpsLE', 'dataElement': 'Dw9e3MkQjck', 'categoryOptionCombo': 'Mm0YLGTPdv8'}]})

print(response.text)

#MARK DATASET AS COMPLETE
response2 = api.post("completeDataSetRegistrations", {'completeDataSetRegistrations': [{'date': '2021-03-16', 'period': '2020Q4', 'dataSet': 'oxGKjhgTsLq', 'organisationUnit': 'xRqMkXZpsLE'}]})

print(response2.text)
