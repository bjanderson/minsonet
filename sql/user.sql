-- SELECT name FROM sqlite_master
-- WHERE type='table' AND name='user';

CREATE TABLE IF NOT EXISTS user (
    pk TEXT NOT NULL PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL
);

INSERT INTO user (pk, email, name)
VALUES ('user1', 'user_1@email.tld', 'user 1');

INSERT INTO user (pk, email, name)
VALUES ('user2', 'user_2@email.tld', 'user 2');

INSERT INTO user (pk, email, name)
VALUES ('user3', 'user_3@email.tld', 'user 3');

-- UPDATE user
-- SET email='user_one@email.tld', name='user One'
-- WHERE pk == 'user1';

-- SELECT * FROM user;

-- SELECT name, email, pk
-- FROM user
-- WHERE pk == 'user1'
-- ORDER BY name DESC;

-- DELETE FROM user
-- WHERE pk == 'user1';

-- DROP TABLE IF EXISTS user;
