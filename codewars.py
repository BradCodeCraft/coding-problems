def check_for_factor(base, factor):
    return base % factor == 0;

def get_sum(a,b):
    sum = 0;

    for x in range(min(a,b), max(a,b) + 1):
        sum += x;

    return sum;

def set_alarm(employed, vacation):
    return employed & (not vacation)

def positive_sum(arr):
    sum = 0

    for x in arr:
        if x >= 0: sum+= x

    return sum

def how_much_i_love_you(nb_petals):
    phrases_arr = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    index = (nb_petals % 6) - 1

    return phrases_arr[index]

def shortcut(s):
    vowels_arr = ["a", "e", "i", "o", "u"]
    result_string = ""

    for letter in s:
        if letter in vowels_arr:
            result_string += ""
        else:
            result_string += letter

    return result_string

def find_short(s):
    shortest_length = len(s.split(" ")[0])

    for word in s.split(" "):
        if len(word) < shortest_length:
            shortest_length = len(word)

    return shortest_length

def two_sort(array):
    result_string = ""
    temporary_array = sorted(array)
    first_string = temporary_array[0]

    for letter in first_string:
        result_string += letter + "***"

    return result_string[0 : len(result_string) - 3]

def stray(arr):
    dict = {}

    for x in arr:
        if x in dict.keys():
            dict[x] = dict[x] + 1
        else:
            dict[x] = 1

    for x in dict.keys():
        if dict[x] == 1: return x

def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [1, 15, 15]
    elif human_years == 2:
        return [1, 24, 24]
    else:
        dog_years = 24
        cat_years = 24

        for x in range(3, human_years + 1):
            cat_years += 4
            dog_years += 5

        return [human_years, cat_years, dog_years]

def to_jaden_case(string):
    result_string = ""

    for word in string.split(" "):
        result_string += word.capitalize() + " "

    return result_string[0: len(result_string) - 1]

def make_negative(number):
    return number if number <= 0 else 0 - number

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b

def find_difference(a, b):
    volume_a = 1
    volume_b = 1

    for x in range(0, 3):
        volume_a *= a[x]
        volume_b *= b[x]

    return abs(volume_a - volume_b)

def plural(n):
    return not n == 1

# RANK UP
def rgb(r, g, b):
    hexidecimal_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    r_hex = g_hex = b_hex = ""

    r_hex += hexidecimal_array[int(max(0, r) / 16)] + hexidecimal_array[int(max(0, r) % 16)]
    g_hex += hexidecimal_array[int(max(0, g) / 16)] + hexidecimal_array[int(max(0, g) % 16)]
    b_hex += hexidecimal_array[int(max(0, b) / 16)] + hexidecimal_array[int(max(0, b) % 16)]

    return r_hex + g_hex + b_hex

# SPLIT STRINGS
def solution(s):
    result_array = []
    current_string = ""

    for index in range(0, len(s)):
        current_string += s[index]

        if len(current_string) == 2:
            result_array.append(current_string)
            current_string = ""

    if len(current_string) == 1:
        current_string += "_"
        result_array.append(current_string)

    return result_array

# Sort Numbers
def solutions(nums = []):
    if nums == None or len(nums) == 0:
        return []
    else:
        return sorted(nums)

# Anagram Detection - 7kyu
def is_anagram(test = "", original = ""):
    test = sorted(test.lower())
    original = sorted(original.lower())
    
    if not len(test) == len(original):
        return False

    for x in range(0, len(test)):
        if not test[x] == original[x]:
            return False

    return True

# Grasshopper Messi Goals - 8kyu
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# Playing with digits - 6kyu
def dig_pow(n, p):
    left = 0
    current_exponent = p
    n_string = str(n)

    for num_string in n_string:
        current_num = int(num_string)
        left += (current_num ** current_exponent)
        current_exponent += 1

    result = left / n

    return int(result) if result == int(result) else -1

# Number of People in the Bus
def number(bus_stops):
    result = 0

    for pair in bus_stops:
        result += pair[0] - pair[1]

    return result

# Consecutive strings - 6kyu
def longest_consec(strarr, k):
    if k <= 0:
        return ""
    else:
        current_longest_string = ""
        temporary_k = k - 1

        for index in range(0, len(strarr) - temporary_k):
            current_concat_string = strarr[index]

            while temporary_k > 0:
                index += 1
                current_concat_string += strarr[index]
                temporary_k -= 1
    
            if len(current_concat_string) > len(current_longest_string):
                current_longest_string = current_concat_string

            temporary_k = k - 1

        return current_longest_string

# Abbreviate a Two Word Name
def abbrev_name(name):
    return name[0].upper() + "." + name[name.index(" ") + 1].upper()

# Invert Values
def invert(lst = []):
    return list(map(lambda n: 0 - n, lst))

# Most frequently used words in a text - 4kyu
import re

def top_3_words(text = ""):
    valid_string = "abcdefghijklmnopqrstuvwxyz'"
    valid_characters_array = list(valid_string)
    new_text = ""

    for index in range(len(text)):
        if text[index].lower() in valid_characters_array:
            new_text += text[index]
        else:
    

top_3_words()
