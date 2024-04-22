
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

def read_input(file_path):
    rounds = []
    with open(file_path, 'r') as file:
        for line in file:
<<<<<<< HEAD
            shape, outcome = line.strip().split()
            rounds.append((shape, outcome))
    return rounds

def calculate_score(rounds):
    # Define scores for each shape and outcome directly
    scores = {
        ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7
    }
    
    # Initialize score to 0
    score = 0
    # Iterate through each round
    for shape, outcome in rounds:
        # Get the score from the predefined scores
        shape_score = scores[(shape, outcome)]
        # Add the shape score to the total score
        score += shape_score

    return score

# Main program
file_path = "input_7_cap1.txt"  # Replace with the path to your input file
rounds = read_input(file_path)
total_score = calculate_score(rounds)
print("Total Score:", total_score)

=======
            shape, outcome = line.strip().split()  # Split line into shape and outcome
            score = scores[shape] + outcomes[outcome]  # Calculate score for the round
            total_score += score  # Add round score to total score
        
    return total_score
>>>>>>> 56ae473e361d701643757c17e3de4d681073c3b7


<<<<<<< HEAD
=======
if __name__ == "__main__":
    main()
>>>>>>> 56ae473e361d701643757c17e3de4d681073c3b7
