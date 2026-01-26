# sandwich.py

def sandwich(text):
    print('-' * len(text))
    print(text)
    print('-' * len(text))

text = input('What text do you want to sandwich? ')
sandwich(text)