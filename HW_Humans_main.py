from HW_Humans_mod import Male,Female,MyGenID,create_profile,Collection,AfterAge,OnlyWomen,UntilAge,OnlyMen
DT = Male("Donald","Trump",70)
AJ = Female("Angelina","Jolie",41)
SH = Male("Sherlock","Holmes",24)
MZ = Male("Mark","Zuckerberg",32)
BG = Male("Bill","Gates",61)
MS = Female("Maria","Sharapova",29)
MJ = Male("Mike","Jordan",18)
MJ = Male("Michael","Jackson",20)
AS = Male("Arnold", "Schwarzenegger",69)
VS = Female("Viktoria","Sidorova",30)
KG = Female("Kate","Gorshkova",26)
MI = Female("Maria","Ivanova",18)
IP = Female("Irina","Petrova",21)

L = [DT,AJ,SH,MZ,BG,MS,MJ,MJ,AS,VS,KG,MI,IP]
c = Collection(L)
print("All collection!")
print(c)
print("----"*15)
print("Create a IDBook")
a = c.reg()
print(a)
print("----"*15)
print("Iterator 'After 21'")
after_age = AfterAge(L)
for i in after_age:
    if i is not None:
        print(i)
    else:
        pass
print("----"*15)
print("Iterator 'Until 21'")
until_age = UntilAge(L)
for i in until_age:
    if i is not None:
        print(i)
    else:
        pass
print("----"*15)
print("Iterator 'Only women'")
only_W = OnlyWomen(L)
for i in only_W:
    if i is not None:
        print(i)
    else:
        pass
print("----"*15)
print("Iterator 'Only men'")
only_M = OnlyMen(L)
for i in only_M:
    if i is not None:
        print(i)
    else:
        pass