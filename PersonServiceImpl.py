# _*_ coding:utf-8 _*_
__author__ = 'KevenPotter'

from py.thrift.generated import ttypes


class PersonServiceImpl:
    def getPersonByUsername(self, username):
        print("Got Client param:" + username)

        person = ttypes.Person()
        person.username = username
        person.age = 20
        person.married = False
        return person

    def savePerson(self, person):
        print("Got Client param:")
        print(person.username)
        print(person.age)
        print(person.married)
