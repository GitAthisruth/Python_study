def randomly():
    from random import choice
    d=choice(a)
    e=choice(b)
    f=choice(c)
    g=f'{d} {e} {f}'
    return g
a=['hey!!','hello!!','hai!!']
b=['yo!!! Whatsapp!!','Nice to meet you!!','How are you!!']
c=['Athisruth!!','Melbin!!','Mann!!!']
print(randomly())