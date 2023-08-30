"""module for implementing data validation"""
import re

def validate_password(pwd1:str, pwd2:str):
    print(pwd1)
    print(pwd2)
    if pwd1 != pwd2:
        return 'Password must be same as Repeat password'
        
    if len(pwd1) < 6:
        return 'Password is to short'
    # pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$"

    result = re.match(pattern, pwd1)
    if result == None:
        return 'Password not accepted'
    return None
