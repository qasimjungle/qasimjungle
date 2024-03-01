
def pandas_series_mode():
    a = []
    v = int(input('Enter how many values you want in the array:'))
    for i in range(0, v):
        c = int(input("Start Entering the value : "))
        a.append(c)
    myseries = pd.Series(a)
    print(myseries)


def access_item(myseries):
    k = int(input('Enter the Index  of the item to access from the series:'))
    print(myseries[k])

