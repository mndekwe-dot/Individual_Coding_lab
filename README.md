# Lab 1: Grade Generator Calculator

## 📚 Project Description
This project consists of two parts that work together to manage student grade calculations and archive the results:
1. **Python Grade Generator** - An interactive OOP-based application that calculates student grades with validation
2. **Shell Script Organizer** - A Bash script that archives CSV files with timestamps and maintains detailed logs

## 📁 Repository Structure
```
Lab1-{YourGithubUsername}/
├── grade-generator.py    # Python grade calculator (OOP implementation)
├── organizer.sh          # Bash archiving script
└── README.md            # Project documentation
```

After running the scripts:
```
Lab1-{YourGithubUsername}/
├── archive/
│   └── grades-YYYYMMDD-HHMMSS.csv
├── grade-generator.py
├── organizer.sh
├── organizer.log
└── README.md
```

---

## 🐍 Part 1: Python Grade Generator

### Features
- ✅ **Object-Oriented Design** with 5 classes
- ✅ **Interactive Input Collection** with comprehensive validation
- ✅ **Automatic Grade Calculations** (weighted grades, GPA)
- ✅ **Pass/Fail Determination** based on 50% threshold for both categories
- ✅ **Formatted Console Output** with detailed summary
- ✅ **CSV Export** for data persistence

### Class Architecture

#### 1. **Assignment Class**
- Represents individual assignments
- Automatically calculates weighted grades
- Provides dictionary and string representations

#### 2. **InputValidator Class**
- Validates grade input (0-100 range)
- Validates category input (FA/SA only)
- Validates weight input (positive numbers)
- Handles yes/no prompts with error handling

#### 3. **GradeCalculator Class**
- Manages collection of assignments
- Calculates category totals and weights
- Computes final grade and GPA (out of 5.0)
- Determines pass/fail status
- Identifies assignments requiring resubmission

#### 4. **ReportGenerator Class**
- Prints formatted summary to console
- Exports assignment data to CSV file
- Handles all output operations

#### 5. **GradeGeneratorApp Class**
- Main coordinator orchestrating all components
- Manages application flow and user interaction
- Integrates all classes into cohesive workflow

### How to Run

```bash
# Run the grade generator
python grade-generator.py
```

### Usage Instructions

1. **Enter Assignment Details** when prompted:
   - **Assignment Name**: Any descriptive name (e.g., "Group Coding Lab")
   - **Category**: 
     - `FA` - Formative Assessment
     - `SA` - Summative Assessment
   - **Grade**: Must be between 0-100
   - **Weight**: Must be a positive number

2. **Add Multiple Assignments**: 
   - Choose `y` to add more assignments
   - Choose `n` when finished

3. **View Summary** showing:
   - Total number of assignments
   - Formative and Summative totals with weights
   - Final grade percentage
   - GPA (out of 5.0)
   - Pass/Fail status
   - Assignments to resubmit (if failed)

4. **Check Output**:
   - Console displays formatted summary
   - `grades.csv` file is automatically created

### Validation Rules

| Input | Rule | Error Handling |
|-------|------|----------------|
| **Grade** | Must be 0-100 | Reprompts until valid |
| **Category** | Must be "FA" or "SA" (case-insensitive) | Reprompts until valid |
| **Weight** | Must be positive number | Reprompts until valid |
| **Data Types** | Numeric values only | Catches ValueError |

### Calculation Logic

1. **Weighted Grade**: `(Grade / 100) × Weight`
2. **Category Totals**:
   - Total Formative = Sum of all FA weighted grades
   - Total Summative = Sum of all SA weighted grades
3. **Final Grade**: `Total Formative + Total Summative`
4. **GPA**: `(Final Grade / 100) × 5.0`
5. **Pass/Fail Logic**:
   - Must score ≥50% in **BOTH** FA and SA categories
   - Example: If total FA weight is 60, student needs ≥30
   - If total SA weight is 40, student needs ≥20

### Example Output

```
==================================================
GRADE SUMMARY
==================================================

Total Assignments: 4

Formative Total: 45.00 / 60.00
Summative Total: 32.00 / 40.00

Final Grade: 77.00%
GPA: 3.85 / 5.0
Status: PASS
==================================================

✓ Data exported to grades.csv
```

### CSV File Format

```csv
Assignment,Category,Grade,Weight
Group Coding Lab,FA,80,30
Individual Lab,FA,75,30
Midterm Exam,SA,85,20
Final Project,SA,75,20
```

---

## 🔧 Part 2: Shell Script Organizer

