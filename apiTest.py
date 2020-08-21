# You can call a function stored in a webservice
# For that request lib is used 
#   # Check documentation for the acceptable values
#   requests.post(address,
#                 http_headers,
#                 function_parameters,
#                 message_body)

# use the requests lib to simplify making a REST API call from python
import requests

# jason used to read the data passed back by the web service
import json

# Web service peronal key (from my email) 
from dotenv import load
load()
import os
key = os.getenv('SUBSCRIPTION_KEY')

# Get input from the user
print()
convert_from = input('Convert from currency? ').upper()
convert_to = input('Convert to currency? ').upper()
amount = input('Enter amount in ' + convert_from + ': ')

# Build te web service url 
# Example: https://free.currconv.com/api/v7/convert?q=EUR_EGP&compact=ultra&apiKey=<KEY>
service_address = "https://free.currconv.com"
address = service_address + "/api/v7/convert?q="+ convert_from + "_" + convert_to + "&compact=ultra&apiKey=" + key

print()

# Call the API and save the response
response = requests.get(url=address)

# Raise eny errors happend during the HTTP call 
response.raise_for_status()

# Format the response as json (basically organized in ciollection 'a dictionary')
data = response.json()

# Convert the entered amunt to the desired currency rounded in hunderedth
converted_amount = float(amount) * (round(100 * data[convert_from + "_" + convert_to]) / 100)

# Output to the user
print(amount + ' ' + convert_from +  ' = ' + str(converted_amount) + ' ' + convert_to)

print()