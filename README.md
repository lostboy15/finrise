# finrise
This is repo for FINRISE assignment solution

## Real-Time Feed Subscription System

## Project Setup

'''
git clone
pip install -r requirements.txt
run redis server #port 6379
python manage.py runserver
python manage.py tasks #To run external websocket
'''

### API URLS

### 1. Register
'''
http://127.0.0.1:8000/feed/user/register
'''
Request
'''
{"username" : "" , password : ""}
'''
Response
'''
{"access_token" : ""}
'''

### 2. Login
'''
http://127.0.0.1:8000/feed/user/login
'''
Request
'''
{"username" : "", "password" : ""}
'''
Response
'''
{"refresh" : "", "access" : ""}
'''

### live feed stream
'''
ws://127.0.0.1:8000/live-data/subscribe
'''
Headers
'''
{"authorization" : "API Bearer Token"}
'''
Response
'''
{"message" : "{"stream" : "btcusd_perp@bookTicker","data":{}}"}
'''
