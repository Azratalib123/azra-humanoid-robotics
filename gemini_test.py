import os
from google import genai

# Apni nayee key ko seedhe yahan daal kar dekhein:
NAYEE_API_KEY = " AIzaSyC__wG0Ten-MOF0iixBQbeeYyjis4m9Ufw  " # <-- DOUBLE-CHECK ki yeh key fresh aur nayi hai

# Client ko is nayi key ke saath initialize karein
client = genai.Client(api_key=NAYEE_API_KEY) # <--- Ab yeh line sirf NAYEE_API_KEY use karegi!

# ... rest of the code ...