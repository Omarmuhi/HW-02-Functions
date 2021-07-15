Enter_test_score: 75
Enter_test_score: 85
Enter_test_score: 95

Your_Scores:   75/85/95
Total_Score:   255
Average_Score: 85

#display title
print()
print("Test Scores Program")
print("You will be prompted to Enter 3 test scores below.")
print()
print("====================")

#get scores from the user and sum the total
score_01=int(input("Enter Test Score: "))
score_02=int(input("Enter Test Score: "))
score_03=int(input("Enter Test Score: "))
total_score=score_01+score_02+score_03

#calculate average score
average_score=round(total_score / 3)

# format and display the result
print("====================")
print(f'Yours Scores:\t {score_01} {score_02} {score_03}')
print(f'Total Score:\t {total_score}')
print(f'Average Score:\t {average_score}')
print()
print('End of Program.')