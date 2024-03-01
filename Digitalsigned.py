from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
import hashlib

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(message, private_key):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def compare_hash(document, expected_hash):
    # Generate a hash of the document
    document_hash = hashlib.sha256(document).hexdigest()

    # Compare the generated hash with the expected hash
    if document_hash == expected_hash:
        return True
    else:
        return False


private_key, public_key = generate_rsa_key_pair()
message = b"This is the message to be signed."
signature = sign_message(message, private_key)
print("Digital Signature:", signature.hex())
document = message
expected_hash = signature


if compare_hash(document, expected_hash):
    print("This documents is not Changed after it was Digital signed ")
else:
    print("You can trust totally This document is changed since it was Digital signed ")
