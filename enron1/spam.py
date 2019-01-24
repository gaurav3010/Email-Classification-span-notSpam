import os
from collections import Counter

dir = "emails/"
files = os.listdir(dir)
#print(files)

emails = [dir + email for email in files]
#print(emails)

words = []
c = len(emails)
for email in emails:
    f = open(email, errors='ignore')
    blob = f.read()
    words += blob.split(" ")
    print(c)
    c -= 1 

for i in range(len(words)):
    if not words[i].isalpha():
        words[i] = "" 

dictionary = Counter(words)
del(dictionary[""])
print(dictionary.most_common(100))