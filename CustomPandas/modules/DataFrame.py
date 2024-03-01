def dataframe_demo():

    data = {
        "\033[0;31mcalories": [420, 380, 390],
        "\033[0;31mduration\033[0;3m": [50, 40, 45]
    }
    df = pd.DataFrame(data, index=["day1", "day2", "day3"])
    print(df)



def access_row():
    c = str(input("Enter the label of the row to access"))
    print("\033[0;31m", df.loc[str(c)], "\033[0;3m")

