'''https://api-ninjas.com/profile'''
'''DATE CREATED 6 SEPT 2024 - TESTED ON VSCODE'''

import time
from plyer import notification
import requests
import random

def getFact(data):

    api_url_facts = 'https://api.api-ninjas.com/v1/'+data+'s?'
    
    response = requests.get(api_url_facts, headers={'X-Api-Key': 'tW/0ZrhGUfy68npIggfjHA==OgnYI6awvCrr74eG'})
    
    if response.status_code == requests.codes.ok:
        return response.json()[0].get(data)
    else:
        return "API call failed"

while True:
    data = random.choice(["fact","joke"])
    message = getFact(data)
    notification.notify(
        title="Here's your "+data+" !",
        message=message,
        app_icon = None,
        timeout = 15
    )
    print(message)
    time.sleep(30)
