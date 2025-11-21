import csv
from datetime import datetime

class Assignment:
    """Represents a single assignment with grade and weight"""
    
    def __init__(self, name, category, grade, weight):
        self.name = name
        self.category = category.upper()
        self.grade = grade
        self.weight = weight
        self.weighted_grade = self.calculate_weighted_grade()
    
    def calculate_weighted_grade(self):
        """Calculate the weighted grade for this assignment"""
        return (self.grade / 100) * self.weight
    
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


class InputValidator:
    """Handles all input validation logic"""
    
    def __init__(self):
        pass
    
    def get_valid_grade(self):
        """Get a valid grade between 0-100"""
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
        """Get a valid positive weight"""
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
        """Get a valid category (FA or SA)"""
        while True:
            category = input("Category (FA/SA): ").strip().upper()
            if category in ["FA", "SA"]:
                return category
            else:
                print("Error: Category must be 'FA' or 'SA'.")
    
    def get_yes_no_input(self, prompt):
        """Get a valid yes/no input"""
        while True:
            response = input(prompt).strip().lower()
            if response in ['y', 'n']:
                return response
            print("Error: Please enter 'y' or 'n'.")


class GradeCalculator:
    """Handles all grade calculations and analysis"""
    
    def __init__(self):
        self.assignments = []
    
    def add_assignment(self, assignment):
        """Add an assignment to the calculator"""
        self.assignments.append(assignment)
    
    def get_category_total(self, category):
        """Calculate total weighted grade for a specific category"""
        return sum(a.weighted_grade for a in self.assignments if a.category == category)
    
    def get_category_weight(self, category):
        """Calculate total weight for a specific category"""
        return sum(a.weight for a in self.assignments if a.category == category)
    
    def calculate_final_grade(self):
        """Calculate the final grade (sum of all weighted grades)"""
        return sum(a.weighted_grade for a in self.assignments)
    
    def calculate_gpa(self):
        """Calculate GPA out of 5.0"""
        final_grade = self.calculate_final_grade()
        return (final_grade / 100) * 5.0
    
    def determine_status(self):
        """Determine pass/fail status and assignments to resubmit"""
        total_fa = self.get_category_total('FA')
        total_sa = self.get_category_total('SA')
        total_fa_weight = self.get_category_weight('FA')
        total_sa_weight = self.get_category_weight('SA')
        
        fa_threshold = total_fa_weight * 0.5
        sa_threshold = total_sa_weight * 0.5
        
        passed = True
        resubmit = []
        
        if total_fa_weight > 0 and total_fa < fa_threshold:
            passed = False
            resubmit.append("Formative Assessments")
        
        if total_sa_weight > 0 and total_sa < sa_threshold:
            passed = False
            resubmit.append("Summative Assessments")
        
        return passed, resubmit
    
    def get_summary(self):
        """Generate a summary dictionary of all calculations"""
        passed, resubmit = self.determine_status()
        return {
            'total_assignments': len(self.assignments),
            'formative_total': self.get_category_total('FA'),
            'formative_weight': self.get_category_weight('FA'),
            'summative_total': self.get_category_total('SA'),
            'summative_weight': self.get_category_weight('SA'),
            'final_grade': self.calculate_final_grade(),
            'gpa': self.calculate_gpa(),
            'passed': passed,
            'resubmit': resubmit
        }


class ReportGenerator:
    """Handles output generation and file exports"""
    
    def __init__(self):
        pass
    
    def print_summary(self, summary):
        """Print formatted summary to console"""
        print("\n" + "=" * 50)
        print("GRADE SUMMARY")
        print("=" * 50)
        print(f"\nTotal Assignments: {summary['total_assignments']}")
        print(f"\nFormative Total: {summary['formative_total']:.2f} / {summary['formative_weight']:.2f}")
        print(f"Summative Total: {summary['summative_total']:.2f} / {summary['summative_weight']:.2f}")
        print(f"\nFinal Grade: {summary['final_grade']:.2f}%")
        print(f"GPA: {summary['gpa']:.2f} / 5.0")
        print(f"Status: {'PASS' if summary['passed'] else 'FAIL'}")
        
        if not summary['passed']:
            print(f"Assignments to Resubmit: {', '.join(summary['resubmit'])}")
        
        print("=" * 50)
    
    def export_to_csv(self, assignments, filename='grades.csv'):
        """Export assignments to CSV file"""
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Assignment', 'Category', 'Grade', 'Weight'])
            
            for assignment in assignments:
                writer.writerow([
                    assignment.name,
                    assignment.category,
                    assignment.grade,
                    assignment.weight
                ])
        
        print(f"\n✓ Data exported to {filename}")


class GradeGeneratorApp:
    """Main application class that coordinates all components"""
    
    def __init__(self):
        self.calculator = GradeCalculator()
        self.validator = InputValidator()
        self.reporter = ReportGenerator()
    
    def display_welcome(self):
        """Display welcome message"""
        print("=" * 50)
        print("GRADE GENERATOR CALCULATOR")
        print("=" * 50)
        print()
    
    def collect_assignment_data(self):
        """Collect data for a single assignment"""
        print("\n--- Enter Assignment Details ---")
        
        name = input("Assignment Name: ").strip()
        category = self.validator.get_valid_category()
        grade = self.validator.get_valid_grade()
        weight = self.validator.get_valid_weight()
        
        return Assignment(name, category, grade, weight)
    
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        # Collect assignments
        while True:
            assignment = self.collect_assignment_data()
            self.calculator.add_assignment(assignment)
            
            add_more = self.validator.get_yes_no_input("\nAdd another assignment? (y/n): ")
            
            if add_more == 'n':
                break
        
        # Generate and display summary
        summary = self.calculator.get_summary()
        self.reporter.print_summary(summary)
        
        # Export to CSV
        self.reporter.export_to_csv(self.calculator.assignments)


def main():
    """Entry point of the application"""
    app = GradeGeneratorApp()
    app.run()


if __name__ == "__main__":
    main()