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
            f"INSERT INTO Student (studentID, email, password, fullName, yearInProgram, graduationYear, program, departmentID) "
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
                f"INSERT INTO Course (courseCode, instructor, cyear) "
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
                    f"INSERT INTO StudentCourse (courseCode, studentID, cyear, grade) "
                    f"VALUES ('{course_code}', {student_id}, {year}, '{grade}');"
                )
                insert_statements.append(insert_statement)

    return insert_statements

def generate_calendar_event_insert_statements(num_students, course_details):
    """Generate INSERT statements for the CalendarEvent table."""
    insert_statements = []
    event_id = 1
    
    # Generate weekly course events from September to December 2024
    start_date = datetime(2024, 9, 1)  # Starting from September 2024
    end_date = datetime(2024, 12, 31)  # Until December 2024
    days_in_week = 7  # Days in a week for weekly events
    duration_str = "03:00:00"  # Fixed three-hour duration

    for course_code in course_details:
        # Schedule weekly lectures for each course
        current_date = start_date
        while current_date <= end_date:
            # Generate insert statement for a weekly lecture
            insert_statement = (
                f"INSERT INTO CalendarEvent (eventID, eventName, eventDescription, eventStart, eventDuration, "
                f"courseCode, cyear, studentID) "
                f"VALUES ({event_id}, 'Weekly Lecture for {course_code}', 'Weekly lecture', "
                f"'{current_date}', '{duration_str}', '{course_code}', 2024, NULL);"
            )
            insert_statements.append(insert_statement)
            event_id += 1
            current_date += timedelta(days=days_in_week)  # Move to the next week

    # Generate individual events for each student
    for student_id in range(1, num_students + 1):
        for _ in range(5):  # Each student has 5 events from Sep to Dec
            event_start = datetime(2024, 9, 1) + timedelta(days=random.randint(0, 120))  # Random date in range
            duration_hours = random.randint(1, 3)  # Random duration 1 to 3 hours
            duration_str = f"{duration_hours}:00:00"  # Format for SQL TIME
            
            # Generate insert statement for individual student event
            insert_statement = (
                f"INSERT INTO CalendarEvent (eventID, eventName, eventDescription, eventStart, eventDuration, "
                f"courseCode, cyear, studentID) "
                f"VALUES ({event_id}, 'Student Event', 'Event for Student {student_id}', "
                f"'{event_start}', '{duration_str}', NULL, NULL, {student_id});"
            )
            insert_statements.append(insert_statement)
            event_id += 1

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
num_students = 2500
num_faculty = 1500
num_courses = 250
num_contacts = 2500


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

sql_script = """
-- Assignment 3 Db Schema Script
CREATE DATABASE 3309Proj;
USE 3309Proj;

-- Create Tables

CREATE TABLE Department (
    departmentID INT PRIMARY KEY,
    departmentName VARCHAR(255) UNIQUE,
    address VARCHAR(255),
    postalCode VARCHAR(10)
);

CREATE TABLE Student (
    studentID INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    fullName VARCHAR(255),
    yearInProgram INT,
    graduationYear INT,
    program VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE FacultyMember (
    facultyID INT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    fullName VARCHAR(255),
    role VARCHAR(255),
    officeNo VARCHAR(50),
    contactInfo VARCHAR(255),
    departmentID INT,
    FOREIGN KEY (departmentID) REFERENCES Department(departmentID)
);

CREATE TABLE CourseDetails (
    courseCode VARCHAR(10) PRIMARY KEY,
    courseName VARCHAR(255),
    courseDescription TEXT,
    credits INT
);

CREATE TABLE Course (
    courseCode VARCHAR(10),
    instructor INT,
    cyear INT,
    PRIMARY KEY (courseCode, cyear),
    FOREIGN KEY (courseCode) REFERENCES CourseDetails(courseCode),
    FOREIGN KEY (instructor) REFERENCES FacultyMember(facultyID)
);

CREATE TABLE StudentCourse (
    courseCode VARCHAR(10),
    studentID INT,
    cyear INT,
    grade CHAR(2),
    PRIMARY KEY (courseCode, cyear, studentID),
    FOREIGN KEY (studentID) REFERENCES Student(studentID),
    FOREIGN KEY (courseCode, cyear) REFERENCES Course(courseCode, cyear)
);

CREATE TABLE CalendarEvent (
    eventID INT PRIMARY KEY,
    eventName VARCHAR(255),
    eventDescription TEXT,
    eventStart DATETIME,
    eventDuration TIME,
    courseCode VARCHAR(10) NULL,
    cyear INT NULL,
    studentID INT NULL,
    FOREIGN KEY (courseCode, cyear) REFERENCES Course(courseCode, cyear),
    FOREIGN KEY (studentID) REFERENCES Student(studentID)
);

CREATE TABLE Contact (
    phoneNumber VARCHAR(15) PRIMARY KEY,
    cName VARCHAR(255),
    address VARCHAR(255),
    postalCode VARCHAR(10)
);

CREATE TABLE EmergencyContact (
    studentID INT,
    phoneNumber VARCHAR(15),
    PRIMARY KEY (studentID, phoneNumber),
    FOREIGN KEY (studentID) REFERENCES Student(studentID),
    FOREIGN KEY (phoneNumber) REFERENCES Contact(phoneNumber)
);

-- Triggers

DELIMITER //

CREATE TRIGGER limit_emergency_contacts
BEFORE INSERT ON EmergencyContact
FOR EACH ROW
BEGIN
    DECLARE contact_count INT;

    -- Count existing emergency contacts for the given studentID
    SELECT COUNT(*) INTO contact_count
    FROM EmergencyContact
    WHERE studentID = NEW.studentID;

    -- Prevent insertion if the student already has 3 emergency contacts
    IF contact_count >= 3 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A student can have a maximum of 3 emergency contacts.';
    END IF;
END //

DELIMITER ;

-- To view the structure of the Department table
DESCRIBE Department;

-- To view the structure of the Student table
DESCRIBE Student;

-- To view the structure of the FacultyMember table
DESCRIBE FacultyMember;

-- To view the structure of the CourseDetails table
DESCRIBE CourseDetails;

-- To view the structure of the Course table
DESCRIBE Course;

-- To view the structure of the StudentCourse table
DESCRIBE StudentCourse;

-- To view the structure of the CalendarEvent table
DESCRIBE CalendarEvent;

-- To view the structure of the Contact table
DESCRIBE Contact;

-- To view the structure of the EmergencyContact table
DESCRIBE EmergencyContact;




"""



# Combine all statements into a single list
combined_statements = sql_script.splitlines() + [
    
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
