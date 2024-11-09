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
    credits DECIMAL(4, 1),
    CONSTRAINT chk_course_credits_multiple CHECK (credits % 0.5 = 0)
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
    FOREIGN KEY (courseCode, cyear) REFERENCES Course(courseCode, cyear) -- Updated reference
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
    FOREIGN KEY (courseCode, cyear) REFERENCES Course(courseCode, cyear), -- Updated reference
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

DELIMITER $$

CREATE TRIGGER prevent_student_event_overlap
BEFORE INSERT ON CalendarEvent
FOR EACH ROW
BEGIN
    DECLARE event_end TIME;
    DECLARE conflicting_event_count INT;

    -- Calculate the end time of the new event based on its start time and duration
    SET event_end = ADDTIME(NEW.eventStart, NEW.eventDuration);

    -- Check for any overlapping events for the same student (if studentID is provided)
    IF NEW.studentID IS NOT NULL THEN
        -- Query to find any events for the same student that overlap with the new event
        SELECT COUNT(*) INTO conflicting_event_count
        FROM CalendarEvent
        WHERE studentID = NEW.studentID
        AND (
            -- Check if the new event starts before an existing event ends, and ends after it starts
            (NEW.eventStart < ADDTIME(eventStart, eventDuration) AND eventStart < event_end)
            OR
            -- Or if the new event ends after an existing event starts
            (eventStart < ADDTIME(NEW.eventStart, NEW.eventDuration) AND ADDTIME(NEW.eventStart, NEW.eventDuration) < ADDTIME(eventStart, eventDuration))
        );
        
        -- If there are overlapping events, raise an error
        IF conflicting_event_count > 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Student events overlap with existing events';
        END IF;
    END IF;
END $$

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






