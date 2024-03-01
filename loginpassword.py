import bcrypt
import csv
import datetime
def find_matching_row(username_to_find):
    with open('user_name_salt.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0] == username_to_find:
                return row
    return None
def read_csv_as_list(filename):
    data = []  # List to store all rows
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)

    return data
def search_value_in_column(file_name, Username, user_name):
    with open('user_name_salt.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row[Username] == user_name:
               pass
            else:
              print("THIS IS ALREADY OCUPPIED")
    return None  
def new_login():
 user_name_login = input("Enter your name to log in please:>")
 matched_row = find_matching_row(user_name_login)
 found_salt=matched_row[1]
 if matched_row:
    user_password_login=input("Enter  the password to complete Login Process:>")
    found_salt = found_salt.encode()# Convert bytes to a string
    hashed_password = bcrypt.hashpw(user_password_login.encode(), found_salt)
    print(hashed_password)
    csv_filename = 'hashpassword.csv'  # Replace with the actual filename
    all_rows = read_csv_as_list(csv_filename)
    print(all_rows)
    list_of_lists =all_rows
    target_string = str(hashed_password)
    found = False

    for inner_list in list_of_lists:
      if target_string in inner_list[0]:
         found = True
         break

    if found:
      print(f"The target string '{target_string}' was found in the list of lists.")
    else:
      print(f"The target string '{target_string}' was not found in the list of lists.")

 else:
    print("No match found.")


user_name = input("Enter the User name please:>")
file_name='user_name_salt.csv'
Username='Username'
search_value_in_column(file_name, Username, user_name)
user_password = input("Enter your password please:>")
salt = bcrypt.gensalt()
encoded_salt = salt.decode()
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
with open('user_name_salt.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([user_name, encoded_salt,formatted_datetime])
print("Data appended to CSV file.")

hashed_password = bcrypt.hashpw(user_password.encode(), salt)
print(hashed_password)
hashed_password=str(hashed_password)
file_path = "hashpassword.csv"
with open('hashpassword.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([hashed_password])

print("Now it is time to log in to the Game")
new_login()
