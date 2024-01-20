-- procedure that computes all students average weighted score

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    SELECT SUM(score * weight) / SUM(weight) INTO @average_weighted_score FROM corrections
    JOIN projects ON corrections.project_id = projects.id;
    UPDATE users SET average_score = @average_weighted_score;
END;$$
DELIMITER ;
