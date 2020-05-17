
class Password:
    def __init__(self, password):
        self.password = password
        self.validate = True
        
        
    def password_exist(self):
        if not self.password:
            # self.validate = False
            raise NameError("Password should exist")
        if self.validate:
            return self.validate
        
        
    def password_length(self):
        if len(self.password) < 8:
            raise ValueError("Password should be longer than 8 characters")
            # self.validate = False
        if self.validate:
            return self.validate
        
        
    def password_lowercase(self):
        if not any(char.islower() for char in self.password):
            # self.validate = False
            raise ValueError(
                "Password should have atleast one lowercase letter")
        if self.validate:
            return self.validate
        
        
    def password_uppercase(self):
        if not any(char.isupper() for char in self.password):
            # self.validate = False
            raise ValueError(
                "Password should have at least one uppercase letter")
        if self.validate:
            return self.validate
        
        
    def password_digit(self):
        if not any(char.isdigit() for char in self.password):
            # self.validate = False
            raise ValueError(
                "Password should at least have one digit")
        if self.validate:
            return self.validate
        
        
    def password_special_character(self):
        special_Symbols = ['$', '@', '#', '%', '!','^','&','*','(',')','_','-','=','+','{','}','[',']',':',';','<','>','?',',','.','~']
        self.symbol = special_Symbols
        if not any(char in self.symbol for char in self.password):
            # self.validate = False
            raise ValueError(
                f"Password should have at least one of the symbols {special_Symbols}")
        if self.validate:
            return self.validate
        
         
            
    def password_is_valid(self, password):
        pass
    
    def password_is_ok(self, pass_is_valid):
        pass
    
if __name__ == '__main__':
    password = "That1thup@d!"
    # validate = True
    password_valid = Password(password)
    # special_Symbols = ['$', '@', '#', '%', '!','^','&','*','(',')','_','-','=','+','{','}','[',']',':',';','<','>','?',',','.','~']
    try:
        if (password_valid.password_special_character()):
            print("Password is valid")
        else:
            print("Invalid Password !!")
    except (NameError, ValueError) as error:
        print(error)
