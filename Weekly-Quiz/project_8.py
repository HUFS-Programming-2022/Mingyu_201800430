"""
Content:
"""
text = input().lower()
final_dict = {letter: text.count(letter)*letter.split() for letter in set(text) if letter.isalpha()}
print(final_dict)