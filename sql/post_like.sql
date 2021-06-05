
CREATE TABLE IF NOT EXISTS post_like (
    postPK TEXT NOT NULL,
    userPK TEXT NOT NULL,
    FOREIGN KEY(postPK) REFERENCES post(pk) ON DELETE CASCADE,
    FOREIGN KEY(userPK) REFERENCES user(pk),
    PRIMARY KEY(postPK, userPK)
);

INSERT INTO post_like (postPK, userPK)
VALUES ('post1', 'user1');

INSERT INTO post_like (postPK, userPK)
VALUES ('post1', 'user2');

INSERT INTO post_like (postPK, userPK)
VALUES ('post1', 'user3');

-- DELETE FROM post_like
-- WHERE postPK == 'post1' AND userPK == 'user1';

DROP TABLE IF EXISTS post_like;

-- count how many likes a post has
SELECT postPK, COUNT(DISTINCT userPK) as num_likes
FROM post_like
GROUP BY postPK;
