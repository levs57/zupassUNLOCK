from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519, padding
from cryptography.hazmat.primitives.hashes import SHA256

privkey = ed25519.Ed25519PrivateKey.generate()
pubkey = privkey.public_key()
privkey_data = privkey.private_bytes_raw()
pubkey_data = pubkey.public_bytes_raw()

f = open('./privkey', 'wb')
f.write(privkey_data)
f.close()

f = open('./pubkey', 'wb')
f.write(pubkey_data)
f.close()
