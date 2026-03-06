# Easy
# https://leetcode.com/problems/biggest-single-number

WITH t1 AS (
    SELECT
        num,
        COUNT(num) as count
    FROM MyNumbers
    GROUP BY num
)
SELECT 
    MAX(num) AS num
FROM t1
WHERE count = 1;