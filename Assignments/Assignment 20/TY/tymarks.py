class TYMarks:
    def __init__(self,theory=0,practical=0):
        self.theory = theory
        self.practical = practical

    def __str__(self):
        return f"Theory = {self.theory}, Practical = {self.practical}"
           
