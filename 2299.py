class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        
        special_chars = [*"!@#$%^&*()-+"]

        requirements = {'lower': False,
                        'upper': False,
                        'digit': False,
                        'special': False}
        
        for index in range(len(password)):
            char = password[index]
            try:
                int(char)
                requirements['digit'] = True
            except ValueError:
                pass
            if char in special_chars:
                requirements['special'] = True
            elif ord(char) >= 97 and ord(char) <= 122:
                requirements['lower'] = True
            elif ord(char) >= 65 and ord(char) <= 90:
                requirements['upper'] = True
            if index == len(password) - 1:
                pass
            else:
                try:
                    if password[index] == password[index+1]:
                        return False
                except ValueError:
                    pass
        
        return all(requirements.values())
