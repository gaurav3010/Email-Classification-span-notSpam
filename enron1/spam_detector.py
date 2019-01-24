import pickle
import os
from sklearn import *
from collections import Counter

def make_dict():
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
    return dictionary.most_common(3000)

with open("spam_classifier.pkl", "rb") as rf:
    classifier = pickle.load(rf)
    
dic = make_dict()

while True:
    features = []
    words = []
    email = input(">")
    if email == "exit":
        break
    words = email.split(" ")

    for entry in dic:
        features.append(words.count(entry[0]))
    #print(features)

    result = classifier.predict([features])

    print(["Not Spam", "Spam"][result[0]])