### Features
- ✅ **Automatic Archive Directory Creation**
- ✅ **CSV File Detection** in current directory
- ✅ **Timestamp Generation** (YYYYMMDD-HHMMSS format)
- ✅ **Comprehensive Logging** with file contents
- ✅ **File Archiving** with timestamped names
- ✅ **Accumulative Log Entries** (never overwrites)

### How to Run

```bash
# Make script executable (first time only)
chmod +x organizer.sh

# Run the organizer
./organizer.sh
```

### What It Does

1. **Checks for Archive Directory**
   - Creates `archive/` if it doesn't exist
   - Displays confirmation message

2. **Finds CSV Files**
   - Searches current directory only (not subdirectories)
   - Identifies all `.csv` files

3. **Processes Each CSV File**:
   - Generates timestamp: `YYYYMMDD-HHMMSS`
   - Creates new filename: `originalname-YYYYMMDD-HHMMSS.csv`
   - Logs archiving details and entire file contents
   - Moves file to `archive/` directory

### Log File Format

```
========================================
Archive Date: 2025-11-23 14:30:25
Original File: grades.csv
New File: grades-20251123-143025.csv
Contents:
Assignment,Category,Grade,Weight
Group Coding Lab,FA,80,30
Individual Lab,SA,90,40

========================================
Archive Date: 2025-11-23 15:45:10
Original File: grades.csv
New File: grades-20251123-154510.csv
Contents:
[... file contents ...]

```

### Example Execution

**Before running organizer.sh:**
```
.
├── grade-generator.py
├── grades.csv
└── organizer.sh
```

**After running organizer.sh:**
```
.
├── archive/
│   └── grades-20251123-143025.csv
├── grade-generator.py
├── organizer.log
└── organizer.sh
```

---

## 🧪 Testing Guide

### Python Script Tests

- [ ] **Valid Input Acceptance**
  - Grades between 0-100 are accepted
  - Categories FA/SA (case-insensitive) are accepted
  - Positive weights are accepted

- [ ] **Invalid Input Rejection**
  - Grades outside 0-100 trigger error message
  - Invalid categories (not FA/SA) trigger error message
  - Negative or zero weights trigger error message
  - Non-numeric inputs are caught and handled

- [ ] **Calculation Accuracy**
  - Weighted grades calculated correctly
  - Category totals sum properly
  - Final grade matches expected value
  - GPA calculation is accurate (out of 5.0)

- [ ] **Pass/Fail Logic**
  - Pass when both FA ≥50% and SA ≥50%
  - Fail when FA <50% (shows in resubmit list)
  - Fail when SA <50% (shows in resubmit list)
  - Fail when both <50% (both show in resubmit list)

- [ ] **File Operations**
  - CSV file is created successfully
  - CSV contains correct headers
  - CSV contains all entered assignments
  - Data format matches specification

### Shell Script Tests

- [ ] **Directory Management**
  - Creates `archive/` directory if missing
  - Doesn't error if `archive/` already exists
  - Handles permissions properly

- [ ] **File Detection**
  - Finds all CSV files in current directory
  - Ignores CSV files in subdirectories
  - Handles case when no CSV files exist

- [ ] **Timestamp Format**
  - Format is exactly `YYYYMMDD-HHMMSS`
  - Timestamp reflects actual execution time
  - Different runs produce different timestamps

- [ ] **File Naming**
  - New filename format: `name-YYYYMMDD-HHMMSS.csv`
  - Original filename preserved in base name
  - Extension remains `.csv`

