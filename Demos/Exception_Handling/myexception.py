class MyException(Exception):
    def __init__(self,*args):
        self.age = args
        print("I am in Con Of MyException class")
    def __str__(self):
        return f"Bhai age proper enter kar"
        
        
