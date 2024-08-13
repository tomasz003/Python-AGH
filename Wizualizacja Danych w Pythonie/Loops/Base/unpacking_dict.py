a = {x: 2*x+1 for x in [2,4,6,8]}
b = {x: 3*x-1 for x in [2,5,8]}
c = {**a,**b}
print(f"a={a}\nb={b}\nc={c}")
