/* Insert */
INSERT INTO StudentCourse (courseCode, studentID, cyear, grade) 
SELECT c.courseCode, 101 as studentID, 2024 as cyear, 'A' as grade 
FROM Course c 
JOIN FacultyMember fm ON c.instructor = fm.facultyID 
WHERE fm.fullName = 'John Doe' AND c.cyear = 2024; 

/* Update 
UPDATE StudentCourse sc 
SET sc.grade = 'B' 
WHERE sc.courseCode IN ( 
    SELECT courseCode 
    FROM StudentCourse 
    WHERE grade < 'C' 
    GROUP BY courseCode 
    HAVING AVG(grade) < 'C' 
) AND sc.cyear = 2024; 

/* Delete
DELETE FROM CalendarEvent 
WHERE courseCode IN ( 
    SELECT courseCode 
    FROM Course 
    WHERE cyear != 2024 
); 

