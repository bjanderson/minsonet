
CREATE TABLE IF NOT EXISTS comment (
    pk TEXT NOT NULL PRIMARY KEY,
    parentCommentPK TEXT,
    postPK TEXT NOT NULL,
    commenterPK TEXT NOT NULL,
    comment TEXT NOT NULL,
    createdAt TEXT NOT NULL,
    FOREIGN KEY(parentCommentPK) REFERENCES comment(pk),
    FOREIGN KEY(postPK) REFERENCES post(pk),
    FOREIGN KEY(commenterPK) REFERENCES user(pk)
);

INSERT INTO comment (pk, parentCommentPK, postPK, commenterPK, comment, createdAt)
VALUES ('comment1', null, 'post1', 'user1', 'comment 1', datetime('now'));

INSERT INTO comment (pk, parentCommentPK, postPK, commenterPK, comment, createdAt)
VALUES ('comment2', 'comment1', 'post1', 'user2', 'comment 2', datetime('now'));

INSERT INTO comment (pk, parentCommentPK, postPK, commenterPK, comment, createdAt)
VALUES ('comment3', null, 'post1', 'user1', 'comment 3', datetime('now'));

-- UPDATE comment
-- SET comment='other comment 1'
-- WHERE pk == 'comment1';

-- SELECT pk, parentCommentPK, postPK, commenterPK, comment, createdAt
-- FROM comment
-- WHERE pk == 'comment1';

-- DELETE FROM comment
-- WHERE pk == 'comment1';

-- DROP TABLE IF EXISTS comment;

-- get all comments for a post,
-- and sort them by the date they were created
SELECT pk, parentCommentPK, postPK, commenterPK, comment, createdAt
FROM comment
WHERE postPK == 'post1'
ORDER BY createdAt DESC;
