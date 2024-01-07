import re

#Example 1 : Phone number
def find1(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

text = "The agent's phone number is 408-555-1234 or 8783515482. Call soon!"
pattern = '\d{3}-\d{3}-\d{4}|\d{10}'
print('Phone number: ')
find1(pattern, text)


#Example 2 : Email
def find2(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

text = "The agent's email is abc@xyz.com"
pattern = '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com'
print('\nEmail: ')
find2(pattern, text)

# Example 3 : URL
def find3(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

text = "The agent's URL is https://www.google.com"
pattern = 'https?://[^\s/$.?#].[^\s]*'
print('\nURL: ')
find3(pattern, text)

#Example 4 : Date
def find4(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

text = "The agent's date of birth is 12/12/1990"
pattern = '\d{2}/\d{2}/\d{4}'
print('\nDate: ')
find4(pattern, text)

#Example 5 : Name
def find5(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

text = "The agent's name is Mr. Bond"
pattern = 'Mr\.?\s[A-Z]\w*'
print('\nName: ')
find5(pattern, text)

# #Example 6 : All
def find6(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

text = "The agent's name is Mr. Potato. The agent's date of birth is 12/12/1990. The agent's email is potato@duck.eu. The agent's phone number is 408-555-1234 or 8783515482. Call soon! The agent's URL is https://www.random.duck"
pattern = 'Mr\.?\s[A-Z]\w*|\d{2}/\d{2}/\d{4}|\d{3}-\d{3}-\d{4}|\d{10}|[a-zA-Z0-9]+@[a-zA-Z0-9]+\.\w+|https?://[^\s/$.?#].[^\s]*'
print('\nAll: ')
find6(pattern, text)