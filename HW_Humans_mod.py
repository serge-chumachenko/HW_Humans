class Human(object):
    def __init__(self,name,last_name,age,sex):
        self.name = name
        self.last_name = last_name
        self.age = age  
        self.sex = sex
    def __str__(self):
        return ("Name: {}||Last Name: {}||Age: {}||Sex: {}".format(self.name,self.last_name,self.age,self.sex))
    def info(self):
        info = (("Name: {}||Last Name: {}||Age: {}||Sex: {}".format(self.name,self.last_name,self.age,self.sex)))
        return  info

class Male(Human):
    def __init__(self,name,last_name,age):
        super().__init__(name,last_name,age,"M")

class Female(Human):
    def __init__(self,name,last_name,age):
        super().__init__(name,last_name,age,"F")

def create_profile(inf,ID):
    ID_Book = {}
    ID = ID.__next__()
    ID_Book[ID] = inf
    return ID_Book

def MyGenID(start = 1):
    if start is not None:
        number = int(start)
    else:
        number = 1
    while True:
        if len(str(number))<6:
            p = 6 - len(str(number))
            yield '0' * p + str(number) 
            number+=1
        else:
            yield str(number)
            number+=1

class Collection(Human):
    def __init__(self,lst):
        self.lst = lst

    def __str__(self):
        for i in self.lst:
            print(i)
        else:
            return ("The list ends here!")

    def reg(self):
        a = {}
        ID = MyGenID()
        for i in self.lst:
            a.update(create_profile(i.info(),ID))
        return(a)

class AfterAge(Collection):
    def __init__(self,lst,dage = None):
        self.lst = lst
        self.leight = len(lst)
        self.dage = 21 if dage is None else dage

    def __iter__(self):
        return self
    def __next__(self):
        if self.leight == 0:
            raise StopIteration
        else:
            self.leight = self.leight - 1
            if self.lst[self.leight].age > self.dage:
                return (self.lst[self.leight])

class UntilAge(Collection):
    def __init__(self,lst,dage = None):
        self.lst = lst
        self.leight = len(lst)
        self.dage = 21 if dage is None else dage
    def __iter__(self):
        return self
    def __next__(self):
        if self.leight == 0:
            raise StopIteration
        else:
            self.leight = self.leight - 1
            if self.lst[self.leight].age < self.dage:
                return (self.lst[self.leight])

class OnlyMen(Collection):
    def __init__(self,lst):
        self.lst = lst
        self.leight = len(lst)
    def __iter__(self):
        return self
    def __next__(self):
        if self.leight == 0:
            raise StopIteration
        else:
            self.leight = self.leight - 1
            if self.lst[self.leight].sex == "M":
                return (self.lst[self.leight])

class OnlyWomen(Collection):
    def __init__(self,lst):
        self.lst = lst
        self.leight = len(lst)
    def __iter__(self):
        return self
    def __next__(self):
        if self.leight == 0:
            raise StopIteration
        else:
            self.leight = self.leight - 1
            if self.lst[self.leight].sex == "F":
                return (self.lst[self.leight])


if __name__ == '__main__':
    print("Hello Humans!")
