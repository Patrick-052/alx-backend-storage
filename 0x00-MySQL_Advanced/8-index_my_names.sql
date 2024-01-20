-- Creating an index on the first letter of the name in table names
-- This is done by prefixing the column name with the number of characters to index
-- This is useful when you have a lot of rows and you want to filter on a column

CREATE INDEX idx_name_first ON names (name(1));
