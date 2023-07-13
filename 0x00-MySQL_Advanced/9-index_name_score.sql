-- 9 index my names score

-- index for first char of name and score in names
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
