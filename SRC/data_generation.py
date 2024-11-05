import random
import string
from datetime import datetime, timedelta

def generate_department_insert_statements(num_departments):
    """Generate INSERT statements for the Department table."""
    insert_statements = []
    for department_id in range(1, num_departments + 1):
        department_name = f"Department_{department_id}"
        address = f"{random.randint(1, 999)} Main St, City {department_id}"
        postal_code = f"{random.randint(10000, 99999)}"
        insert_statement = (
            f"INSERT INTO Department (departmentID, departmentName, address, postalCode) "
            f"VALUES ({department_id}, '{department_name}', '{address}', '{postal_code}');"
        )
        insert_statements.append(insert_statement)
    return insert_statements

def generate_student_insert_statements(num_students, department_ids):
    """Generate INSERT statements for the Student table."""
    insert_statements = []
    for student_id in range(1, num_students + 1):
        email = f"student{student_id}@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        full_name = f"Student {student_id}"
        year = random.randint(1, 4)  # Random year between 1-4
        graduation_year = year + 4
        program = f"Program_{random.randint(1, 10)}"
        department_id = random.choice(department_ids)  # Pick a valid department ID
        insert_statement = (
            f"INSERT INTO Student (studentID, email, password, fullName, year, graduationYear, program, departmentID) "
            f"VALUES ({student_id}, '{email}', '{password}', '{full_name}', {year}, {graduation_year}, '{program}', {department_id});"
        )
        insert_statements.append(insert_statement)
    return insert_statements

def generate_faculty_insert_statements(num_faculty, department_ids):
    """Generate INSERT statements for the FacultyMember table."""
    insert_statements = []
    for faculty_id in range(1, num_faculty + 1):
        email = f"faculty{faculty_id}@example.com"
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        full_name = f"Faculty {faculty_id}"
        role = random.choice(['Professor', 'Lecturer', 'Assistant Professor'])
        office_no = f"Office_{faculty_id}"
        contact_info = f"123-456-789{faculty_id % 10}"
        department_id = random.choice(department_ids)  # Pick a valid department ID
        insert_statement = (
            f"INSERT INTO FacultyMember (facultyID, email, password, fullName, role, officeNo, contactInfo, departmentID) "
            f"VALUES ({faculty_id}, '{email}', '{password}', '{full_name}', '{role}', '{office_no}', '{contact_info}', {department_id});"
        )
        insert_statements.append(insert_statement)
    return insert_statements

def generate_course_details_insert_statements(num_courses):
    """Generate INSERT statements for the CourseDetails table."""
    insert_statements = []
    for course_code in range(1, num_courses + 1):
        course_code_str = f"COURSE{course_code}"
        course_name = f"Course Name {course_code}"
        course_description = f"This is a description for {course_name}."
        credits = random.choice([0.5, 1.0])  # Only .5 or 1
        insert_statement = (
            f"INSERT INTO CourseDetails (courseCode, courseName, courseDescription, credits) "
            f"VALUES ('{course_code_str}', '{course_name}', '{course_description}', {credits});"
        )
        insert_statements.append(insert_statement)
    return insert_statements

def generate_course_insert_statements(course_details):
    """Generate INSERT statements for the Course table with entries for 2024, 2025, and 2026."""
    insert_statements = []
    for course_code in course_details:
        for year in range(2024, 2027):  # Years 2024, 2025, 2026
            instructor = random.choice(range(1, num_faculty + 1))  # Assuming 1000 faculty members
            insert_statement = (
                f"INSERT INTO Course (courseCode, instructor, year) "
                f"VALUES ('{course_code}', {instructor}, {year});"
            )
            insert_statements.append(insert_statement)
    return insert_statements

def generate_student_course_insert_statements(num_students, course_details):
    """Generate INSERT statements for the StudentCourse table for each student taking 12 courses a year."""
    insert_statements = []

    for student_id in range(1, num_students + 1):  # Assuming student IDs are sequential from 1 to num_students
        for year in range(2024, 2027):  # For the years 2024, 2025, and 2026
            # Pick 12 unique course codes for the current year
            selected_courses = random.sample(course_details, 12)  # Randomly select 12 courses

            for course_code in selected_courses:
                grade = random.choice(['A', 'B', 'C', 'D', 'F'])  # Random grade
                insert_statement = (
                    f"INSERT INTO StudentCourse (courseCode, studentID, year, grade) "
                    f"VALUES ('{course_code}', {student_id}, {year}, '{grade}');"
                )
                insert_statements.append(insert_statement)

    return insert_statements

