-- converts hbtn_0c_0 database to UTF8
SELECT CCSA.character_set_name 
FROM information_schema.TABLES T,
information_schema.COLLATION_CHARACTER_SET_APPLICABILITY CCSA 
WHERE CCSA.collation_name = T.table_collation 
AND T.table_schema = "hbtn_0c_0" 
AND T.table_name = "first_table"
AND T.table_name = "name";
