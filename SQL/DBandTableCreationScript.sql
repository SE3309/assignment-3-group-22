
/*Assignment 3 Db Schema Script*/

CREATE DATABASE 3309Proj;
USE 3309Proj;
/*Create Tables*/

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
    year INT,
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
    year INT,
    PRIMARY KEY (courseCode, year),
    FOREIGN KEY (courseCode) REFERENCES CourseDetails(courseCode),
    FOREIGN KEY (instructor) REFERENCES FacultyMember(facultyID)
);

CREATE TABLE StudentCourse (
    courseCode VARCHAR(10),
    studentID INT,
    grade CHAR(2),
    PRIMARY KEY (courseCode, studentID),
    FOREIGN KEY (studentID) REFERENCES Student(studentID),
    FOREIGN KEY (courseCode) REFERENCES CourseDetails(courseCode)
);

CREATE TABLE CalendarEvent (
    eventID INT PRIMARY KEY,
    eventName VARCHAR(255),
    eventDescription TEXT,
    eventStart DATETIME,
    eventDuration TIME,
    courseID VARCHAR(10) NULL,
    studentID INT NULL,
    FOREIGN KEY (courseID) REFERENCES CourseDetails(courseCode),
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

--Trigers

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








