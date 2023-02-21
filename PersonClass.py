
class Person:

    def__init__(self, name, address, phone):
        self.__name = name 
        self.__address = address
        self.__phone = phone 
    
    def print_person(self):
        print('Name:',self.__name)
        print('Address:',self.__address)
        print('Phone:',self.__phone)

class Customer(Person):

    def __init__(self,customernum,mailinglist)
        self.__customernum = customernum
        self.__mailinglist = 
