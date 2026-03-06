# Hard
# https://leetcode.com/problems/department-top-three-salaries

WITH t1 AS (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank
    FROM Employee
),
t2 AS (
    SELECT * FROM t1 WHERE rank <= 3
)
SELECT
    d.name AS "Department",
    t2.name AS "Employee",
    t2.salary AS "Salary"
FROM t2
INNER JOIN Department d ON t2.departmentId = d.id;