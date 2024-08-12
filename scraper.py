import requests 
import json 
import pandas as pd

def postRequest(url, data, tokenAuth):

    headers = {
        'Authorization': token,
        # Any other header construction needed
        'tokenTarget': tokenAuth
    }

    response = requests.post(url, json = data, headers = headers) # POST request for the target API with Auth tokens if needed

    if response.status_code == 200:
        return response.json() #Saves response in a JSON file
    else:
        return None
    

apiUrl = ' ' # Where do you want to pull things from

token = ''
tokenOAuth2 = ''
# Any autorization tokens you might need 

outputFile = 'info.json'

for i in range(): # Dealing with pagination formats
    postData = {
        'pageNumber': i+1,
        'orderBy': '',
        # Any other necessary filters
    }

    responseJson = postRequest(apiUrl, postData, tokenOAuth2)

    if responseJson:
        # Update output file
        with open(outputFile, 'a') as file:
            json.dump(responseJson, file)
            file.write('\n') # New line to prevent cluttering

table = pd.read_json('info.json') # From here we can use any other functions to check and filter the file as needed