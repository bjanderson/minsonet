
CREATE TABLE IF NOT EXISTS post (
    pk TEXT NOT NULL PRIMARY KEY,
    authorPK TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    createdAt TEXT NOT NULL,
    FOREIGN KEY(authorPK) REFERENCES user(pk)
);

INSERT INTO post (pk, authorPK, title, content, createdAt)
VALUES ('post1', 'user1', 'title 1', 'content 1', datetime('now'));

INSERT INTO post (pk, authorPK, title, content, createdAt)
VALUES ('post2', 'user1', 'title 2', 'content 2', datetime('now'));

-- UPDATE post
-- SET title='other title 1', content='other content 1'
-- WHERE pk == 'post1';

-- SELECT pk, authorPK, title, content, createdAt
-- FROM post
-- WHERE pk == 'post1'
-- ORDER BY createdAt DESC;

-- DELETE FROM post
-- WHERE pk == 'post1';

-- DROP TABLE IF EXISTS post;

-- get all posts made by a user,
-- and sort them by the date they were created
SELECT pk, authorPK, title, content, createdAt
FROM post
WHERE authorPK == 'user1'
ORDER BY createdAt DESC;
