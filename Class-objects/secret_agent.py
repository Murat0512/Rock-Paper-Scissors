class SecretAgent:
    def _init__ (self,code_name):
        self.code_name= code_name
        print(f"Agent {self.code_name} is active.")

    def __del__(self):
        print(f"Mission over, Agent {self.code_name} has left the building.")

    
spy = SecretAgent("007")
del spy


        