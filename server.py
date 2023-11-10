from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding
from cryptography.hazmat.primitives.hashes import SHA256
import qrcode
from io import BytesIO

from flask import Flask, request, send_file

app = Flask(__name__)

qr_data = b''

f = open('./pubkey', 'rb')
data = f.read()
f.close()

public_key = ed25519.Ed25519PublicKey.from_public_bytes(data)


@app.route('/set_qr', methods=['POST'])
def set_qr():
    global qr_data
    global public_key
    
    data = request.json
    qr = bytes.fromhex(data.get('qr'))
    signature = bytes.fromhex(data.get('signature'))
    public_key.verify(signature, qr)

    qr_data = qr
    return "OK"

@app.route('/get_qr', methods=['GET'])
def get_qr():
    qr = qrcode.QRCode(version=7, box_size=10, border=0)
    qr.add_data(qr_data.decode('utf-8'))
    qr.make()
    img = qr.make_image()
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png', download_name='qr_code.png')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)