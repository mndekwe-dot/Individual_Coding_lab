import csv
from datetime import datetime

class Assignment:
    def __init__(self, name, category, grade, weight):
        self.name = name
        self.category = category.upper()
        self.grade = grade
        self.weight = weight
        self.weighted_grade = self.calculate_weighted_grade()

    def calculate_weighted_grade(self):
        return (self.grade/100) * self.weight

    def to_dict(self):
        """Convert assignment to dictionary format"""
        return {
            'name': self.name,
            'category': self.category,
            'grade': self.grade,
            'weight': self.weight,
            'weighted_grade': self.weighted_grade
        }
    
    def __str__(self):
        return f"{self.name} ({self.category}): {self.grade}% - Weight: {self.weight}"
class inputvalidator:
    def __init__(self):
        pass
    def get_valid_grade(self):
        while True:
            try:
                grade = float(input("Grade Obtained (0-100): "))
                if 0 <= grade <= 100:
                    return grade
                else:
                    print("Error: Grade must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid number.")
    
    def get_valid_weight(self):
        while True:
            try:
                weight = float(input("Weight: "))
                if weight > 0:
                    return weight
                else:
                    print("Error: Weight must be a positive number.")
            except ValueError:
                print("Error: Please enter a valid number.")
    
    def get_valid_category(self):
        while True:
            category = input("Category (FA/SA): ").strip().upper()
            if category in ["FA", "SA"]:
                return category
            else:
                print("Error: Category must be 'FA' or 'SA'.")
    
    def get_yes_no_input(self, prompt):
        while True:
            response = input(prompt).strip().lower()
            if response in ['y', 'n']:
                return response
            print("Error: Please enter 'y' or 'n'.")


