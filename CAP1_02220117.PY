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
# Your Solution Score: 50259
# Put your number here: 7
################################

def calculate_score(input_file):
    shapes = {'rock': 'A', 'paper': 'B', 'scissors': 'C'} # Mapping the shapes to variables
    scores = {'A': 1, 'B': 2, 'C': 3}  # Mapping the shapes to scores
    outcomes = {'X': 0, 'Y': 3, 'Z': 6}  # Mapping the outcomes to scores
    
    total_score = 0  # Initializing the total score to 0
    
    with open(input_file, 'r') as file:
        for line in file:
            shape, outcome = line.strip().split()  # Split line into shape and outcome
            score = scores[shape] + outcomes[outcome]  # Calculate score for the round
            total_score += score  # Add round score to total score
    
    return total_score

#Reads the input file and calculates the total outcome
def main():
    input_file = "input_7_cap1.txt"  
    total_score = calculate_score(input_file)
    print("\nTotal score:", total_score)

if __name__ == "_main_":
    main()
