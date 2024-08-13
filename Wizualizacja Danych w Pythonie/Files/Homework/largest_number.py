def largest():
    max_record=-1000000000000000
    f=open('numbers.txt','r')
    for line in f:
        line=line.replace('\n','')
        if int(line)>max_record:
            max_record=int(line)
    return max_record