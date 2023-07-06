# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.


# List -> looking things up requires you to iterate thru the whole list O(n)
# Dict/Object -> looking things up requires key (Instant) O(1)

def anagrams(s1, s2):
    # First, check for strings' lengths
    if len(s1) != len(s2):
        return False

    #  Initialize a dict to hold the letters present in first string
    count = {}
    for char in s1:
        if char not in count:
            count[char] = 1
        #   count['r'] = 1
        else:
            count[char] += 1

    print('count dict initialized: ', count)

    # Loop thru second string and check each letter with the dict
    for char in s2:
        if char not in count:
            return False
        else:
            count[char] -= 1
            if count[char] < 0:
                return False

    print('count dict after second loop: ', count)
    return True

# # TEST CASES
print(anagrams('restful', 'fluster'))  # -> True
# {
#     'r': 1, -> 0
#     'e': 2, -> 1 -> 0
#     's': 1
# }
# anagrams('cats', 'tocs') # -> False
# print(anagrams('monkeyswrite', 'newyorktimes')) # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# print(anagrams('pp', 'oo')) # -> False
