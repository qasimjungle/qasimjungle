from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import base64


def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key, private_key.public_key()

def save_private_key_to_pem(private_key, filename):
    with open(filename, "wb") as private_key_file:
        private_key_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def save_public_key_to_pem(public_key, filename):
    with open(filename, "wb") as public_key_file:
        public_key_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def load_private_key_from_pem(filename):
    with open(filename, "rb") as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def load_public_key_from_pem(filename):
    with open(filename, "rb") as public_key_file:
        public_key = serialization.load_pem_public_key(
            public_key_file.read(),
            backend=default_backend()
        )
    return public_key
import base64

def encrypt_and_store(data, public_key, output_file):
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Encode the encrypted data using Base64
    encrypted_data_base64 = base64.b64encode(encrypted_data)

    # Write the encoded data to the output file
    with open(output_file, "wb") as pem_file:
        pem_file.write(encrypted_data_base64)
def load_and_decrypt(encrypted_file, private_key):
    with open(encrypted_file, "rb") as pem_file:
        encrypted_data_base64 = pem_file.read()

    # Decode the Base64 encoded data
    encrypted_data = base64.b64decode(encrypted_data_base64)

    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_data


private_key, public_key = generate_rsa_key_pair()

private_key_file = "private_key.pem"
public_key_file = "public_key.pem"

save_private_key_to_pem(private_key, private_key_file)
save_public_key_to_pem(public_key, public_key_file)

print("Private key saved as:", private_key_file)
print("Public key saved as:", public_key_file)

private_key_filename = "private_key.pem"
public_key_filename = "public_key.pem"

loaded_private_key = load_private_key_from_pem(private_key_filename)
print(loaded_private_key)
loaded_public_key = load_public_key_from_pem(public_key_filename)

data = input("Enter the Original Name Please:>").encode()
encrypt_and_store(data, loaded_public_key, "OriginalName.pem")
encrypted_file = "OriginalName.pem"
decrypted_data = load_and_decrypt(encrypted_file, loaded_private_key)

print("Decrypted Data:", base64.b64decode(decrypted_data).decode('utf-8'))
