import random
import string

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
symbols=string.punctuation

password=lower+upper+digits+symbols
length=input("Enter the length of the password")
random.sample(password,length)