-- 100 average weighted score

-- procedure to calculate average weighted score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    SELECT SUM(score * weight), SUM(weight) INTO total_score, total_weight
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;
    UPDATE users
    SET average_score = total_score / total_weight
    WHERE id = user_id;
END;$$
DELIMITER ;
