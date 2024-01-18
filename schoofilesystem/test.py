from urllib.request import urlopen
from bs4 import BeautifulSoup

# Function to fetch data from a URL
def fetch_data(url):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Example usage
school_url = 'https://www.aupp.edu.kh/academic-information/'  # Replace with the actual school website URL

# Fetch data from the school webpage
school_data = fetch_data(school_url)

# Extract assessment information, student scores, and other details
assessment_info = school_data.find('div', {'class': 'assessment-info'}).text
student_scores = school_data.find('table', {'id': 'student-scores'}).text
other_details = school_data.find('div', {'class': 'other-details'}).text

# Print the extracted data
print('Assessment Information:', assessment_info)
print('Student Scores:', student_scores)
print('Other Details:', other_details)