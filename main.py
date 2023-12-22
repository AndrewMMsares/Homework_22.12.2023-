# Task 1
# print("Hello user")
# string = input("Please enter string: ")
# letter = 0
# digit = 0
# try:
#     for i in string:
#         if i.isalpha():
#             letter += 1
#         elif i.isdigit():
#             digit += 1
# except Exception as error:
#     print()
#
# print("Letter: ", letter)
# print("Digit: ", digit)

# Task 2
# print("Hello user")
# string = input("Please enter string: ")
# search = input("Please enter letter: ")
#
# count = 0
#
# for i in string:
#     if i == search:
#         count += 1
#
# print("symbol: ", search, "\nmeets: ", count)


# Task 3.1
# string = input("Enter the line ")
# word = input("Enter a word to search for: ")
# replace_word = input("Enter a replacement word: ")
#
# string2 = string.replace(word, replace_word)
#
# print(string2)


# Task 3.2
# string = input("Enter the line ")
# word = input("Enter a word to search for: ")
# replace_word = input("Enter a replacement word: ")
#
# words = string.split()
#
# for i in range(len(words)):
#     if words[i] == word:
#         words[i] = replace_word
#
# last_string = ' '.join(words)
# print(last_string)


# Task 4
# string = input("Enter the line ")
# print(string[2])
# print(string[-2])
# print(string[:5])
# print(string[::2])
# print(string[1::2])
# print(string[::-1])
# print(string[::-2])

# Task 5
# input_text = input("Enter the line ")
#
# sentences = input_text.split('. ')
# processed_text = '. '.join(sentence.capitalize() for sentence in sentences)
#
# digit = sum(c.isdigit() for c in input_text)
# punctuation = sum(c in ',.?!;:-()"\'[]{}' for c in input_text)
# exclamation = input_text.count('!')
#
# print("Changed text:")
# print(processed_text)
#
# print("\nThe number of digits in the text:", digit)
# print("The number of punctuation marks in the text:", punctuation)
# print("The number of exclamation marks in the text:", exclamation)