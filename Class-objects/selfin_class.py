class Vehicle: 
    def __init__(self, model,engine):
        self.model = model
        self.engine= engine
    
    def details(self):
        print(f"{self.model} has {self.engine} engine. ")


v1= Vehicle("Lamborgini","8-Strokes" )
v1.details()
v2 = Vehicle("Ferrari", "7- Strokes")
v2.details()

print(v1.model)

class SmartLight:
    def __init__(self, color):
        # We take the color you typed and 'stick' it to this specific light
        self.color = color
        print(f"Light is now {self.color}" )

# Creating the objects
kitchen_light = SmartLight("Warm White")
bedroom_light = SmartLight("Deep Blue")


