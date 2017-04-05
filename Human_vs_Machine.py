#
# HUMAN VS MACHINE?!
#
# Person or machine?  The rps-string challenge...
# This code looks into see if a string (in the rps.csv file) is human made or computer made
#

"""
Short description of (1) the features you compute for each rps-string and 
      (2) how you score those features and how those scores relate to "humanness" or "machineness"

My program first runs read_data, which takes in the rps.csv file, and outputs all of the strings into a list
Then, it sees if s, r or p are repeated 3 times, and if so, adds one to a dictionary
Next, it adds all items of the dictionary to get a score that sees how many of the strings had 3 repeating strings
If the score is over 18, then the string is machineness, and is made my a computer. Else, it's made by a human. I 
came up with this algorithm, because computer generated scores are more likely to have 3 in a row. So, when there are
19 or more instances of 3-in a row, this algorithm believes it is comp-generated.

According to my file, the extra string in rps.csv is computer genereated.





"""


# Here's how to machine-generate an rps string.
# You can create your own human-generated ones!

import random
import csv

def gen_rps_string( num_characters ):
    """ return a uniformly random rps string with num_characters characters """
    result = ''
    for i in range( num_characters ):
        result += random.choice( 'rps' )
    return result

# Here are two example machine-generated strings:
rps_machine1 = gen_rps_string(200)
rps_machine2 = gen_rps_string(200)
# print those, if you like, to see what they are...




from collections import defaultdict

#
# extract_features( rps ):   extracts features from rps into a defaultdict
#
def extract_features( rps ):
    """ This counts the numnber of 3 in a row repeating r's s's and p's
    """
    d = defaultdict( float )  # other features are reasonable

    num_repeat_r = 0
    num_repeat_p = 0
    num_repeat_s = 0


    for i in range(len(rps)-3):
        if rps[i] == 'r' and rps[i+1] == 'r' and rps[i+2] == 'r':
            num_repeat_r += 1
        
        if rps[i] == 'p' and rps[i+1] == 'p' and rps[i+2] == 'p':
            num_repeat_p += 1
            
        if rps[i] == 's' and rps[i+1] == 's' and rps[i+2] == 's':
            num_repeat_s += 1
            
    
    d['s'] = num_repeat_r
    #print("the num of r repeats is " + str(num_repeat_r))
    
    d['p'] = num_repeat_p
    #print("the num of p repeats is " + str(num_repeat_p))

    d['r'] = num_repeat_s
    #print("the num of s repeats is " + str(num_repeat_s))

    return d





#
# score_features( dict_of_features ): returns a score based on those features
#

#how do you know what number makes it human vs not? Is it random?
def score_features( dict_of_features ):
    """ 
    Takes in a dictionary with numbers from above. Since computers are more likely to have 3 in a row repeats.
    if the numnber of 3-in a row repeats are higher than 100, my algorithm believes its human generated.
    """
    d = dict_of_features
    
    s_score = d['s']
    r_score = d['r']
    p_score = d['p']

    total_score = s_score + r_score + p_score
    print(total_score)

    if total_score > 18:
        return("This string was computer-generated")
    else:
        return("This string was human-generated")



#
# read_data( filename="rps.csv" ):   gets all of the data from "rps.csv"
#

#should this be a list of lists? or a list of strings
def read_data( filename="rps.csv" ):
    """ 
    This will take in the filename, and will then return a list of each of the rows, in strings
    """
    try:
        csvfile = open( filename, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row[3] )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []



def write_to_csv(filename = "rps copy.csv" ):
    """
    Writing the scores to the csv file
    """
    csvfile = open( filename, 'wb' )
    filewriter = csv.writer( csvfile )
        
    file_name = read_data()
    for i in range(len(file_name)):

        num_dic = extract_features(file_name[i])
        score = score_features(num_dic)
            
        filewriter.writerow( score )
    
    csvfile.close()


def main():
    """
    This runs the program-
    1. Reads the CSV file and takes in the strings, and outputs them as a list
    2. For each string in the list, counts the number of times r p or s is repeated 3 times
    3. Scores the string, and based on the score being more than 18, determines if it is a comp generated or human
    """
    file_name = read_data()

    comp_gen = 0
    human_gen = 0

    for i in range(len(file_name)):
            
        extract_num = extract_features(file_name[i])
        true_score = score_features(extract_num)
            
        print(true_score)
        if true_score == "This string was computer-generated":
            comp_gen += 1
        else:
            human_gen += 1
    #write_to_csv()
    return("The number of comp generated files is " + str(comp_gen) + " and the number of human generated is " + str(human_gen))
            

def batch_play(rps1, rps2):
    """
    Plays rock paper sisscors against 2 strings
    """
    rps_string1 = 0
    rps_string2 = 0

    for i in range(len(rps1)):
        if rps1[i] == 'r' and rps2[i] == 'p':
            rps_string2 += 1
        elif rps1[i] == 'r' and rps2[i] == 's':
            rps_string1 += 1 
        elif rps1[i] == 's' and rps2[i] == 'p':
            rps_string1 += 1
        elif rps1[i] == 's' and rps2[i] == 'r':
            rps_string2 += 1
        elif rps1[i] == 'p' and rps2[i] == 'r':
            rps_string1 += 1
        elif rps1[i] == 'p' and rps2[i] == 's':
            rps_string2 += 1
    
    print("the number of wins for the first string is " + str(rps_string1))
    print("the number of wins for the second string is " + str(rps_string2))
    
    if rps_string1 > rps_string2:
        return 1
    elif rps_string2 > rps_string1:
        return 2
    else:
        return 0

#
# you'll use these three functions to score each rps string and then
#    determine if it was human-generated or machine-generated 
#    (they're half and half with one mystery string)

# According to the my algorithm, the extra one was computer generated.
#
