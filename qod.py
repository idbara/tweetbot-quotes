import requests
headers = {
  'Content-Type': 'application/json'
}

def getQuote():
    response = requests.get('http://quotes.rest/qod?category=love', headers=headers)
    json_response = response.json()
    # print(json_response)
    # quote = json_response['contents']['quotes'][0]['quote']
    # author = json_response['contents']['quotes'][0]['author']
    # print(quote+" - "+author)
    result = json_response['contents']['quotes'][0]['quote']+" - "+json_response['contents']['quotes'][0]['author']
    return result