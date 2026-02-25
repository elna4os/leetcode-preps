# Easy
# https://leetcode.com/problems/list-the-products-ordered-in-a-period
WITH t1 AS (
    SELECT
        product_id,
        unit
    FROM
        Orders
    WHERE
        order_date >= '2020-02-01'
        AND order_date < '2020-03-01'
),
t2 AS (
    SELECT
        product_id,
        SUM(unit) AS unit
    FROM
        t1
    GROUP BY
        product_id
    HAVING
        SUM(unit) >= 100
)
SELECT
    p.product_name,
    t2.unit
FROM
    t2
    INNER JOIN Products p ON p.product_id = t2.product_id;