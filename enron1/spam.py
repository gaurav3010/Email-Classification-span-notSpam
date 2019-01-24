import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

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

def make_dataset(dictionary):
    dir = "emails/"
    files = os.listdir(dir)

    emails = [dir + email for email in files]
    #print(emails)

    feature_set = []
    labels = []
    c = len(emails)

    for email in emails:
        data = []
        f = open(email, errors='ignore')
        blof = f.read()
        words = blof.split(" ")

        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)

        if 'ham' in email:
            labels.append(0)
        if 'spam' in email:
            labels.append(1)
        
        c -= 1
        print(c)

    return feature_set, labels

dic = make_dict()
print(len(dic))

feature, labels = make_dataset(dic)

print(len(feature))
print(len(labels))

#print(feature[3])

X_train, X_test, y_train, y_test = train_test_split(feature, labels, test_size = 0.2)
classifier = MultinomialNB()
classifier.fit(X_train,y_train)

pred = classifier.predict(X_test)
print(accuracy_score(y_test, pred))

with open('spam_classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)

