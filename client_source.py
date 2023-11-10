import requests
import time
from PIL import ImageGrab
from pyzbar.pyzbar import decode

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding
from cryptography.hazmat.primitives.hashes import SHA256

import re

regex = re.compile(
        r'^https://[0-9a-z_.:/]*', re.IGNORECASE)


server_url = 'https://levs57.pythonanywhere.com/set_qr'

is_url_valid = re.match(regex, server_url) is not None;

if not is_url_valid:
    print("Please use https.")
#    exit()

f = open('./privkey', 'rb')
data = f.read()
f.close()

private_key = ed25519.Ed25519PrivateKey.from_private_bytes(data)

while True:
    try:
        screenshot = ImageGrab.grab()
        qr_codes = decode(screenshot)
        if True: #len(qr_codes) == 1:
            qr = qr_codes[0]
            signature = private_key.sign(qr.data)
            data = {'qr' : qr.data.hex(), 'signature' : signature.hex()}
            response = requests.post(server_url, json=data)
            print(response)
    except:
        pass
    time.sleep(5)
