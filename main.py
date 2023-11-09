class human:
    
    def __init__(self,n,a,h):
        print('')
        self.__name=n
        self.__age=a
        self.height=h
        
    def print(self):

        print(f'имя:{self.__name}')
        print(f'Возраст:{self.__age}')
        print(f'рост:{self.height}')
        print('-'*30)
    @property        
    def name(self):
        return '' + self.__name
    
    @name.setter
    def name(self,n):
        if len(n)>=2 and len(n)<=20:
            self.__name=n
        else:
            print(f'Недопустимое имя:{n}')
    @property        
    def age(self):
        return 'Мне:' + self.__age
    
    @name.setter
    def age(self,a):
        if int(a)>=2 and int(a)<=20:
            self.__age=a
        else:
            print(f'Недопустимый возраст:{a}')
 
    
q=human('петя',10,110)
q.name='Ян'
name=q.name
print(name)
q.age='15'
age=q.age
q.print()


class stud(human):
    def study(self):
        print(f'{self.name} Учится')
q=stud('Petya',19,190)
q.study()



