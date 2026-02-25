# https://leetcode.com/problems/most-common-course-pairs/

WITH top_performers AS (
    SELECT
        user_id
    FROM
        course_completions
    GROUP BY
        user_id
    HAVING
        COUNT(*) >= 5
        AND AVG(course_rating) >= 4
),
filtered AS (
    SELECT
        cc.user_id,
        cc.course_name,
        cc.completion_date
    FROM
        course_completions cc
        JOIN top_performers tp ON cc.user_id = tp.user_id
),
chained AS (
    SELECT
        course_name AS first_course,
        LEAD(course_name) OVER (
            PARTITION BY user_id
            ORDER BY
                completion_date
        ) AS second_course
    FROM
        filtered
)
SELECT
    first_course,
    second_course,
    COUNT(*) AS transition_count
FROM
    chained
WHERE
    second_course IS NOT NULL
GROUP BY
    first_course,
    second_course
ORDER BY
    transition_count DESC,
    LOWER(first_course) ASC,
    LOWER(second_course) ASC;