name=input("Whom should I sign this to: ")
filename=input("Where shall I save it: ")

f=open(filename, 'w')
f.write(f'Hi {name}, we hope you enjoy learning Python with us!')
f.close()