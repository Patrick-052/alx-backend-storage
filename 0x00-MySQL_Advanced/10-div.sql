-- Custom mysql function that returns the result of dividing two numbers

CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS DECIMAL(10,2) DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END;
