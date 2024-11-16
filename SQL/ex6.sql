/* Insert */
INSERT INTO StudentCourse (courseCode, studentID, cyear, grade)
SELECT 'COURSE38', 2222 as studentID, 2025 as cyear, 'A' as grade
FROM Course c
JOIN FacultyMember fm ON c.instructor = fm.facultyID
WHERE fm.fullName = 'Faculty 1' AND c.cyear = 2025;

/* Update */ 
UPDATE StudentCourse sc 
JOIN ( 
    SELECT courseCode, 
           AVG(CASE 
               WHEN grade = 'A' THEN 4 
               WHEN grade = 'B' THEN 3 
               WHEN grade = 'C' THEN 2 
               WHEN grade = 'D' THEN 1 
               WHEN grade = 'F' THEN 0 
           END) AS avgGrade 
    FROM StudentCourse 
    GROUP BY courseCode 
    HAVING avgGrade < 2 
) avgCourses ON sc.courseCode = avgCourses.courseCode 
SET sc.grade = 'B' 
WHERE sc.grade = 'F' AND sc.courseCode IS NOT NULL; 

/* Delete */
DELETE FROM CalendarEvent
WHERE courseCode IN (
    SELECT courseCode
    FROM Course
    WHERE cyear != 2024
);