import requests
#utilizado para criar um email no site https://ethereal.email/
#'user': 'o7q3sv4ubxg23kzk@ethereal.email', 'pass': 'qxQyXcGaV9SVU1Uwtf'

payload = {
    "requestor": "YoutNameOfAppName",
    "version": "1.0"
}

response = requests.post('https://api.nodemailer.com/user', json=payload)
if response.status_code ==200:
    account = response.json()
    print(account)
else:
    raise Exception(f'Could not create Ethereal account: {response.text}')
