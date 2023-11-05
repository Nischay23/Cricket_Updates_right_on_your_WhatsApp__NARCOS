import requests
import json
import os
from twilio.rest import Client
class ScoreGet:
    def __init__(self):
        self.user_input1 = input("please enter the team 1  ")  # Display a prompt to the user
        self.user_input1.lower()
        self.user_input1=self.user_input1.capitalize()
        self.user_input2 = input("please enter the team 2  ")
        self.user_input2.lower()
        self.user_input2 =self.user_input2.capitalize()

        """
        Declaring the endpoints, apikey
        """
        self.url_get_all_matches = "https://api.cricapi.com/v1/currentMatches"
        self.api_key = "6a9d499a-dc31-4acd-b59f-a0b287092ef7"
        self.unique_id = ""  # unique to every match

    def get_unique_id(self):
        """
        Returns Indian cricket teams match id, if the match is Live
        :return:
        """
        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found=0
        my_dict={}
        for i in resp_dict['data']:
            if (self.user_input1 in i['teams'] and self.user_input2 in i['teams'] ):
                uid_found=1
                self.unique_id=i['id']
                my_dict={
                    "name ":i['name'],
                    "match type ":i['matchType'],
                    "status ":i['status'],
                    "venue ":i['venue'],
                    "date ":i['date'],
                    "dateTimeGMT ":  i['dateTimeGMT'],
                    "teams ":i['teams'],
                    "score ": i['score'],
                    "matchStarted ":i['matchStarted'],
                    "matchEnded ":i['matchEnded']
                }
                return(my_dict)      
        if (uid_found==0):
            return('match not found')

if __name__=="__main__":
    obj_score=ScoreGet()
    abc=obj_score.get_unique_id()
    json_string = json.dumps(abc, indent=4)
    from twilio.rest import Client

    account_sid = 'AC849f0585431f11041e285f8aef24bbae'
    auth_token = 'a7f64907dd61688d62e9a4faa7fb35de'
    client = Client(account_sid, auth_token)
    
    conversation = client.conversations \
                     .v1 \
                     .conversations \
                     .create(friendly_name='how r u')

    print(conversation.sid)

    message = client.messages.create(
      from_='whatsapp:+14155238886',
      body=json_string,
      to='whatsapp:+919309578754'
    )

    print(message.sid)


   



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure







