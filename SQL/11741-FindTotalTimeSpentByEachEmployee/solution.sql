# https://leetcode.com/problems/find-total-time-spent-by-each-employee/

SELECT event_day as day, emp_id, sum(out_time) - sum(in_time) as total_time FROM employees GROUP BY day, emp_id
