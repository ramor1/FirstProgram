got_answer=False
while not(got_answer):
    buffer=input("What's your name?")
    if buffer.isalpha():
        got_answer=True
print("Hello " + buffer.capitalize())
