from dotenv import load
load()
import os

password = os.getenv('SUBSCRIPTION_KEY')
print(password)