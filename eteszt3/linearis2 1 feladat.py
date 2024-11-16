print("Írd be a vektort x és y részét kölön külön a consolba. Ezen karakterekből, space nélkül: x y + - 0123456789\n")

x = input("x rész:")
teszt= True
while teszt:
    teszt = False
    for k in x:
        if k not in "xy+-0123456789":
            teszt = True
            x = input("helytelen x, probáld újra:")
            break

y = input("y rész:")
teszt= True
while teszt:
    teszt = False
    for k in x:
        if k not in "xy+-0123456789":
            teszt = True
            y = input("helytelen y, probáld újra:")
            break

print('(', x, ',',  y, ')', '\n')


def get(tengey, vect):
    vect: str
    s = vect.find('x')

    szorzo = 0
    if tengey == 'x':
        if s != -1 and vect[:s]:
            if vect[:s] == '-':
                szorzo = -1
            else:
                szorzo = int(vect[:s])
        elif s != -1:
            szorzo = 1

    else:
        if s != -1:
            vect = vect[s+1:]
            vect = vect.lstrip('+')
        e = vect.find('y')

        if e != -1 and vect[:e]:
            if vect[:e] == '-':
                szorzo = -1
            else:
                szorzo = int(vect[:e])
        elif e != -1:
            szorzo = 1

    return szorzo


a = [[get('x', x), get('x', y)],
     [get('y', x), get('y', y)]]

#print(a)

s = -a[0][0]-a[1][1]
t = a[0][0]*a[1][1]-a[0][1]*a[1][0]

print(f"f = λ^2 {s}λ {'+' if t>0 else ''}{t if t!=0 else ''}\n")
print("ha egyezik pipa")
