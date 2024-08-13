students=input("Student information: ")
exercices=input("Exercises completed: ")

gradebook={}
file_st=open(students, 'r')

for line in file_st:
    line = line.replace('\n', '')
    id, name, last_name = line.split(';')
    if id=='id':
        continue
    gradebook[id]=[name, last_name, 0]

file_ex=open(exercices, 'r')

for line in file_ex:
    line=line.replace('\n','')
    id, *scores = line.split(';')
    if id=='id':
        continue
    gradebook[id][2]=sum(int(x) for x in scores)

for name, last_name, result in gradebook.values():
    print(f"{name} {last_name} {result}")










