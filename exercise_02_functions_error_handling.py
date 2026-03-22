"""
exercise_02_functions_error_handling.py

Simulates input validation before making an API call.
Practices writing reusable functions, returning values,
and handling errors gracefully with try/except.

Author: Hunter
Date: 2026-03-21
1.)functions
    validate user name
        checks username is atleast 3 characters long
        if its too short, raise ValueErrow with helpful msg
    validate_age(handles age that cant be converted to it & age out of range)
        converts age to an it
        check its between 13-120
    validate zip
        checks zipcode is exactly 5 digits
        raise ValueError if not
2.)##NEWneverDONE## wrap functions in try/except block
        prints clear error message if anything else fails
        
"""

# ── User input (pretend this came from a form or terminal) ─────────────────────

user_data = {
    "username": "hcraft",
    "age": "nineteen",
    "email": "hcraft.developer@gmail.com",
    "zip_code": "391"
}

#validate username function
def validate_username(user_name):
    if len(user_name) < 3:
        raise ValueError("Username must be atleast 3 characters long")
    
#validate age(covert age to int and check if valid 13-120)
def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        raise ValueError("Age must not contain anything but numbers")
    if age < 13 or age > 120:
        raise ValueError("Age must be 13-120")
    
#validate zip(checks 5 digits long if not ValueError)
def validate_zip(zip):
    if not zip.isdigit():
        raise ValueError("Zip must only contain digits")
    if len(zip) != 5:
        raise ValueError("The length of a zipcode is always 5 digits")
        
  #Wrap the functions in try/except block
try:
    validate_username(user_data["username"])   
    validate_age(user_data["age"]) 
    validate_zip(user_data["zip_code"]) 
except ValueError as e:
    print(f"Validations error: {e}")
  
                 