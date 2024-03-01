def read_jason_file():
    g = str(input("Enter the File name with .json extension to read :"))
    df = pd.read_json(g)
    print(df.to_string())


def python_dictionary_json():
    print("\033[0;32mUpper is json file and Lower File is a Python Dictionary we can see similarlity between them")
    data = {
        "Duration": {
            "0": 60,
            "1": 60,
            "2": 60,
            "3": 45,
            "4": 45,
            "5": 60
        },
        "Pulse": {
            "0": 110,
            "1": 117,
            "2": 103,
            "3": 109,
            "4": 117,
            "5": 102
        },
        "Maxpulse": {
            "0": 130,
            "1": 145,
            "2": 135,
            "3": 175,
            "4": 148,
            "5": 127
        },
        "Calories": {
            "0": 409.1,
            "1": 479.0,
            "2": 340.0,
            "3": 282.4,
            "4": 406.0,
            "5": 300.5
        }
    }

    df = pd.DataFrame(data)
    print(df)


def access_rows_from_start():
    u = str(input('Enter the file Name with the .json extension:'))
    v = int(input('Enter the numbers Rows to see from the start:'))
    df = pd.read_json(u)
    print(df.head(v))


def access_rows_from_end():
    a = str(input('Enter the file name with .json extension or exit:'))
    b = int(input("Enter number of rows you want to read from the last :"))
    df = pd.read_json(a)
    print(df.tail(b))


def file_information():
    a = str(input('Enter the name of the file with .json  extention:'))
    df = pd.read_json(a)
    print(df.info())


