# Easy
# https://leetcode.com/problems/capital-gainloss
WITH t1 AS (
    SELECT
        stock_name,
        price,
        CASE
            WHEN operation = 'Buy' THEN -1
            ELSE 1
        END AS price_sign
    FROM
        Stocks
)
SELECT
    stock_name,
    SUM(price * price_sign) AS capital_gain_loss
FROM
    t1
GROUP BY
    stock_name;