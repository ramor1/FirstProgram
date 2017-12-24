import sys
print sys.argv[0:]

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        elif ok in ('n', 'no', 'nop', 'nope'):
            return False
        else:
            retries = retries - 1
            if retries < 0:
                raise IOError('refusenik user')
            print complaint

height_metres = float(input("What is your height in metres? "))
height_inches = round(height_metres * 39.37)
height_feet = int(height_inches / 12)
height_remain_inches = height_inches - height_feet * 12
print ("You are " + str(height_feet)
       + "\' "
       + str(int(height_remain_inches))
       + '\" tall.')
test=ask_ok("Do you want to quit")
if test:
    print("He wants out")
else:
    print("He wants to stick around")


