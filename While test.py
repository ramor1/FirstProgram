got_answer=False
while not(got_answer):
    buffer=raw_input("What's your name?")
    if buffer.isalpha():
        got_answer=True
print("Hello " + buffer.capitalize())
