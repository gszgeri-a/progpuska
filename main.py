f = open('szoveg.txt','r',encoding='utf8')
jegyek = []
#tördelt lista
for sor in f:
    jegyek.append(sor.split())
    
    
#int-é alakítja a tagokat ha szoveg.txtbe így vannak az adatok : "xy név" 1 32 51 51 2
for i in range(len(jegyek)):
    for h in range(1,len(jegyek[i])):
        jegyek[i][h] = int(jegyek[i][h])
print(jegyek)


for i in jegyek:
    osszejegy = 0
    mennyiseg = 0
    for a in i[1:]:
        osszejegy += a
        mennyiseg += 1
    #átlaguk
    print(osszejegy / mennyiseg)