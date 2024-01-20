-- A view that lists students that have score under 80 and last_meeting is older than 30 days or NULL

CREATE VIEW need_meeting AS
SELECT name FROM students
WHERE score < 80 AND last_meeting is NULL OR (CURDATE() - last_meeting) > 30;
