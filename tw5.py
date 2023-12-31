x1 = [1, 1]
x2 = [1, -1]
x3 = [-1, 1]
x4 = [-1, -1]
xilist = [x1, x2, x3, x4]
y = [1, -1, -1, -1]
w1 = w2 = b = 0
# b = 1

def heb_learn():
    global w1, w2, b
    print("dw1\tdw2\tdb\tw1\tw2\tb")
    i = 0
    for xi in xilist:
        dw1 = xi[0]*y[i]
        dw2 = xi[1]*y[i]
        db = y[i]
        w1 += dw1
        w2 += dw2
        b += db
        print(dw1,dw2,db,w1,w2,b,sep='\t')
        i += 1

print('learning...')
heb_learn()
print('Learning completed')
print("Output of AND gate using obtained w1,w2,bw :")
print("x1\tx2\ty")
for xi in xilist:
    print(xi[0],xi[1],1 if w1*xi[0]+w2*xi[1]+b > 0 else -1, sep='\t')
print(f"Final weights are : w1 = {w1} w2 = {w2}")
