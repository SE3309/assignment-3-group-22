-- Insert statements used in Question 3 -- 
-- 1st insert --
INSERT INTO CalendarEvent (eventID, eventName, eventDescription, eventStart, eventDuration, courseCode, cyear, studentID)
SELECT 
    ROW_NUMBER() OVER (ORDER BY c.courseCode) + 100000 AS eventID,
    CONCAT(c.courseName, ' Exam') AS eventName,
    CONCAT('Midterm exam for ', c.courseName) AS eventDescription,
    '2024-03-15 10:00:00' AS eventStart,
    '02:00:00' AS eventDuration,
    c.courseCode,
    2024 AS cyear,
    s.studentID
FROM CourseDetails c
CROSS JOIN (SELECT studentID FROM Student WHERE studentID = 3) s;
-- 2nd insert --
INSERT INTO EmergencyContact (studentID, phoneNumber)
SELECT 
    s.studentID AS studentID, 
    c.phoneNumber
FROM Student s
JOIN Contact c ON c.cName = "Contact Name 1222"
WHERE s.departmentID = 10
LIMIT 1;
-- 3rd insert --
INSERT INTO Course (courseCode, instructor, cyear)
SELECT 
    'ECE4436' AS courseCode,
    f.facultyID,
    2024 as cyear
FROM FacultyMember f
WHERE f.fullName = 'Faculty 58';

