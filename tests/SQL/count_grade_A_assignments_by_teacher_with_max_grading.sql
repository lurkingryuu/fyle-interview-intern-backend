-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(grade) AS grade_A_count
FROM assignments JOIN (
    SELECT teacher_id
    FROM assignments
    WHERE state = 'GRADED'
    GROUP BY teacher_id
    ORDER BY COUNT(grade) DESC
    LIMIT 1
) AS max_teach ON assignments.teacher_id = max_teach.teacher_id
WHERE grade = 'A';