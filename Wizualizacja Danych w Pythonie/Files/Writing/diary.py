while (n:=int(input("1 - add an entry, 2 - read entries, 0 - quit\nFunction: ")))!=0:
    if n==1:
        f=open('diary.txt', 'a')
        f.write(f'{input("Diary entry: ")}\n')
        print("Diary saved\n")
        f.close()
    else:
        f=open('diary.txt', 'r')
        print(f"Entries:\n{''.join(f.read())}", end='')
        f.close()

print("Bye now!")