class person :
    def __init__(self, age,height,weight,name,surname,catch_phrase):
        self.age= age 
        self.height = height
        self.weight = weight
        self.name= name 
        self.surname= surname
        self.catch_phrase= catch_phrase

    def walk(self):
        print("Walking....")
    def run(self):
        print("Running...")

user= person(25,185,90,"John","Wick", "Come on John Wick!!" )



print(user.height)
user.walk()
user.run()
