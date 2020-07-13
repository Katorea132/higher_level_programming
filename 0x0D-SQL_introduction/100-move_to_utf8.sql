-- UTFinator
-- like WTFinator but safe
ALTER DATABASE hbtn_0c_0 CHARACTER SET = ut8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
