text=input("Please type in a sentence: ")
for x in text.split(' '):
    try:
        print(x[0])
    except:
        pass