def generate_calendar_event_insert_statements(num_students, course_details):
    """Generate INSERT statements for the CalendarEvent table."""
    insert_statements = []
    existing_events = set()  # To track existing events and prevent conflicts

    # Generate events for each student
    for student_id in range(1, num_students + 1):
        for _ in range(100):  # 100 events per student
            # Randomly pick a start time within the next 6 months
            event_start = datetime.now() + timedelta(days=random.randint(0, 180))
            duration_hours = random.randint(1, 3)  # Random duration between 1 and 3 hours
            event_end = event_start + timedelta(hours=duration_hours)
            duration_str = f"{duration_hours}:00:00"  # Format for TIME in SQL

            # Check for time conflicts
            event_tuple = (event_start, event_end)
            if event_tuple not in existing_events:
                existing_events.add(event_tuple)
                insert_statement = (
                    f"INSERT INTO CalendarEvent (eventID, eventName, eventDescription, eventStart, eventDuration, "
                    f"courseID, cyear, studentID) "
                    f"VALUES ({len(insert_statements) + 1}, 'Event for Student {student_id}', 'Description for event', "
                    f"'{event_start}', '{duration_str}', NULL, NULL, {student_id});"
                )
                insert_statements.append(insert_statement)

    # Generate course-related events (5 for each courseCode and year)
    for course_code in course_details:
        for _ in range(5):  # 5 events per courseCode and year combo
            # Randomly pick a start time within the next 6 months
            event_start = datetime.now() + timedelta(days=random.randint(0, 180))
            duration_hours = random.randint(1, 3)  # Random duration between 1 and 3 hours
            event_end = event_start + timedelta(hours=duration_hours)
            duration_str = f"{duration_hours}:00:00"  # Format for TIME in SQL

            # Check for time conflicts
            event_tuple = (event_start, event_end)
            if event_tuple not in existing_events:
                existing_events.add(event_tuple)
                insert_statement = (
                    f"INSERT INTO CalendarEvent (eventID, eventName, eventDescription, eventStart, eventDuration, "
                    f"courseID, cyear, studentID) "
                    f"VALUES ({len(insert_statements) + 1}, 'Event for {course_code}', "
                    f"'Description for course event', "
                    f"'{event_start}', '{duration_str}', '{course_code}', NULL, NULL);"
                )
                insert_statements.append(insert_statement)

    return insert_statements

phone_numbers = set()
def generate_contact_insert_statements(num_contacts):
    """Generate INSERT statements for the Contact table."""
    insert_statements = []
    
    for contact_id in range(1, num_contacts + 1):
        phone_number = f"+1-800-{random.randint(1000000, 9999999)}"  # Random phone number
        while phone_number in phone_numbers:
            phone_number = f"+1-800-{random.randint(1000000, 9999999)}"
        phone_numbers.add(phone_number)
        c_name = f"Contact Name {contact_id}"
        address = f"{random.randint(1, 999)} Contact St, City {contact_id}"
        postal_code = f"{random.randint(10000, 99999)}"
        insert_statement = (
            f"INSERT INTO Contact (phoneNumber, cName, address, postalCode) "
            f"VALUES ('{phone_number}', '{c_name}', '{address}', '{postal_code}');"
        )
        insert_statements.append(insert_statement)
    return insert_statements

def generate_emergency_contact_insert_statements(num_students, num_contacts):
    """Generate INSERT statements for the EmergencyContact table."""
    insert_statements = []
    student_contact_map = {}
    phone_number_list = list(phone_numbers) 

    for student_id in range(1, num_students + 1):
        student_contact_map[student_id] = set()  # Initialize a set for unique contacts

    for student_id in range(1, num_students + 1):
        while len(student_contact_map[student_id]) < 3:  # Each student can have up to 3 contacts
            phone_number = random.choice(phone_number_list)  # Randomly select a contact ID
            if phone_number not in student_contact_map[student_id]:  # Ensure uniqueness
                insert_statement = (
                    f"INSERT INTO EmergencyContact (studentID, phoneNumber) "
                    f"VALUES ({student_id},'{phone_number}');"
                )
                insert_statements.append(insert_statement)
                student_contact_map[student_id].add(phone_number)  # Add to the set of contacts

    return insert_statements

def save_to_sql_file(filename, statements):
    """Save the generated SQL statements to a file."""
    with open(filename, 'w') as file:
        for statement in statements:
            file.write(statement + '\n')

# Configuration for data generation
num_departments = 25
num_students = 500
num_faculty = 500
num_courses = 100
num_contacts = 500


# Generate data
department_statements = generate_department_insert_statements(num_departments)
student_statements = generate_student_insert_statements(num_students, range(1, num_departments + 1))
faculty_statements = generate_faculty_insert_statements(num_faculty, range(1, num_departments + 1))
course_details_statements = generate_course_details_insert_statements(num_courses)
course_details = [f'COURSE{course_code}' for course_code in range(1, num_courses + 1)]
course_statements = generate_course_insert_statements(course_details)
student_course_statements = generate_student_course_insert_statements(num_students, course_details)
calendar_event_statements = generate_calendar_event_insert_statements(num_students, course_details)
contact_statements = generate_contact_insert_statements(num_contacts)
emergency_contact_statements = generate_emergency_contact_insert_statements(num_students, num_contacts)

# Combine all statements into a single list
combined_statements = [
    "USE 3309Proj;",
    "-- Department Inserts",
] + department_statements + [
    "-- Student Inserts",
] + student_statements + [
    "-- Faculty Inserts",
] + faculty_statements + [
    "-- Course Details Inserts",
] + course_details_statements + [
    "-- Course Inserts",
] + course_statements + [
    "-- Student Course Inserts",
] + student_course_statements + [
    "-- Calendar Event Inserts",
] + calendar_event_statements + [
    "-- Contact Inserts",
] + contact_statements + [
    "-- Emergency Contact Inserts",
] + emergency_contact_statements

# Save to a single SQL file
save_to_sql_file('full_insert_script.sql', combined_statements)

print("Single SQL script generated successfully!")
