from collections import defaultdict


grades_dict = {"Italo": [8, 9, 10], "Antonio": [7, 6, 5], "Javier": [10, 10, 10]}

def calculate_average_student(student_grades: dict) -> dict:
    average_grades = {}
    for student, grades in student_grades.items():
        if any(isinstance(grade, str) for grade in grades):
            return None
        
        if any(grade < 0 for grade in grades):
            return None
        
        average = sum(grades) / len(grades)
        average_grades[student] = average
    
    return average_grades


def calculate_class_average(student_grades: dict) -> float:
    total_grades = 0
    total_students = len(student_grades)
    
    for grades in student_grades.values():
        if any(isinstance(grade, str) for grade in grades):
            return None
        
        if any(grade < 0 for grade in grades):
            return None
        
        total_grades += sum(grades)
    
    class_average = total_grades / (total_students * len(grades))
    return class_average


average_scores = calculate_average_student(grades_dict)
class_average = calculate_class_average(grades_dict)
