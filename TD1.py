#Exercice 1
#27   -   DaDaDaDa   -   PaLAPaLa    -    2.5    -   2     -    1
#
#Exercice 2
#444  -   3.2    -     .0750.75


#Exercice 3

i=0
for i in range (20):
    print((i+1)*7)
    i+=1

#Exercice 4

i=0
a = input("nb")
while (i<12):
    print(a)
    a=int(a)*3
    i+=1


#Exercice 5

sec = input("Secondes a convertir:" )
Jours =int(sec)//(60*60*24)
sec = int(sec)%(60*60*24)
heures = sec//(60*60)
sec = sec%(60*60)
minutes =  sec//60
sec= sec%60
print(f"jours : {Jours}, heures : {heures}, minutes : {minutes}, sec : {sec}")


#Exercice 6
i=0
for i in range(6):
    print("*"*(i+1))



#Exercice 7

mot = input("Mot: ")
i = 0
mot2 = ""
for i in range (len (mot)):
    lettre =mot[-(i+1)]
    mot2 = mot2+lettre
print(mot2)


#Exercice 8

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2= ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre','Octobre', 'Novembre', 'Décembre']
t3=[]
i=0
t3.append(t1[], t2[])