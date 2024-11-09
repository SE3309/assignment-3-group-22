-- Select statements used in Question 5 --
-- 1st select -- 
SELECT fullName, email, program
FROM Student
WHERE departmentID = 1 and program = "Program_8";
-- 2nd select -- 
SELECT s.fullName, s.email, d.departmentName
FROM Student s
JOIN Department d ON s.departmentID = d.departmentID
where email = "student7@example.com";
-- 3rd select -- 
SELECT courseCode, studentID, grade
FROM StudentCourse
WHERE studentID IN (
    SELECT studentID
    FROM Student
    WHERE yearInProgram = 2 AND grade = 'F' and studentID = 2
    AND grade = 'F'
);
-- 4th select --  
SELECT program, COUNT(studentID) AS studentCount
FROM Student
GROUP BY program;
-- 5th select -- 
SELECT departmentName
FROM Department d
WHERE EXISTS (SELECT 1 FROM FacultyMember f WHERE f.departmentID = d.departmentID);
-- 6th select -- 
SELECT s.fullName, s.email, cd.courseName, c.cyear
FROM Student s
JOIN StudentCourse sc ON s.studentID = sc.studentID
JOIN Course c ON sc.courseCode = c.courseCode AND sc.cyear = c.cyear
JOIN CourseDetails cd ON c.courseCode = cd.courseCode
WHERE c.cyear = 2024 and cd.courseName = 'Course Name 33' and sc.grade = UPPER('f');
-- 7th select -- 
SELECT cd.courseCode, cd.courseName
FROM CourseDetails cd
LEFT JOIN StudentCourse sc ON cd.courseCode = sc.courseCode
WHERE sc.studentID = 41;