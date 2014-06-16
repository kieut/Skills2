string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    dictionary = {}
    words = string1.split(" ")

    i = 0
    for i in words:
        dictionary[i] = dictionary.setdefault(i, words.index(i)) + 1
    print dictionary

# count_unique(string1)

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""

def common_items(list1, list2):
    common_items_list = []

    for num in list1:
        for num2 in list2:
            if num == num2 and num not in common_items_list:
                common_items_list.append(num)
    
    print common_items_list

    # This solution loops through indices.
    # match_list = []

    # for index1 in range(0, len(list1)):
    #     for index2 in range(0, len(list2)):
    #         if list1[index1] == list2[index2] and list1[index1] not in match_list:
    #             match_list.append(list1[index1])
    # print match_list

# common_items(list1, list2)


"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    match_dict = {}
    match_list = []

    # loop through indices of list1 against list2, if number in common, add to dict.

    for index1 in range(0, len(list1)):
        for index2 in range(0, len(list2)):
            if(list1[index1] == list2[index2]):
                if list1[index1] in match_dict:
                    match_dict[list1[index1]] += 1 #if num is in match dict, add 1 to value
                else:
                    match_dict[list1[index1]] = 1 # if num not in match dict, set value to 1
                       
    for k, v in sorted(match_dict.iteritems()): 
        match_list.append(k)

    print match_dict
    print match_list

common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    # both solutions work

    zero_sum_pairs = []

    for index in range(0, len(list1)):
        for next_index in range(index+1, len(list1)):
            if list1[index] + list1[next_index] == 0:
                    zero_sum_pairs.append((list1[index], list1[next_index]))
    print zero_sum_pairs

    # zero_sum_pairs = []

    # for num in list1:
    #     neg_num = num * -1
    #     if neg_num in list1:
    #         zero_sum_pairs.append((num, neg_num))

    # print zero_sum_pairs

# sum_zero(list1)

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    word_count = {}
    duplicate_list = []

    for word in words:
        word_count[word] = word_count.setdefault(word, 0) + 1

    duplicate_list = word_count.keys()

    print duplicate_list

# find_duplicates(words)


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    word_dict = {}

    # make dictionary of word, word_length pairs
    for word in words:
        word_length = len(word)
        word_dict[word_length] = word_dict.setdefault(word_length, []) + [word]

    # print word_dict
    lengths = word_dict.keys() # returns a list of word_dict keys
    lengths.sort()


    for length in lengths:
        word_dict[length].sort()
        for word in word_dict[length]:
            print word

# word_length(words

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def make_trans_dict(filename):
    word_pairs = {}

    f = open(filename)

    for line in f:
        line = line.rstrip()
        words = line.split()
        word_pairs[words[0]] = words[1]

    for word in word_pairs:
        word_pairs[word] = word_pairs[word].replace('-', ' ')

    return word_pairs

    f.close()

    # print word_pairs

def main():

    word_pairs = make_trans_dict("pirate_trans.txt")
    pirate_translation = []

    input_sentence = raw_input("Type in a sentence for me to translate to Pirate- argh. ")
    input_words = input_sentence.split(" ")

    for word in input_words:
        word = word.strip(".,!?():;")
        # if the input_word doesn't exist in pirate speak, use the input_word
        pirate_word = word_pairs.get(word, word + ' argh')
        pirate_translation.append(pirate_word)

    translated_sentence = " ".join(pirate_translation) + "."

    print translated_sentence


if __name__ == "__main__":
    main()
