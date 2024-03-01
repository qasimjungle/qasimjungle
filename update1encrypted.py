import csv
import datetime
import time
import bcrypt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import  rsa, padding
current_value = 0  # Global variable for calculation of the amount of the time sleep at each iteration of this function

def load_private_key():
    with open("user_name_salt.csv", "rb") as keyfile:
        private_key = serialization.load_pem_private_key(
            keyfile.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def decrypt_field(private_key, encrypted_value):
    decrypted_field = private_key.decrypt(
        encrypted_value.encode(),  # Encode the string as bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_field.decode()

def decryption_list():
    loaded_private_key = load_private_key()
    target_column_index = 0
    decrypted_column_values = []
    decrypted_rows = []  # Add this line to initialize the list for decrypted rows
    with open("user_name_salt.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) > target_column_index:
                Username = row[target_column_index]
                decrypted_field = decrypt_field(loaded_private_key, Username)
                decrypted_column_values.append(decrypted_field)
                row[0] = decrypted_field
                decrypted_rows.append(row)  # Append the row to decrypted_rows

    return decrypted_column_values, decrypted_rows  # Return both the column values and the rows

# Call the decryption_list function to get the results
decrypted_values, decrypted_rows = decryption_list()

# Print decrypted values and rows
print("Decrypted Values:", decrypted_values)
for decrypted_row in decrypted_rows:
    print("Decrypted Row:", decrypted_row)

def old_login():
    user_name_login = input("\033[0;32mEnter your name to log in please:>")
    List = decryption_list()
    print(List)
    if user_name_login in List:
     matching_hashed_password()
    else:
        print("Your are not LogIN ")

def matching_hashed_password(matched_row):
        found_salt = matched_row[1]
        user_password_login = input("Enter  the password to complete Login Process:>")
        found_salt = found_salt.encode()
        hashed_password = bcrypt.hashpw(user_password_login.encode(), found_salt)
        all_rows = read_csv_as_list()
        list_of_lists = all_rows
        target_string = str(hashed_password)
        found = False
        for inner_list in list_of_lists:
            if target_string in inner_list[0]:
                found = True
                break
        if found:
################################END OF THE WHOLE PROGRAM IS HERE PRESENT ############################################
            print("\033[0;36 Login process is completed")
        else:
            amount = 10
            increase_value(amount)
            old_login()
def increase_value(amount):
    global current_value
    current_value += amount
    seconds = current_value
    wait_for_next_try(seconds)
def wait_for_next_try(seconds):
    time_elapsed = 0
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        remaining_time = seconds - time_elapsed
        print(f":Try again in seconds{time_elapsed}" , end='\r')
def read_csv_as_list():
 values_list = []
 with open("hashpassword.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:
            value = row[0]
            values_list.append(value)
 return values_list





def username_limiting():
    while True:
        input_string = input("Enter a User name (at least 8 characters): ")
        if len(input_string) >= 8:
            return input_string
        else:
            print("User name must contain  at least 8 characters long.")
            username_limiting()

def generate_rsa_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key


def save_private_key(private_key, filename):
    with open(filename, "wb") as keyfile:
        keyfile.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))


def save_public_key(public_key, filename):
    with open(filename, "wb") as keyfile:
        keyfile.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
def load_public_key(filename):
    with open(filename, "rb") as keyfile:
        public_key = serialization.load_pem_public_key(keyfile.read())
    return public_key


def encrypt_data(public_key, original_data):
    encrypted_data = public_key.encrypt(
        original_data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_data
def username_salt_datetime_store(encrypted_data, encoded_salt):
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    with open('user_name_salt.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([encrypted_data, encoded_salt, formatted_datetime])


def password_limiting():
    special_characters = "!@#$%^&*()_+{}[]|;:,.<>?/`~"
    input_string = input("Enter your password minimum 8 character  with a special character  ")

    if len(input_string) < 8:
        print("Password should be at least 8 characters long.")
        password_limiting()
    else:
        contains_special_character = any(char in special_characters for char in input_string)
        if contains_special_character:
             return input_string
        else:
             print("Input should contain at least one special character.")
             password_limiting()


def hashed_password(user_password, salt):
    hashed_password = bcrypt.hashpw(user_password.encode(), salt)
    hashed_password = str(hashed_password)
    file_path = "hashpassword.csv"
    with open('hashpassword.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([hashed_password])


if __name__ == "__main__":
 """   original_data = str(username_limiting())
    private_key, public_key = generate_rsa_key_pair()
    save_private_key(private_key, "decryptionkey.csv")
    save_public_key(public_key, "encryptionKey.csv")
    loaded_private_key = load_private_key("decryptionkey.csv")
    loaded_public_key = load_public_key("encryptionKey.csv")
    encrypted_data = encrypt_data(loaded_public_key, original_data)
    salt = bcrypt.gensalt()
    encoded_salt = salt.decode()
    username_salt_datetime_store(encrypted_data, encoded_salt)
    user_password = str(password_limiting())
    hashed_password(user_password, salt)"""
print("Now it is time to log in to the Game")
old_login()
