names = ["Arash", "Atena", "Ardeshir", "Atoosa"]
scores = [11, 14, 16, 18]

# 1- calculate the average here

score_letters = []
for i in range(len(scores)):
    # 2- letter A for 18 or better
    # letter B for 15 or better
    # letter C for 12 or better
    # letter F for less than 12

print(score_letters)

for i in range(len(scores)):
    match score_letters[i]:
        # 3- use string formatting and match/case
        # to print each student's name and their performance
        # A: Excellent, B: good, C: Need Practice, F: Failed
