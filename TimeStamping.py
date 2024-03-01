from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes
import datetime

# Generate RSA key pair for timestamping
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Function to create a timestamp

def create_timestamp():
    current_time = datetime.datetime.utcnow()
    timestamp = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    return timestamp

# Usage
timestamp = create_timestamp()
print("Generated Timestamp:", timestamp)

data = b"I am Going to be Time Stamped (Time Stamped)"
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa,padding
from cryptography.hazmat.primitives import hashes
import datetime

# Generate RSA key pair for timestamping
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Function to create a timestamp

def create_timestamp():
    current_time = datetime.datetime.utcnow()
    timestamp = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    return timestamp

# Usage
timestamp = create_timestamp()
print("Generated Timestamp:", timestamp)

data = b"I am Going to be Time Stamped (Time Stamped)"
data_str = data.decode('base64')  # Use the appropriate encoding if not utf-8

data_with_timestamp = data_str + timestamp

signature = private_key.sign(
    data_with_timestamp,
    padding.PKCS1v15(),
    hashes.SHA256()
)
print("Data with Timestamp:", data_with_timestamp)
print("Signature:", signature.hex())
print("Public Key:", public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8'))

signature = private_key.sign(
    data_with_timestamp,
    padding.PKCS1v15(),
    hashes.SHA256()
)
print("Data with Timestamp:", data_with_timestamp)
print("Signature:", signature.hex())
print("Public Key:", public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode('utf-8'))
