
CREATE TABLE IF NOT EXISTS password (
    userPK TEXT NOT NULL PRIMARY KEY,
    password TEXT NOT NULL,
    FOREIGN KEY(userPK) REFERENCES user(pk)
);

INSERT INTO password (userPK, password)
VALUES ('user1', 'Password_1');

INSERT INTO password (userPK, password)
VALUES ('user2', 'Password_2');

INSERT INTO password (userPK, password)
VALUES ('user3', 'Password_3');

-- UPDATE password
-- SET password='Password_One'
-- WHERE userPK == 'user1';

-- SELECT password, userPK
-- FROM password
-- WHERE userPK == 'user1';

-- DELETE FROM password
-- WHERE userPK == 'user1';

-- DROP TABLE IF EXISTS password;
