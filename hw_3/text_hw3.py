text = "Lorem Ipsum is simply dummy text of the printing and typesetting" \
 "industry. Lorem Ipsum has been the industry's standard dummy text ever" \
"since the 1500s, when an unknown printer took a galley of type and scrambled"\
"it to make a type specimen book. It has survived not only five centuries, but" \
"also the leap into electronic typesetting, remaining essentially unchanged." \
"It was popularised in the 1960s with the release of Letraset sheets containing" \
"Lorem Ipsum passages, and more recently with desktop publishing software like" \
"Aldus PageMaker including versions of Lorem Ipsum."
letter = input("enter letter ")

letter_up = letter.capitalize()
letter_low = letter_up.lower()

res = letter_low or letter_up
word_counter = 0

for word in text.split():
    if res in word:
       word_counter += 1
result = {letter: word_counter}

print(result)
