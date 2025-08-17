# Student Score Tracker
# asking user for user for the student name and score
student_names = input("Enter three student name seperated by space: ").split(" ")
student_score = []
student_score.append(int(input(f"Enter {student_names[0]} score: ")))
student_score.append(int(input(f"Enter {student_names[1]} score: ")))
student_score.append(int(input(f"Enter {student_names[-1]} score: ")))
print(f"\nName\tScore\n{student_names[0]}\t{student_score[1]}\n{student_names[1]}\t{student_score[0]}\n{student_names[-1]}\t{student_score[-1]}")