# # Candidate Eligibility
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))
# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
# """The code is used to confirm the eligibility of a candidate below 18 years of age and if they met the required score mark for the scholarship """ 

# Fedral Government Schorlarship Key Eligibility Requirement 
citizenship = input("Are you a citizen of Nigeria?\nYes or No: ").title
enrollment = input("Are you registered as a full-time undergraduate student in a recognized nigerian university?\nYes or No: ").title
other_scholarships = input("Are you receiving any other scholarship from an entity in the Oil and Gas industry, whether national or internaltional?\nYes or No: ").title
academic_qualification = input("Do yoy have five distinctions (As and Bs) in your WAEC/WASSCE exams including English and Mathematics?\nYes or NO: ").title
eligibility = (citizenship == "Yes") and (enrollment == "Yes") and (other_scholarships == "No") and (academic_qualification == "Yes")
print(f"Dear Candidate\nEligible: {eligibility}")