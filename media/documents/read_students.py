import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('students.xml')
root = tree.getroot()

# Iterate over each student in the XML
for student in root.findall('student'):
    # Retrieve the student's ID (attribute)
    student_id = student.get('id')
    
    # Retrieve the student's name, age, and major (sub-elements)
    name = student.find('name').text
    age = student.find('age').text
    major = student.find('major').text
    
    # Display the student information
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Major: {major}")
    print("-" * 20)