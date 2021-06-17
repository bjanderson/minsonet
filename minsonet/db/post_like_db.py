from ..models import PostLike


class PostLikeDB:
    def __init__(self, db):
        self.db = db
        self.create_table()

    @property
    def table_name(self):
        return "post_like"

    @property
    def table_column_definitions(self):
        # Note: these columns must be in the same order as the property assignments in the Post class or the mappings will break
        return [
            "postPK TEXT NOT NULL",
            "userPK TEXT NOT NULL",
            "FOREIGN KEY(postPK) REFERENCES post(pk) ON DELETE CASCADE",
            "FOREIGN KEY(userPK) REFERENCES user(pk)",
            "PRIMARY KEY(postPK, userPK)",
        ]

    def create_item(self, tup):
        post = PostLike.from_tuple(tup)
        return post

    def create_table(self):
        stmt = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({', '.join(self.table_column_definitions)});"
        self.db.execute(stmt)

    def insert(self, item):
        print(f"insert item: {item}")
        try:
            cols = "postPK, userPK"
            vals = f"{item['postPK']}, {item['userPK']}"
            stmt = f"INSERT INTO {self.table_name} ({cols}) VALUES ({vals})"
            self.db.execute(stmt)
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            print(message)
        return self.get(item["pk"])

    def delete(self, postPK, userPK):
        stmt = f"DELETE FROM {self.table_name} WHERE postPK = '{postPK}' AND userPK = '{userPK}';"
        self.db.execute(stmt)

    def get_number_of_likes_for_post(self, postPK):
        stmt = f"SELECT postPK, COUNT(DISTINCT userPK) as num_likes FROM {self.table_name} WHERE postPK = '{postPK}';"
        result = self.db.fetchone(stmt)
        return result[1]

    def get_posts_liked_by_user(self, userPK):
        pass
