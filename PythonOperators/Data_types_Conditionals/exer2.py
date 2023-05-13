# exercise 2 
#You are developing a program for a teacher to grade their students' exams. 
# The program should prompt the teacher to enter the number of questions on the exam, 
# the number of questions the student answered correctly, and 
# the number of points each question is worth. 
# The program should then calculate the student's grade as a percentage, 
# and print out a message indicating whether the student passed or failed the exam.

# solution:
# Get input from teacher
num_questions =int(input("what is the total number of questions for the exam: "))
num_correct_answers= int(input("what is the number of questions the students answered correctly:"))
points_per_questions =float(input("what is the point worth for each question:"))


#calculate the student number of points ( by multiplying the number of question answers by the point)
total_num_points = num_correct_answers * points_per_questions

# Calculate the maximum number of points earn by students 
max_num_point_earn = num_questions * points_per_questions

#calculate the student score calculated in percentage
total_score= ( total_num_points / num_questions )* 100


# print the conditional statement 
if total_score >=50:
    print("the student pass the exam")
else:
    print("the student fail the exam")
    