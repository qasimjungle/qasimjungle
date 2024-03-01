def loading_file():
    b = str(input('Enter the File name you want ot read in data frame: with .csv extention'))
    df = pd.read_csv(b)
    print(df.to_string())


def maximum_row_file():
    print(pd.options.display.max_rows)


def change_row_file():
    j = int(input('\033[0;36mEnter number of row you want to give to file \033[0;3m:'))
    pd.options.display.max_rows = j
    print(pd.options.display.max_rows)


