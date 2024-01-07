# Regular Expressions
A regular expression, often abbreviated as regex, is a sequence of characters that forms a search pattern. In Python, the `re` module provides support for regular expressions. Regular expressions can be used to check if a string contains a specified search pattern.
<br><br>
In Natural Language Processing (NLP), regular expressions are used for text cleaning and text manipulation tasks. Here are a few examples:

1. **Tokenization**: Regular expressions can be used to split a sentence into tokens. For example, you can use the `re.split()` function to split a sentence into words.

2. **Removing unwanted characters**: Regular expressions can be used to remove unwanted characters from a text. For example, you can use the `re.sub()` function to remove all non-alphabetic characters from a text.

3. **Finding specific patterns**: Regular expressions can be used to find specific patterns in a text. For example, you can use the `re.findall()` function to find all email addresses in a text.

Here's an example of how you can use regular expressions in Python:

```python
import re

# Define a regular expression pattern for an email address
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Define a text
text = "My email address is example@example.com"

# Use the re.findall() function to find all email addresses in the text
matches = re.findall(pattern, text)

# Print the matches
print(matches)  # Output: ['example@example.com']
```

In this example, the regular expression pattern `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b` is used to find all email addresses in the text. The `re.findall()` function returns a list of all matches.