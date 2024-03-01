def reading_csv_file():
    b = str(input('\033[0;31mEnter the File name you want ot read in data frame: with .csv extention'))
    df = pd.read_csv(b)
    print(df.to_string())


def Removing_File_Row():
    b = str(input('Enter the File name you want to remove the empty cell  with .csv extention'))
    df = pd.read_csv(b)
    print(df.to_string())
    df.dropna(inplace=True)
    print(df.to_string())
    # Notice in the result that some rows have been removed (row 18, 22 and 28).
    # These rows had cells with empty values.


def filling_empty_row():
    b = str(input('Enter the File name you want to add something to empty  cell  with .csv extention'))
    c = str(input('Enter something you want to replace with empty cell in file :'))
    df = pd.read_csv(b)
    print(df.to_string())
    df.fillna(c, inplace=True)
    print(df.to_string())
    # Notice in the result that some rows have been filled with your string(row 18, 22 and 28).
    # These rows had cells with empty values.


def mean_mode_median():
    b = str(input('Enter the File name you want to add something to empty  cell  with .csv extention'))
    c = str(input('Enter the name of the cloumn whose mean, mode , median you want to calculate in file :'))
    df = pd.read_csv(b)
    print(df.to_string())
    x = df[c].mean()
    y = df[c].mode()
    z = df[c].median()
    print("\033[0;31mMean of given coulmn is =", x)
    print("\033[0;32mMode of Given coulmn is =", y)
    print("\033[0;35mMedian of Given coulmn is =", z)


def remove_duplicate_row(df):
    print(df.duplicated())
    df.drop_duplicates(inplace=True)
    print(df.to_string())


def add_something_empty_cell():
    b = str(input('\033[0;36mEnter the File name you want to add something to empty  cell  with .csv extention'))
    df = pd.read_csv(b)
    print(df.to_string())

