import re

def find(pattern, text):
    match = re.findall(pattern, text)
    if match:
        print(match)
    else:
        print('Not found')

#Example 1 : Phone number
text = "The agent's phone number is 408-555-1234 or 8783515482. Call soon!"
pattern = '\d{3}-\d{3}-\d{4}|\d{10}'
print('Phone number: ')
find(pattern, text)

#Example 2 : Email
text = "The agent's email is abc@xyz.com"
pattern = '[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com'
print('\nEmail: ')
find(pattern, text)

# Example 3 : URL
text = "The agent's URL is https://www.google.com"
pattern = 'https?://[^\s/$.?#].[^\s]*'
print('\nURL: ')
find(pattern, text)

#Example 4 : Date
text = "The agent's date of birth is 12/12/1990"
pattern = '\d{2}/\d{2}/\d{4}'
print('\nDate: ')
find(pattern, text)

#Example 5 : Name
text = "The agent's name is Mr. Bond"
pattern = 'Mr\.?\s[A-Z]\w*'
print('\nName: ')
find(pattern, text)

# #Example 6 : All
text = "The agent's name is Mr. Potato. The agent's date of birth is 12/12/1990. The agent's email is potato@duck.eu. The agent's phone number is 408-555-1234 or 8783515482. Call soon! The agent's URL is https://www.random.duck"
pattern = 'Mr\.?\s[A-Z]\w*|\d{2}/\d{2}/\d{4}|\d{3}-\d{3}-\d{4}|\d{10}|[a-zA-Z0-9]+@[a-zA-Z0-9]+\.\w+|https?://[^\s/$.?#].[^\s]*'
print('\nAll: ')
find(pattern, text)