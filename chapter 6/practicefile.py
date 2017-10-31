# print("Hello World")
# letter_count = 0
#  Printing letter count
# for letter in "hello world":
#     print(letter_count,':', letter)
#     letter_count = letter_count + 1
# print("This is third example")
#
# my_str = "Hello World"
# print(my_str[0])


#  printing string using while loop
# my_str = "Pakistan"
# index = 0
# while index < len(my_str):
#     letter = my_str[index]
#     print(index, ':', letter)
#     index = index + 1

# Second example of printing a string using the while loop
# my_str2 = "Hello World This is my country Pakistn"
# index = 0
# while index < len(my_str2):
#     letter = my_str2[index]
#     print(index, ':', letter)
#     index = index + 1

# third example using while loop to print a string

# my_str3 = "This is the third string"
# index = 0
# while index < len(my_str3):
#     letter = my_str3[index]
#     print(index, ':', letter)
#     index = index+1

# I want to print only chartacter which appears in a string a skip the space
# my_str4 = "This is my world of imagination."
# index = 0
# while index < len(my_str4)-1:
#     letter = my_str4[index]
#     if letter is not " ":
#         print(index, ':', letter)
#     index = index +1

# I want to know how many "a"s are in a given string
my_str5 = "Hello World, how are you"
letter_count = 0
for letter in my_str5:
    if letter == 'a':
        letter_count = letter_count + 1
if letter_count > 0:
    print("Your string contains:", letter_count)
else:
    print("No 'A(s)'were found")



