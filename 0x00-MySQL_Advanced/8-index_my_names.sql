-- 8 index my names

-- index for first char of name in names
CREATE INDEX idx_name_first ON names (name(1));
