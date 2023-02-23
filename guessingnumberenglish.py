import random
upper_bond=100

random.randint(0, upper_bond)                                                                                           #random. randient generiet numbers 0 is the initial value upperbond is the final value and is separated with ",".
                                                                                                                        # upperbond upper limit
secret_number = random.randint(0, upper_bond)                                                                           # Secret number is a variable I can use later.

print(" A random number between 0 and " + str (upper_bond) + " has just been generated")                                # here str upper_bond is converted into string
print("Your task is to guess which number it is. ")
print("Good luck")


guess = None                                                                                                            # guess is set to zero. a value is taken from the pre-declaration.
count = 1                                                                                                               # count is set to 1 because it is counted high

while guess != secret_number:                                                                                           # That means if guess is not equal to secret_number, run the while loop until it becomes equal to
    guess = int (input (" Select an integer between 0 and " +  str(upper_bond) + ":  "  ))                           # Here guess is caught as a variable for the function.
                                                                                                                        #Here the input is prompted and converted to int because we only work with integers here.


    if guess  == secret_number:
        print("Yeahh, that's correct!")
    elif guess < secret_number:
        print("The number you are looking for is bigger than your guessed number !")
        count = count + 1
    else:
        print("The number you are looking for is smaller than the number you guessed!")
        count = count + 1

print("It took you " + str(count) + " tries to guess the correct number.!")