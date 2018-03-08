# -*- coding: utf-8 -*-
import json
import fitbit
import gather_keys_oauth2 as Oauth2
from os import path

# Globals
AUTH_TOKEN_FILENAME = "auth_token.json"
CREDENTIALS_FILENAME = "creds.json"
# /Globals

def create_credsfile(id,secret):
    login = {   
            "client_id": id, 
            "client_secret": secret, 
            "callback_url":"http://127.0.0.1:8080/"
        }

    with open(CREDENTIALS_FILENAME,'w') as f:
        json.dump(login,f)
    
    return login
        
'''
# Code to manually create an auth_token.json file
auth = {   
    'token_type' : 'Bearer',
    'user_id' : '',
    'scope' : ['heartrate', 'nutrition', 'profile', 'sleep', 'activity', 'weight', 'social', 'settings', 'location'],
    'refresh_token' : '',
    'expires_in' : 28800,
    'expires_at' : 1500000000.0000001,
    'access_token' : ''
}
with open(AUTH_TOKEN_FILENAME,'w') as f:
    json.dump(auth,f)
'''

def authorize_application(_creds):
    print("   NOTE: CherryPy spins up a webserver on localhost so that you can auth \n")
    print("   If you are on Ubuntu Server, use a commandline browser:")
    print("     sudo apt-get install elinks \n")
    print("   Then, when running this python program, elinks will auto open.")
    print("   NOTE: press enter and q to exit elinks after completed (when you see: 'ENGINE Waiting for child threads')\n")
    # redirect_uri is required if you have more than one callback_url registered in your FitbitApp
    # otherwise it can be removed.
    # however, in order to use the gather_keys_oauth2 cherrypy example, it requires http://127.0.0.1:8080/ set in your app
    server = Oauth2.OAuth2Server(_creds['client_id'],_creds['client_secret'],redirect_uri=_creds['callback_url'])
    server.browser_authorize()
    token_saver(server.fitbit.client.session.token)

def token_saver(_token_dict):
    print(" Called token_saver (Created new token or Refreshed expired, saving to json now)")
    with open(AUTH_TOKEN_FILENAME,'w') as f:
        json.dump(_token_dict,f)

def get_client(login,auth):
    return fitbit.Fitbit(
    login['client_id'],
    login['client_secret'],
    access_token=auth['access_token'], 
    refresh_token=auth['refresh_token'],
    redirect_uri=login['callback_url'],
    expires_at=auth['expires_at'],
    expires_in=auth['expires_in'],
    refresh_cb=token_saver
    )
    
def load_client():
    with open(CREDENTIALS_FILENAME,'r') as f:
        login = json.load(f)
    with open(AUTH_TOKEN_FILENAME,'r') as f:
        auth = json.load(f)
    return get_client(login,auth)
    
def run():    
    # If first time running app, need to authorize it. Create a credentials file first.
    # Or, if auth token file does not exist, create a new one
    
    if (path.exists(AUTH_TOKEN_FILENAME)) is not True:
        try:
            with open(CREDENTIALS_FILENAME,'r') as f:
                login = json.load(f)
                
        except FileNotFoundError:
            login = create_credsfile('<your id>','<your secret>')
            
        authorize_application(login)
    
    with open(AUTH_TOKEN_FILENAME,'r') as f:
        auth = json.load(f)
    
    # Login and Auth files created, see if you can access your fitbit data
    # by creating a client and testing with Get_Devices
    fbclient = get_client(login,auth)
    
    # Get_Devices requires an authenticated session
    fbgd = fbclient.get_devices() 
    print(fbgd)

if __name__ == '__main__':
    run()
    
