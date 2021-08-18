# RandomPassword

A simple python library to generate customizable random passwords in python!

### Installation:

```pip install RandomPassword```

### Import:

```python 
import RandomPassword
```

### Making a simple password:

```python
import RandomPassword

a = RandomPassword.RandomPassword()
password = a.generate_random_password(length=10)
print(password)
```

### Customizing your password:

The ```generate_random_password()``` has some parameters to customize the password!

* ```include_upper_case_alphabets``` ---> Set to 'True' if you want uppercase alphabets in your password
* ```include_lower_case_alphabets``` ---> Set to 'True' if you want lowercase alphabets in your password
* ```include_special_characters``` ---> Set to 'True' if you want special characters in your password
* ```include_numbers``` ---> Set to 'True' if you want digits in your password

### Thank you!
