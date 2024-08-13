def matrix_sum():
    f=open('matrix.txt', 'r')
    count_matrix=0
    for line in f:
        line=line.replace('\n','')
        temp=line.split(',')
        for i in temp:
            count_matrix+=int(i)
    return count_matrix


def matrix_max():
    f=open('matrix.txt', 'r')
    max_matrix=0
    for line in f:
        line=line.replace('\n','')
        temp=line.split(',')
        for i in temp:
            if int(i)>max_matrix:
                max_matrix=int(i)
    return max_matrix


def row_sums():
    f=open('matrix.txt', 'r')
    rows=[]
    for line in f:
        rosum=0
        line=line.replace('\n','')
        temp=line.split(',')
        for i in temp:
            rosum+=int(i)
        rows.append(rosum)

    return rows