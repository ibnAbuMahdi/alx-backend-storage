-- 101 average weighted score for all

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

-- procedure to calculate average weighted score for all
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE user_id INT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    OPEN cur;
    user_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;
        CALL ComputeAverageWeightedScoreForUser(user_id);
    END LOOP;
    CLOSE cur;
END$$
DELIMITER ;
