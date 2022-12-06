import sys

def initialize_word_list():
    file = "./word_list.txt"
    word_list = []
    for word in open(file):
        word_list.append(word.strip())
    return word_list

def try_word(trial_word, todays_word):
    result = []
    for letter_index in range(0, len(trial_word)):
        if trial_word[letter_index] == todays_word[letter_index]:
            result.append([trial_word[letter_index], 2])
        elif trial_word[letter_index] in todays_word:
            result.append([trial_word[letter_index], 1])
        else:
            result.append([trial_word[letter_index], 0])
    return result
# handle green
def only_keep_words_with_letter_in_position(word_list, letter, position):
    resulting_list = []
    for word in word_list:
        if word[position] == letter:
            resulting_list.append(word)
    return resulting_list
# handle yellow
def only_keep_words_with_letter_but_not_position(word_list, letter, position):
    resulting_list = []
    for word in word_list:
        if letter in word and letter != word[position]:
            resulting_list.append(word)
    return resulting_list
# handle gray
def eliminate_words_that_contain_letter(word_list, letter):
    resulting_list = []
    for word in word_list:
        if letter not in word:
            resulting_list.append(word)
    return resulting_list

def choose_word_to_try(word_list):
    return word_list.pop(0)

def sort_list_optimally(word_list):
    letter_frequency = {}
    for word in word_list:
        for letter in word:
            if letter not in letter_frequency:
                letter_frequency[letter] = 1
            else:
                letter_frequency[letter] += 1
    word_scores = {}
    for word in word_list:
        score = 0
        letter_set = set(word)
        for letter in letter_set:
            score += letter_frequency[letter]
        word_scores[word] = score
    sorted_scores = dict(sorted(word_scores.items(), key=lambda item: item[1], reverse=True)).keys()
    return list(sorted_scores)

wl = initialize_word_list()
wl = sort_list_optimally(wl)
todays_word = sys.argv[1]
word_found = False
counter = 0
while (not word_found):
    counter += 1
    word_to_try = choose_word_to_try(wl)
    print("Trying word: " + word_to_try)
    word_result = try_word(word_to_try, todays_word)
    print("Word result: ")
    print(word_result)
    if word_to_try == todays_word:
        word_found = True
        print("Word found! " + word_to_try + " in " + str(counter) + " tries")
        break
    for index in range(0, len(word_result)):
        if word_result[index][1] == 2:
            wl = only_keep_words_with_letter_in_position(wl, word_result[index][0], index)
        elif word_result[index][1] == 1:
            wl = only_keep_words_with_letter_but_not_position(wl, word_result[index][0], index)
        else:
            wl = eliminate_words_that_contain_letter(wl, word_result[index][0])
    print("remaining possible words: ")
    print(wl)
    if not wl:
        print("Word not in list. No remaining words to try")
        break

        




