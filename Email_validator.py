def is_valid_email(email):
    # Check if the email contains exactly one '@' symbol
    if email.count('@') != 1:
        return False
    
    #checking if mail id cannot start with - or @
    if email[0]=='-' or email[0]=='@':
        return False

    # Split the email into local part and domain part
    local_part, domain_part = email.split('@')

    #checking punctuation marks are comming consecutively or not
    if '!!' in email: 
        return False
    
    #checking if fullstop is having full stop or not
    if not '.' in domain_part: 
        return False

    #checking length of local name is less than 64 or not
    if not len(local_part)<=64:
        return False
    
    #checking '_' not allowed in domain part
    if '_' in domain_part:
        return False

    # Check if the local part and domain part are non-empty
    if not local_part or not domain_part:
        return False

    # Check if the local part contains only alphanumeric characters and some special characters
    if not all(char.isalnum() or char in ['.', '_', '-','!','#','$','%','&',"'",'*','+','/','=','?','^','{','}','|','~',','] for char in local_part):
        return False

    # Check if the domain part contains at least one '.' and only alphanumeric characters
    if '.' not in domain_part or not all(char.isalnum() or char == '.' for char in domain_part):
        return False

    # Check if the email ends with a valid top-level domain (TLD)
    if not domain_part.split('.')[-1].isalpha():
        return False
    
    # check if the total length of an email address must not exceed 254 characters
    if not len(email) <= 254:
        return False
    
    # Check if '@' symbol is more than 6 characters from the end
    at_index = email.find('@')
    
    if not at_index != -1 and (len(email) - at_index) > 6:
        return False
    
    # checking if spaces in between
    if ' ' in email:
        return False

    return True

# Get email input from the user
user_email = input("Enter a sample email to check whether the email is valid or not ?:: ")

# Check if the email is valid
if is_valid_email(user_email):
    print("Valid.")
else:
    print("Invalid.")
