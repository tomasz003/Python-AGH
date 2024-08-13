def read_fruits():
    dict={}
    f=open('fruits.csv', 'r')
    for line in f:
        line=line.replace('\n','')
        parts=line.split(';')
        print(parts)
        dict[parts[0]]=parts[1]

    return dict
