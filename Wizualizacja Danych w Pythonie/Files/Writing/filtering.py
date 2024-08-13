def filter_solutions():
    f=open('solution.csv', 'r')
    correct=[]
    incorrect=[]
    for line in f:
        line=line.replace('\n','')
        temp=line.split(';')
        if int(eval(temp[1]))==int(temp[2]):
            correct.append(temp)
        else:
            incorrect.append(temp)
    f.close()

    fc=open('correct.csv','w')
    for temp in correct:
        fc.write(f'{temp[0]};{temp[1]};{temp[2]}\n')
    fc.close()

    fi = open('incorrect.csv', 'w')
    for temp in incorrect:
        fi.write(f'{temp[0]};{temp[1]};{temp[2]}\n')
    fi.close()