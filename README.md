# MicroserviceA
# Motivational Quotes Microservice

## Communication Contract

### Requesting Data
To request a random quote:
import requests

response = requests.get("http://127.0.0.1:5101/quote")
print(response.json())

-------------------------------------------------------

To request a quote by category:
import requests

response = requests.get("http://127.0.0.1:5101/quote/confidence")
print(response.json())

-------------------------------------------------------

Receiving Data
The response will be a JSON object containing the quote and author:
{
    "q": "Believe in yourself and all that you are.",
    "a": "Christian D. Larson"
}

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

<img width="477" alt="image" src="https://github.com/user-attachments/assets/28a1f7a9-dd18-4058-a326-539159aef7b9" />


