class Firth_parametrs:
    def __init__(self) -> None:
        self.parametr =[]

        self.object = []
        self.parametr.append(self)

    def __enter__(self):
        self.object = self.parametr.copy()
        return self
    
    def __exit__(self, parametr_type, parametr_values, parametr):
        if parametr_type:
            self.parametr = self.object.copy()
        return False

    



class Second_parametrs:
    def __init__(self, parametr) -> None:
        self.parametr = parametr
        self.parametr.append(self)



    def __enter__(self):
        return self.parametr.__enter__()
    
    
    
    def __exit__(self, parametr_type, parametr_values, parametr):
        return self.parametr.__exit__(parametr_type, parametr_values, parametr)
    
parametrs_1 = Second_parametrs
try:
    with Firth_parametrs() as parametrs_1:
        parametrs_1.append(1)
        parametrs_1.append(2)
        raise ValueError("An error occurred!")
        parametrs_1.append(1)

except ValueError as comback:
    print(comback)

print(parametrs_1.parametr)
