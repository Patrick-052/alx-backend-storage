-- Creating an index on first letters of name and score in table names
-- Advantage: you can filter on both columns using this index thus making the query faster

CREATE INDEX idx_name_score_first IF NOT EXISTS ON names (name(1), score);
