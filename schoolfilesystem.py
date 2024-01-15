
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
        self.data = None
    def process_file(self):            
        types = self.filename[-3:]
        if types == 'txt':
            try:
                with open(filename, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                # Handle file not found exception
                print(f"Error: File '{filename}' not found.")
                return None

        elif types == 'pdf':
            
            reader = PdfReader(filename)
            page = reader.pages[0]
            text = page.extract_text()
        
        elif types == 'csv':
            with open(filename, mode = 'r') as file:
                text = []
                csvFile = csv.reader(file)
            
                text2 = csvFile
                for i in csvFile:
                    text.append(i)
            
        print(text)
        print(csvFile)
        print(types)
        
    def transfer_data():
        pass
    def fetch_web_data():
        pass
    def analyze_content():
        pass
    def generate_summary():
        pass


filename = input("enter a file name: ")
new_system = SchoolAssessmentSystem(filename)
new_system.process_file()

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
