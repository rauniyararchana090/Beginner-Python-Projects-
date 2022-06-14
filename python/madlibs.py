#string concatenation(how to put strings together)
from cgi import print_arguments


youtuber="Archana Rauniyar"
print("Subscribe to "+youtuber)
print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}")


adj =input("Adjective: ")
verb1=input("Put ur verb: ")
verb2=input("Put here: ")
famous_person=input("input someone's name:")
matlib=f"Computer programming is so {adj}! it makes me so excited all the time because  \
    I love to {verb1}. Stay hydrated and {verb2} lik you are {famous_person}! "
print(matlib)    