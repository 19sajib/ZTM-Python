class User():
    def __init__(self, email):
        self.email = email
    
    def signed_in(self):
        print("User is logged in.")
        
    def attack(self):
        print("Do nothing.")
        
class Wizard(User):
    def __init__(self, name, power, email):
        # User.__init__(self, email)
        super().__init__(email)     # same as using the above command, it does not take 'self' parameter
        self.name = name
        self.power = power
     
    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")

wizard1 = Wizard("sajib", 50, 'sajib@gmail.com')
print(wizard1.email)
  