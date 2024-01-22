unit=int(input())

if unit>50:
    a=(50*2)
else:
    a=(unit*2)
    
if unit<=50 or unit>=50:
    b=0
    if unit>150:
        b=(100*3)
    else:
        if unit>50:
            a1=unit-50
            b=(a1*3)
        
if unit<=50 or unit>=50:
    c=0
        
    if unit>250:
        c=(100*5)
    else:
        if unit>=150:
            b1=unit-150
            c=(b1*5)
if unit<=50 or unit>=50:
    d=0
    if unit<=150 or unit>=150:
        d=0
        if unit>251:
            c1=unit-250
            d=(c1*8)
total=a+b+c+d
result=total*0.2
print(result+total)