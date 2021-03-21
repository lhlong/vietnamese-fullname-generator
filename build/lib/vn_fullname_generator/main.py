import random
import time

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read().split("\n")

    return data


def generate_fullname(firstnames, malenames, femalenames, gender):
    if gender: # man
        fullname = "{} {}".format(random.choice(firstnames), random.choice(malenames))
        print("Male Name: {}".format(fullname))
        
    else:
        fullname = "{} {}".format(random.choice(firstnames), random.choice(femalenames))
        print("Female Name: {}".format(fullname))
    
    return fullname


def main():
    firstname_filename = "./data/first.name"
    male_filename = "./data/male.name"
    female_filename = "./data/female.name"

    firstnames = read_file(firstname_filename)
    malenames = read_file(male_filename)
    femalenames = read_file(female_filename)

    generate_fullname(firstnames, malenames, femalenames, random.getrandbits(1))

if __name__=="__main__":
    main()
