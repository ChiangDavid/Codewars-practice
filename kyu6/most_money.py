# You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:

# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
# As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".

# Notes:

# Each student will have a unique name
# There will always be a clear winner: either one person has the most, or everyone has the same amount
# If there is only one student, then that student has the most money

#Mine:
def most_money(students):
    if len(students) == 1:
        return students[0].name
    # NOTE: the Student class is preloaded
    # for all the students in list using index
    #Calculate total money
    total = 0
    max_total = 0
    each_total = []
    max_total_person = ""
    for person in range(len(students)):
        #calculate each person's total amount
        total = (students[person].fives * 5) +  (students[person].tens * 10) + (students[person].twenties * 20)
        each_total.append(total)
        if total > max_total:
            max_total_person = students[person].name
            max_total = total
            
        
    if len(set(each_total)) == 1:
        return "all" 
    else:
        return max_total_person
    pass
#Other method by using dictionary
def most_money(students):
    if len(students) == 1:
        return students[0].name
    
    moneys = {}
    max_amount = 0
    
    for student in students:
        total = student.fives * 5 + student.tens * 10 + student.twenties * 20
        moneys[total] = student.name
        max_amount = max(total, max_amount)
        
    if len(moneys) == 1:
        return "all"
    return moneys[max_amount]
