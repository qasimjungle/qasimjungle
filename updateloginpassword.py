import bcrypt
import csv
import datetime
import time
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
current_value = 0  # Global variable for calculation of the amount of the time sleep at each iteration of this function
def increase_value(amount):
    global current_value
    current_value += amount
    time.sleep(current_value)
def old_login():
 user_name_login = input("\033[0;32mEnter your name to log in please:>")
 matched_row = find_matching_row(user_name_login)
 found_salt=matched_row[1]
 if matched_row:
    user_password_login=input("Enter  the password to complete Login Process:>")
    found_salt = found_salt.encode()
    hashed_password = bcrypt.hashpw(user_password_login.encode(), found_salt)
    csv_filename = 'hashpassword.csv'
    all_rows = read_csv_as_list(csv_filename)
    list_of_lists =all_rows
    target_string = str(hashed_password)
    found = False
    for inner_list in list_of_lists:
      if target_string in inner_list[0]:
            found = True
            break
    if found:
            print("\033[0;36 Login process is completed")
    else:
        amount=1
        increase_value(amount)
        print(" Try again please")
 else:
     print("033[0;31m Enter the right User_name Please")
     old_login()



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
old_login()
