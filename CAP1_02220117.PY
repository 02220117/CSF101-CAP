
################################

# Your Name:Kencho Zangmo
# Your Section:ECE
# Your Student ID Number:02220117
################################
# REFERENCES
# https://www.programiz.com/python-programming/file-operation
# https://stackoverflow.com/questions/32293947/assistance-on-python-rock-paper-scissors-using-input-file
# the problem
# 
################################
# SOLUTION
# Your Solution Score: 50169
# Put your number here: 7
################################

def input(file):
    all_rounds = []
    with open(file, 'r') as file:
        for line in file:
            shape, outcome = line.strip().split()
            all_rounds.append((shape, outcome))
    return all_rounds

def score_calculated(all_rounds):
    # Defining the scores for the shapes and outcomes
    scores = {
        ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7
    }
    
    # Initializing the score to zero
    score = 0
    # Iterating through each round
    for shape, outcome in all_rounds:

        shape_score = scores[(shape, outcome)]

        score += shape_score

    return score

#Calcuting the score in the file
file = "input_7_cap1.txt"  
all_all_rounds = input(file)
total_score = score_calculated(all_all_rounds)
print("Total Score:", total_score)



