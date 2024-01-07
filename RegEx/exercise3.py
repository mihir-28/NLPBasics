'''
Companies in europe reports their financial numbers of semi annual basis and you can have a document like this. Write a RegEx to extract quarterly and semi annual period.
'''

import re

text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion. BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern = 'FY(\d{4} (Q[1-4]|S[1-2])) .*? (\$\d+(?:\.\d+)? billion)'
match = re.findall(pattern, text)
for m in match:
    print(f'Period: {m[0]}, Cost: {m[2]}')