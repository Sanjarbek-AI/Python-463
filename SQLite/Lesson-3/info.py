"""Bugungi mavzular:

1. INTEGER PRIMARY KEY AUTOINCREMENT
2. NULL | UNIQUE | qo'yib ketish
3. UPDATE and DELETE
4. SELECT and INSERT
5. ORDER BY | ASC | DESC | MAX | MIN | COUNT | SUM | DISTINCT |
6. TEXT, INTEGER, NULL, REAL, BLOB
7. CREATE TABLE
8. DROP TABLE IF EXISTS

--------------------------------------------------------------------
UPDATE tabel_name SET column=value, coulmn1=value1 WHERE expression;
--------------------------------------------------------------------
DELETE FROM table_name WHERE expression;
--------------------------------------------------------------------
SELECT * FROM tabel_name ORDER BY rowid DESCorASC;
--------------------------------------------------------------------
DROP TABLE IF EXISTS TableName;
--------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Projects (
    ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProjectName TEXT,
    StartDate TEXT,
    EndDate TEXT NULL, -- This column allows NULL values
    Status TEXT
)

---------------------------------------------------------------------

Mashqlar:

1.  

"""