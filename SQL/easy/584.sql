# Write your MySQL query statement below

SELECT name
FROM customer
WHERE referee_id IS NULL
	OR NOT referee_id = 2;