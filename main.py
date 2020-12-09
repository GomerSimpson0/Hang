import os
import random as rand
import sys

words = ['action', 'activity', 'age', 'air', 'area', 'authority', 'bank', 'body', 'book', 'building', 'business', 'car', 'case', 'centre', 'century',
        'child', 'city', 'community', 'company', 'condition', 'country', 'course', 'court', 'day', 'discussion', 'development', 'door',
        'education', 'effect', 'end', 'example', 'experience', 'eye', 'face', 'fact', 'family', 'father', 'fiel', 'figure', 'food', 'form', 'friend',
        'game', 'girl', 'government', 'group', 'guy', 'hand', 'head', 'health', 'history', 'home', 'hour', 'house', 'idea', 'industry', 'information',
        'interest', 'job', 'kid', 'language', 'law', 'level', 'life', 'line', 'man', 'manager', 'manner', 'market', 'million', 'mind', 'minister',
        'minute',  'moment', 'money', 'month', 'morning', 'mother', 'name', 'need', 'night', 'number', 'office', 'opportunity', 'order', 'paper', 'parent',
        'part', 'party', 'people', 'period', 'person', 'place', 'plan', 'point', 'police', 'position', 'power', 'president', 'price', 'problem',
        'process', 'program', 'project', 'quality', 'question', 'rate', 'reason', 'relationship', 'report', 'result', 'right', 'road',
        'room', 'school', 'sense', 'service', 'side', 'society', 'staff', 'story', 'street', 'student', 'study', 'support', 'system', 'table',
        'teacher', 'team', 'term', 'thing', 'time', 'type', 'use', 'view', 'war', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']

print('Hello, now we will play the game "Hang"')
print("Do you know rules?")
cache = input("\nInput your choise(yn): ")
if cache == 'n':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Rules:\n")
    print("Сomputer guesses a word, and you will guess this word")
    print("You will be given 6 attempts")
    input("\nPress enter to continue...")
os.system('cls' if os.name == 'nt' else 'clear')

cache = int(len(words))
cache = rand.randint(0, cache)
boof = str(words[cache])
del cache
cache = []

tmp3 = False

for i in range(100):
    tmp2 = False
    print('Word: ', end = '')
    for j in range(len(boof)):
        tmp = False
        for x in range(len(cache)):
            if boof[j] == cache[x]:
                tmp = True
        if tmp == True:
            print(boof[j] + ' ', end = '')
            i = i - 1
        else: 
            print("_ ", end = '')
            tmp2 = True
    del tmp
    if tmp2 == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\nWow, you guess word!")
        print("\nSee you later")
        sys.exit()
    print('\n\n')
    i = 6 - i
    if i == 0: 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You lose\n")
        print('Guessed word: ' + boof)
        sys.exit()
    elif i == 1: print('You have 1 attempt\n')
    else: print('You have ' + str(i) + ' attempts\n')
    if tmp3 == True:
        print("Entered letters: ", end = '')
        for j in cache: print(j + '  ', end = '')
        print("\n")
    cache.append(input("\nInput letter: "))
    os.system('cls' if os.name == 'nt' else 'clear')
    tmp3 = True
