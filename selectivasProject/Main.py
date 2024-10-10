#Simple
a = 33
b = 200
if (b > a):
    print(b, "es mayor que", a)

#Doble
y = 200
z = 333
if (y > z):
    print(y, "es mayor que", z)
else:
    print(y, "no es mayor que", z)

#Multiple
x = 200
g = 207
if (x > g):
    print(x, "es mayor que", g)
elif (x < g):
    print(x, "es menor que", g)
else:
    print(x, "es igual que", g)

p = 28
if (p > 10):
    print(p, "Por encima de diez,")
    if (p > 20):
        print("Y por encima de veinte!")
    else:
        print("pero no por encima de veinte.")

print("Estudiar los sabados", end=' ')
print("es genial")

print("Daniela","Luis","Carlos","Camila") #agrega espacio por defecto
print("Daniela","Luis","Carlos","Camila", sep="") #Quita el espacio
print("Daniela","Luis","Carlos","Camila", sep=",") #agrega una coma
print("Daniela","Luis","Carlos","Camila", sep="_", end="_Curso_Python") #Implementacion de end y sep