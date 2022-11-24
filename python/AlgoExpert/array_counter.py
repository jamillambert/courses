"""From a demo interview off youtube

The task is to set up two functions, the first takes in an array of strings
and does as much work as possible so that the second function is as efficient
as possible.

The second function takes a string as an argument, with possible * wildcard
characters, and returns True or False if the word is in the original list"""

def setup(word_array):
    # creates a dictionary to store the entered array for fast lookup
    word_dict = {}
    for word in word_array:
        if word[0] not in word_dict:
            word_dict[word[0]] = {}
        sub_dict = word_dict[word[0]]
        for i in range(1, len(word)):
            if word[i] not in sub_dict:
                sub_dict[word[i]] = {}
            sub_dict = sub_dict[word[i]]        
    return word_dict



def exists(word, word_dict):
    # searches the dictionary and returns True if word is in it
    sub_dict = word_dict
    for i in range(len(word)):
        if word[i] == '*':
            #check all entries on in sub_dict
            in_dict = False
            for key in sub_dict:
                in_dict = in_dict or exists(word[i+1:], sub_dict[key])
            return in_dict
        else:
            if word[i] in sub_dict:
                sub_dict = sub_dict[word[i]]
                continue
            else:
                return False
    return True
        
    
    
word_dict = setup(["bob", "bill", "alice", "alibe", "alidd"])
 
print(exists("alice", word_dict))
print(exists("Alice", word_dict))
print(exists("bob", word_dict))
print(exists("ali*e", word_dict))
print(exists("g***e", word_dict))
print(exists("a***e", word_dict))
