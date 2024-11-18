CREATE VIEW FacultyCourseView AS
SELECT 
    fm.facultyID,
    fm.fullName AS facultyName,
    c.courseCode,
    cd.courseName,
    c.cyear AS courseYear
FROM 
    facultymember fm
JOIN 
    course c ON fm.facultyID = c.instructor
JOIN 
    coursedetails cd ON c.courseCode = cd.courseCode;

CREATE VIEW StudentEventCalendarView AS
SELECT 
    ce.eventID,
    ce.eventName,
    ce.eventStart,
    ce.eventDuration,
    s.studentID,
    s.fullName AS studentName
FROM 
    calendarevent ce
JOIN 
    student s ON ce.studentID = s.studentID;
