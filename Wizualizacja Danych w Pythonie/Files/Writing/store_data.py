def store_personal_data(person: tuple):

    name, age, height=person
    entry=f"{name};{age};{height}\n"
    f=open('people.csv', 'r')
    data=set(f.readlines())
    if entry not in data:
        f.close()
        f2=open('people.csv','a')
        f2.write(entry)
        f2.close()
