
CREATE TABLE IF NOT EXISTS password (
    password TEXT NOT NULL,
    userPK TEXT NOT NULL PRIMARY KEY,
    FOREIGN KEY(userPK) REFERENCES user(pk)
);

INSERT INTO password (password, userPK)
VALUES ('Password_1', 'userpk1');

INSERT INTO password (password, userPK)
VALUES ('Password_2', 'userpk2');

INSERT INTO password (password, userPK)
VALUES ('Password_3', 'userpk3');

-- UPDATE password
-- SET password='Password_One'
-- WHERE userPK == 'userpk1';

-- SELECT password, userPK
-- FROM password
-- WHERE userPK == 'userpk1';

-- DELETE FROM password
-- WHERE userPK == 'userpk1';

-- DROP TABLE IF EXISTS password;
