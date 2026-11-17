def analizador_lexico(codigo):
    estado=0
    i=0
    n=len(codigo)
    pal=''
    num=''
    tokens=[]
    
    while i<n:
        c=codigo[i]
        if estado==0:
            if c.isspace():
                i=i+1
                continue
            if c.isdigit():
                num=num+c
                estado=1
                continue
            elif c.isalpha():
                estado=2
                pal=pal+c
                i=i+1
                continue
            elif c=='(':
                i=i+1
                estado=3
                continue
            elif c==')':
                i=i+1
                estado=4
                continue
        
        elif estado==2:
            if c.isalpha():
                pal=pal+c
                i=i+1
            else:
                if pal=='if':
                    tokens.append(1000)
                elif pal=='or':
                    tokens.append(1001)
                elif pal=='and':
                    tokens.append(1002)
                elif pal=='True':
                    tokens.append(1003)
                elif pal=='False':
                    tokens.append(1004)
                else:
                    tokens.append(2000)
                
            estado=0
            pal=''

        elif estado==1:
            if c.isdigit():
                estado=1
                num=num+c
                i=i+1
            else:
                tokens.append(2001)
                estado=0
                num=''
                
        elif estado==3:
            tokens.append(10)
            estado=0
        elif estado==4:
            tokens.append(11)
            estado=0

    return tokens

codigo_if='''
if(12)
'''
print(analizador_lexico(codigo_if))
            
            