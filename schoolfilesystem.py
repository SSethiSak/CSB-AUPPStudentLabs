
#Libraries you may need:
#import csv, collections, dictionary, (pandas as pd), urlopen, etc..
import csv
import collections
import pandas as pd
from PyPDF2 import PdfReader

#import urlopen


#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self,filename):
        self.filename = filename
        self.student = []
        self.text = None
        self.pdf = None
    def process_file(self):            
        types = self.filename[-3:]
        try:
            if types == 'txt':   
                with open(filename, 'r') as file:
                    text = file.read()
                    self.text = text
                    
            elif types == 'pdf':
                reader = PdfReader(filename)
                page = reader.pages[0]
                text = page.extract_text()
                self.pdf = text
                
            elif types == 'csv':
                with open(filename, mode = 'r') as file:              
                    csvFile = csv.reader(file)
                    for i in csvFile:
                        self.student.append(i)
                    
                        
        except FileNotFoundError:
            # Handle file not found exception
            print(f"Error: File '{filename}' not found.")
            return None
            
        print(self.student)
        
    def transfer_data():
        pass
    def fetch_web_data():
        pass
    
    def analyze_content(self, student_name):
        for i in self.student:
            if i[0] == student_name:
                avrg_score = (eval(i[6]) + eval(i[7]) + eval(i[8])) / 3
                top_score = max(i[6:])
                top_index = i.index(top_score)

                self.generate_summary(student_name, avrg_score, top_index, top_score)
                
        
    def generate_summary(self, student_name, avg_score, top_class_index, top_score):
        print(f"1. Overall Performance of {student_name}:")
        print(f"-Average Score: {avg_score}\n-Top-Performing-class: {self.student[0][top_class_index]}")
        


filename = input("enter a file name: ")
new_system = SchoolAssessmentSystem(filename)
new_system.process_file()
assessment = input("Enter a student name: ")
new_system.analyze_content(assessment)

# Analyze content & display result area
# Sample of Output:
"""
School Assessment Summary Report:

1. Overall Performance of Student A:
   - Average score: 85.5
   - Top-performing class: Grade 10B

2. Subject-wise Analysis:
   - Mathematics: Improved by 10% compared to the last assessment.
   - Science: Consistent performance across all classes.

3. Notable Observations:
   - Grade 8A shows a significant improvement in English proficiency.

4. Web Data Insights:
   - Online participation: 95% of students accessed assessment resources online.

5. Recommendations:
   - Consider additional support for Grade 9B in Mathematics.

Report generated on: 2024-01-14
"""
