use edupathway_db;
DELIMITER $$

CREATE EVENT IF NOT EXISTS decrement_room_duration
ON SCHEDULE EVERY 1 MINUTE
DO
BEGIN
    -- Decrement the duration for all rooms where duration > 0
    UPDATE room
    SET duration = duration - 1
    WHERE duration > 0;

    -- Delete rows where duration has reached 0
    DELETE FROM room
    WHERE duration = 0;
END$$

DELIMITER ;
