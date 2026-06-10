def py():
    f=open('padma.txt','w+')
    f.write('ROW lAT \n --------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
py()

def py():
    
    f=open('padma.txt','a+')
    f.write('col lat \n---------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
py()

def py():
    
    f=open('padma.txt','a+')
    f.write('row lat upper \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()
def py():
   
    f=open('padma.txt','a+')
    f.write('col rat upper \n------------------\n')
    
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(j+65)))
        f.write('\n')
py()  

def py():
    
    f=open('padma.txt','a+')
    f.write('col lat lower \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(j+97)))
        f.write('\n')
    f.close()
py()

def py():
   
    f=open('padma.txt','a+')
    f.write('row lat lower \n------------------\n')
    for i in range(1,6):
        for j in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
py()

def py():
  
    f=open('padma.txt','a+')
    f.write('inverse row lat \n------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(i))
        f.write('\n')
    f.close()
py()
def py():
    
    f=open('padma.txt','a+')
    f.write('inverse col lat \n------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(j))
        f.write('\n')
    f.close()
py()
def py():
    
    f=open('padma.txt','a+')
    f.write('inverse row upper lat \n------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(chr(i+64)))
        f.write('\n')
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('inverse col upper \n------------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(chr(j+65)))
        f.write('\n')       
    f.close()
py()

def py():
    f=open('padma.txt','a+')
    f.write('inverse row lower \n------------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(chr(i+96)))
        f.write('\n')
    f.close()
py()


def py():
    f=open('padma.txt','a+')
    f.write('inverse col lower \n------------------------\n')
    for i in range(6,0,-1):
        for j in range(0,i):
            f.write(str(chr(j+96)))
        f.write('\n')
    f.close()
py()
                    
    







