SELECT 
    c1.visited_on,
    SUM(c2.daily_amount) AS amount,
    ROUND(SUM(c2.daily_amount) / 7, 2) AS average_amount
FROM
    (
        SELECT visited_on, SUM(amount) AS daily_amount
        FROM Customer
        GROUP BY visited_on
    ) c1
JOIN
    (
        SELECT visited_on, SUM(amount) AS daily_amount
        FROM Customer
        GROUP BY visited_on
    ) c2
ON c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY)
                     AND c1.visited_on
GROUP BY c1.visited_on
HAVING COUNT(c2.visited_on) = 7
ORDER BY c1.visited_on;
