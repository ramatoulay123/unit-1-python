
"""
Task 0: class we do 

"""

class  Character:
    health = 20

    def __init__(self,name):
        self.name = name 
        
    def damage(self, dmg = 1 ): 
        self.health = self.health - dmg  

class player(Character): 
    health = 50

    def healing(self):
        if self.health < 50: 
           self.health = self.health + 1

enemy1 = Character("baldazor") 
enemy1.damage() 
print(enemy1.health)  
player1 = player("mr.forlenza")  
print(player1.health)










"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""
class Person: 
    gender = "female"
# class created for the person 
    # sets the variables using init and self 
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def hi(self):
        # The print statement it would print adding the variable 
        print("Hi, my name is " + self.name)
        print("My age is " + str(self.age))
# gives the values the name and age 
x = Person("Rama", 17)
# prints statement in the def function 
x.hi()











"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""
# Created a base class with a method called speak
class Animal:
    def speak(self):
        pass 
# this class is connected to animal
class Dog(Animal):
# adds speak method 
    def speak(self): 
    # what the dog would print 
        return "woof"

class Cat(Animal): 
# adds speak method for the cat 
    def speak(self):
    # what the cat would say 
        return "Meoww"  
dog = Dog() 
cat = Cat()
# prints out the statements 
print(dog.speak())
print(cat.speak()) 
        
    




"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""
# creates a class bankaccount with functions inside
class bankaccount: 
    # sets the balance to 0
    def __init__(self,owner, balance = 0): 
    # assigns the two variable
        self.owner = owner 
        self.balance = balance 
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Current balance is: ${self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance is: ${self.balance}")
        else:
            print("Withdrawal amount must be positive") 



     
        


