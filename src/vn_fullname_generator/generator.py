import random
import time
from importlib import resources

firstname_filename = "first.name"
male_filename = "male.name"
female_filename = "female.name"

def read_file(filename):
    # with open(filename, 'r') as f:
    with resources.open_text("vn_fullname_generator.data", filename) as f:
        data = f.read().split("\n")

    return data

firstnames = read_file(firstname_filename)
malenames = read_file(male_filename)
femalenames = read_file(female_filename)


def generate(gender=random.getrandbits(1)):
    if gender: # man
        fullname = "{} {}".format(random.choice(firstnames), random.choice(malenames))
        
    else:
        fullname = "{} {}".format(random.choice(firstnames), random.choice(femalenames))
    
    return fullname
