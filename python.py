print("WELCOME TO THE QIIZ GAME")
score = 0
#Question 1
print("Question 1: Who is the current president of USA? \n A: Barrack Obama\n B: Elon Musk\n C: Donald Trump\n D: Joe Biden" )
answer1 = input("What is your answer(A, B, C or D): ").upper()
if answer1 == "C":
    score += 1

#Question 2
print("Question 2: What is the highest mountain in the world?\n A: Mount Kilimanjaro\n B: Mount Everest\n C: Mount Kenya\n D: Mount Elgon ")
answer2 = input("What is your answer(A, B , C or D): ").upper()
if answer2 == "B":
    score += 1

#Question 3
print("Question 3: How many continents are there in the world?\n A: 8\n B: 6\n C: 7\n D: 9 ")
answer3 = input("What is your answer(A, B , C or D): ").upper()
if answer3 == "C":
    score += 1

#Question 4
print("Question 4: Which month has 28 days in a normal year?\n A: February\n B: March\n C: August\n D: September ")
answer4 = input("What is your answer(A, B , C or D): ").upper()
if answer4 == "A":
    score += 1

#Question 5
print("Question 5: Which instrument is used to measure temperature?\n A: Barometer\n B: Thermometer\n C: Compass\n D: Stop watch ")
answer5 = input("What is your answer(A, B , C or D): ").upper()
if answer5 == "B":
    score += 1    

if score == 5:
    remark = "That is Excellent"
elif score == 4:
    remark = "That is Very Good"
elif score == 3:
    remark = "That is Good"
elif score == 2:
    remark = "That is a Nice Try"
elif score == 1:
    remark = "Keep Practicing"
else:
    remark = "You will do better next time"       

print("Your total score is",score ,remark)    