- [ ] **Logging**
  - `organizer.log` is created
  - Log contains archive date/time
  - Log contains original filename
  - Log contains new filename
  - Log contains entire file contents
  - Multiple runs append (don't overwrite)

- [ ] **File Movement**
  - Files moved to `archive/` directory
  - Files renamed with timestamp
  - Original files removed from current directory

### Complete Workflow Test

```bash
# 1. Run Python script
python grade-generator.py
# Enter test data and verify output

# 2. Check CSV was created
ls -la grades.csv

# 3. Run organizer first time
./organizer.sh

# 4. Verify results
ls -la archive/          # Should have 1 file
cat organizer.log        # Should have 1 entry
ls grades.csv            # Should not exist

# 5. Run Python script again
python grade-generator.py

# 6. Run organizer second time
./organizer.sh

# 7. Verify accumulation
ls -la archive/          # Should have 2 files
cat organizer.log        # Should have 2 entries
```

---

## 🚀 Quick Start Guide

### Step 1: Clone/Setup Repository
```bash
git clone <your-repo-url>
cd Lab1-{YourGithubUsername}
```

### Step 2: Run Grade Generator
```bash
python grade-generator.py
```

### Step 3: Archive Results
```bash
chmod +x organizer.sh    # First time only
./organizer.sh
```

### Step 4: View Results
```bash
ls archive/              # See archived files
cat organizer.log        # Read log entries
```

---

## 🛠️ Troubleshooting

### Python Script Issues

**Problem:** `NameError: name 'InputValidator' is not defined`
```
Solution: Ensure class names match throughout the code.
Check that InputValidator and ReportGenerator classes use PascalCase.
```

**Problem:** `grades.csv` not created
```
Solution: 
- Check file permissions in directory
- Ensure you complete at least one assignment entry
- Verify no errors during script execution
```

**Problem:** Validation not working
```
Solution:
- Ensure methods are called correctly
- Check that validator instance is created
- Verify input prompts are displayed
```

### Shell Script Issues

**Problem:** `Permission denied` when running `./organizer.sh`
```bash
Solution: Make script executable
chmod +x organizer.sh
```

**Problem:** Script not finding CSV files
```
Solution:
- Ensure CSV files are in same directory as script
- Check files have .csv extension (lowercase)
- Run: ls *.csv to verify files exist
```

**Problem:** Archive directory not created
```
Solution:
- Check directory permissions
- Ensure script has write access
- Run: mkdir archive manually if needed
```

**Problem:** On Windows, bash commands don't work
```
Solution:
- Install Git for Windows (includes Git Bash)
- OR use WSL (Windows Subsystem for Linux)
- OR run: bash organizer.sh
```

---

## 📋 Submission Checklist

- [ ] Repository named correctly: `Lab1-{YourGithubUsername}`
- [ ] All required files present:
  - [ ] `grade-generator.py`
  - [ ] `organizer.sh`
  - [ ] `README.md`
- [ ] Python script uses OOP approach (5 classes)
- [ ] Python script has no static methods
- [ ] All validation rules implemented correctly
- [ ] Pass/Fail logic works for both categories
- [ ] CSV file generated with correct format
- [ ] Shell script creates archive directory
- [ ] Shell script generates correct timestamp format
- [ ] Shell script logs all required information
- [ ] Shell script moves and renames files correctly
- [ ] Log file accumulates entries (doesn't overwrite)
- [ ] Both scripts tested and working
- [ ] Code follows Python naming conventions (PascalCase for classes)
- [ ] Repository is public and accessible

---

## 🎓 Learning Outcomes Achieved

### 1. Data Structures ✅
- Used lists to store multiple Assignment objects
- Used dictionaries for summary data representation
- Implemented data manipulation through class methods

### 2. Loops and Control Flow ✅
- `while` loops for input collection
- `for` loops for processing assignments
- Conditional logic for validation and pass/fail determination

### 3. Input Validation ✅
- Try-except blocks for error handling
- Range validation for grades (0-100)
- Type validation for numeric inputs
- Category validation with specific allowed values

### 4. Object-Oriented Programming ✅
- 5 classes with single responsibilities
- Encapsulation of data and behavior
- Instance methods (no static methods)
- Object composition in GradeGeneratorApp

### 5. User Interaction ✅
- Interactive console prompts
- Formatted output display
- User-friendly error messages
- Clear summary presentation

### 6. File Operations ✅
- Writing data to CSV format
- Reading user input and processing
- Bash script for file management
- Log file creation and appending

### 7. Shell Scripting ✅
- Conditional directory creation
- File searching and filtering
- Timestamp generation
- Automated file organization

---

## 👨‍💻 Author Information

**Student Name:** NDEKWE Dieu Merci  
**Program:** BSE Year 1 Trimester 2  
**Institution:** African Leadership University  
**Course:** Introduction to Python Programming and Databases  
**Lab:** Lab 1 - Grade Generator Calculator  
**Submission Date:** November 23, 2025

---

## 📝 Additional Notes

### Design Decisions

1. **OOP Approach**: Chose to implement full OOP with 5 distinct classes to demonstrate encapsulation, modularity, and single responsibility principle.

2. **No Static Methods**: All methods are instance methods to maintain flexibility for future enhancements and proper OOP design.

3. **Comprehensive Validation**: Implemented robust error handling to ensure data integrity and user-friendly experience.

4. **Accumulative Logging**: Shell script appends to log file rather than overwriting to maintain complete audit trail.

### Future Enhancements

- Add support for weighted category percentages (e.g., FA=60%, SA=40%)
- Implement grade editing functionality
- Add data visualization for grade distribution
- Create backup functionality before archiving
- Add email notification for low grades
- Implement database storage instead of CSV files

---

## 📞 Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section above
2. Review the example outputs
3. Verify all validation rules are met
4. Contact course instructor or TAw

---

**Last Updated:** November 23, 2025