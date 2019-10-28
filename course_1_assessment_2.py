#There is a function we are providing in for you in this problem called square. It takes one integer and returns the square of that integer value. Write code to assign a variable called xyz the value 5*5 (five squared). Use the square function, rather than just multiplying with *.
xyz = 25

squared = square(xyz)
print(squared)

#Write code to assign the number of characters in the string rv to a variable num_chars.
rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

num_chars = 0
for i in rv:
    num_chars = num_chars + 1



#(This is not an assessment question) The code below defines functions used by one of the questions above. Do not modify the code, but feel free to take a look.

def square(num):
    return num**2
