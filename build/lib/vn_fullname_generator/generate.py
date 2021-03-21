import random
import time


firstname_filename = "first.name"
male_filename = "male.name"
female_filename = "female.name"


from importlib import resources

# ...     alice = fid.readlines()

def read_file(filename):
    # with open(filename, 'r') as f:
    with resources.open_text("vn_fullname_generator.data", filename) as f:
        data = f.read().split("\n")

    return data


firstnames = read_file(firstname_filename)
malenames = read_file(male_filename)
femalenames = read_file(female_filename)


def generate_fullname(gender):
    if gender: # man
        fullname = "{} {}".format(random.choice(firstnames), random.choice(malenames))
        
    else:
        fullname = "{} {}".format(random.choice(firstnames), random.choice(femalenames))
    
    return fullname

# generate_fullname(random.getrandbits(1))
