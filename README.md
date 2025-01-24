### **Email Validator Project: Detailed Description**

#### **Project Overview**
The Email Validator project is a Python-based script designed to check the validity of an email address based on various predefined rules. The script ensures that an email conforms to standard formatting rules, including structural correctness, character constraints, length restrictions, and domain validity.

This validation function helps prevent users from entering incorrect or improperly formatted email addresses in applications, registration forms, and authentication systems.

---

### **Functional Description**
The project consists of a Python function named `is_valid_email(email)`, which performs multiple checks to determine whether the given email is valid. The program prompts the user to enter an email address, validates it using the function, and then displays whether it is "Valid" or "Invalid."

---

### **Validation Rules Implemented**
The `is_valid_email(email)` function applies a series of checks to ensure the entered email meets the required criteria.

#### **1. Ensuring Exactly One '@' Symbol**
```python
if email.count('@') != 1:
    return False
```
- The email must contain exactly one '@' symbol.
- If the '@' count is not exactly one, the function returns `False`.

#### **2. Email Cannot Start with '@' or '-'**
```python
if email[0] == '-' or email[0] == '@':
    return False
```
- Ensures that an email does not begin with `@` or `-`, which are not valid starting characters.

#### **3. Splitting the Email into Local and Domain Parts**
```python
local_part, domain_part = email.split('@')
```
- The email is divided into two parts:
  - **Local part** (before `@`)
  - **Domain part** (after `@`)

#### **4. Checking for Consecutive Punctuation Marks**
```python
if '!!' in email: 
    return False
```
- Ensures that `!!` (double exclamation marks) do not appear consecutively.

#### **5. Domain Must Contain a Period ('.')**
```python
if not '.' in domain_part: 
    return False
```
- The domain part must contain at least one `.` to separate the domain name from the top-level domain (TLD) (e.g., `.com`, `.org`).

#### **6. Local Part Must Be ≤ 64 Characters**
```python
if not len(local_part) <= 64:
    return False
```
- The local part (before `@`) must not exceed 64 characters.

#### **7. Domain Part Must Not Contain Underscore ('_')**
```python
if '_' in domain_part:
    return False
```
- The domain part should not contain `_`, as it is not allowed in domain names.

#### **8. Ensuring Both Local and Domain Parts Are Non-Empty**
```python
if not local_part or not domain_part:
    return False
```
- Ensures that both parts of the email exist.

#### **9. Valid Characters in Local Part**
```python
if not all(char.isalnum() or char in ['.', '_', '-','!','#','$','%','&',"'",'*','+','/','=','?','^','{','}','|','~',','] for char in local_part):
    return False
```
- Allows **alphanumeric characters** and a set of **special characters** in the local part.

#### **10. Valid Characters in Domain Part**
```python
if '.' not in domain_part or not all(char.isalnum() or char == '.' for char in domain_part):
    return False
```
- The domain part should contain only alphanumeric characters and `.`.

#### **11. Checking for a Valid Top-Level Domain (TLD)**
```python
if not domain_part.split('.')[-1].isalpha():
    return False
```
- The last segment of the domain (after the last `.`) should consist only of **alphabetic** characters (e.g., `.com`, `.org`, `.edu`).

#### **12. Total Email Length Must Not Exceed 254 Characters**
```python
if not len(email) <= 254:
    return False
```
- The entire email address must be **≤ 254 characters**.

#### **13. '@' Symbol Must Be at Least 6 Characters from the End**
```python
at_index = email.find('@')
if not at_index != -1 and (len(email) - at_index) > 6:
    return False
```
- Ensures that there are at least **six characters after `@`**, avoiding cases where the domain is too short.

#### **14. Email Must Not Contain Spaces**
```python
if ' ' in email:
    return False
```
- Ensures that there are **no spaces** in the email.

---

### **User Input and Output**
```python
user_email = input("Enter a sample email to check whether the email is valid or not ?:: ")
```
- The user is prompted to enter an email address.

```python
if is_valid_email(user_email):
    print("Valid.")
else:
    print("Invalid.")
```
- The function `is_valid_email(user_email)` is called.
- If the email passes all the validation checks, the program prints **"Valid."**
- Otherwise, it prints **"Invalid."**

---

### **Use Cases**
This project can be used in:
- **Web applications** to validate email addresses during user registration.
- **Data validation** when handling user-provided email addresses.
- **Security checks** to filter out improperly formatted email inputs.

---

### **Potential Improvements**
1. **Regular Expressions (`re` module)**  
   - The current validation could be optimized using **regex patterns**.
2. **Checking Valid TLDs**  
   - Can be improved to verify that the **TLD exists** in a list of registered domains.
3. **Better Consecutive Character Checks**  
   - Expand rules to avoid multiple consecutive punctuation marks.

---

### **Conclusion**
This Email Validator project is a simple yet effective implementation to check if an email address follows standard formatting rules. It ensures the correctness of an email input by applying structural and character-based validations. This project can be further enhanced with more sophisticated checks to improve reliability.
