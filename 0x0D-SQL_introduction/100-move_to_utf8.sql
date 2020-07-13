-- script that converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARSET = utf8mb4 COLLATE=utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
