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

SUBSCRIPTION_KEY = "a73bb5f29795e3e452e2"

service_address = "https://free.currconv.com"
address = service_address + "/api/v7/convert?q=USD_PHP,PHP_USD&compact=ultra&apiKey=" + SUBSCRIPTION_KEY
print()
r = requests.get(url=address, verify=False)

txt = r.text

outdict = eval(txt.replace("\"", "\'"))

print(txt)
print(outdict['USD_PHP'])
#print(dict(r.text))
print()