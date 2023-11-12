while True:
    names = ['ali', 'vali', 'gani']
    try:
        index = int(input("Enter index: "))
        print(names[index])
    except ValueError:
        print("Xato")
    except IndexError:
        print("Xato index")
