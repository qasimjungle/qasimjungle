def finding_correlation():
    b = str(input('\033[0;31mEnter the File name for Finding correlation of the file  with .csv extention'))
    df = pd.read_csv(b)
    print(df.corr())

