
#Libraries you may need:
#import csv, collections, dictionary, (pandas as pd), urlopen, etc..
import csv
import collections
import pandas as pd
from PyPDF2 import PdfReader

#import urlopen


#classes and Functions to implement
class SchoolAssessmentSystem:
    def __init__(self,curr_semester, prev_semester):
        self.curr_semester = curr_semester
        self.prev_semester = prev_semester
        self.student = []
        self.student_prev_semester = []
        self.text = None
        self.pdf = None
        
    def process_file(self,):            
        types = self.curr_semester[-3:]

        try:
            if types == 'txt':   
                with open(curr_semester, 'r') as file:
                    text = file.read()
                    self.text = text
                    
            elif types == 'pdf':
                reader = PdfReader(curr_semester)
                page = reader.pages[0]
                text = page.extract_text()
                self.pdf = text
                
            elif types == 'csv':
                with open(curr_semester, mode = 'r') as file:              
                    csvFile = csv.reader(file)
                    for i in csvFile:
                        self.student.append(i)
                
                with open(prev_semester, mode = 'r') as file:
                    csvFile = csv.reader(file)
                    for i in csvFile:
                        self.student_prev_semester.append(i)
                    
                        
        except FileNotFoundError:
            # Handle file not found exception
            print(f"Error: File '{curr_semester}' not found.")
            return None
            
        
    def transfer_data(self, file1, file2):


        df = pd.read_csv(file1)
        df2 = pd.read_csv(file2)
        
        header = df.columns.tolist()
        merged = pd.merge(df[['name', 'math score', 'English score', 'Science score']], df2[['name', 'math score', 'English score', 'Science score']], on="name")
        merged.to_csv('new_merged.csv', index=False)
        
    def fetch_web_data():
        pass
    
    def analyze_content(self, student_name):
        curr_score = []
        prev_score = []
        
        for i in self.student:
            if i[0] == student_name:
                avrg_score = (eval(i[6]) + eval(i[7]) + eval(i[8])) / 3
                top_score = max(i[6:])
                top_index = i.index(top_score)
                curr_score = curr_score + [eval(x) for x in i[6:]]

                
        for j in self.student_prev_semester:
            if j[0] == student_name:
                prev_score = prev_score + [eval(x) for x in j[6:]]
                
        assessment_result = []
        for score in range(len(curr_score)):
            assessment_result.append(curr_score[score] - prev_score[score])
        
        self.generate_summary(student_name, avrg_score, top_index, top_score, assessment_result)
        
        class_data = {assessment[2]: {'math':0, 'english' : 0, 'science' : 0} for assessment in self.student[1:]}

        class_data['10A']['math'] = 45
        for student in self.student[1:]:
            class_data[student[2]]['math'] += eval(student[6])
            class_data[student[2]]['english'] += eval(student[7])
            class_data[student[2]]['science'] += eval(student[8])

        print(class_data)

            
                
        
    def generate_summary(self, student_name, avg_score, top_class_index, top_score, scores):
        print(f"1. Overall Performance of {student_name}:")
        print(f"-Average Score: {avg_score}\n-Top-Performing-class: {self.student[0][top_class_index]}")
        print("2. Subject-wise Analysis:")
        sub_ind = 6
        for result in scores:
            if result > 0:
                print(f"{self.student[0][sub_ind]}: Improved by {result}% compared to the last assessment.")
                sub_ind += 1
            elif result < 0:
                print(f"{self.student[0][sub_ind]}:  Worsened by {result}% compared to the last assessment.")
                sub_ind += 1
            else:
                print(f"{self.student[0][sub_ind]}: Consistent performance across all classes.")
    
    def print_student(self):
        for i in self.student:
            print(i[0])
        
        


curr_semester = input("enter a file name for the current semester: ")
prev_semester = input("enter a file name for the previous semester: ")

new_system = SchoolAssessmentSystem(curr_semester, prev_semester)
new_system.process_file()

new_system.print_student()
# print(new_system.student)
# print(new_system.student_prev_semester)

assessment = input("Enter a student name: ")
new_system.analyze_content(assessment)

new_system.transfer_data(curr_semester, prev_semester)
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
