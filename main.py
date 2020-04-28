import pymongo
import uuid

client = pymongo.MongoClient('mongodb://bassoon_user:bassoon_password@localhost:27017/')
db = client['bassoon_db']


def main():
    data = {
        "comment": "+rep даже не стыдно клавишы потыкать.Спасибо за угарный вечер!",
        "tone": 10,
    }
    comments = db.comments
    # comment_id = comments.insert_one(data).inserted_id
    # print(comments.find_one({"_id": comment_id}))
    # comments.delete_one({"_id": comment_id})
    # print(comments.find_one({"_id": comment_id}))
    comment = comments.find_one({"tone": 10})
    if comment is not None:
        print(comments.find_one({"_id": comment['_id']}))
        comments.delete_one({"_id": comment['_id']})
        print(comments.find_one({"_id": comment['_id']}))


if __name__ == '__main__':
    main()
