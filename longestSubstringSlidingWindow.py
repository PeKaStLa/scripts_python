# The Longest Substring of Unique Characters
# Task: Write a function longest_unique_substring(s) that takes a string s and
# returns the length of the longest substring that contains no repeating characters
#

print("start")
    
def longest_unique_substring(s):
    current_substring = ""
    longest_substring = ""

    if s == "":
         return len(longest_substring)

    for ch in s:
        while ch in current_substring:
            current_substring = current_substring[1:]
        if ch not in current_substring:
            current_substring = current_substring + ch
            if len(current_substring)>=len(longest_substring):
                longest_substring = current_substring
            #print("longest_substring: ", longest_substring, "current_substring: ", current_substring)
   
    print("longest_substring: ", longest_substring)
    return len(longest_substring)

def testing(string, real_length):
    test_length = longest_unique_substring(string)
    if test_length == real_length:
        print("Erfolgreicher Test für", string, "Länge:", real_length)
    else:
        print("ERROR: string: ", string, "gave test_length:", test_length, "instead of real length:", real_length)

testing("qweüoietjihasdfbyvöjsdgüuqwrupoasfdhköyxcbnasdfkhlqwpruoö", 19)
testing("asdfghikljaqwertzum", 18)
testing("abcabcbb", 3)
testing("abba", 2)
testing("dvdf", 3)
    
print("end")

