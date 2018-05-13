import uuid,datetime
from database import Database

class Post(object):
    def __init__(self,title,content,blog_id,author,date=datetime.datetime.utcnow(),id=None):
        self.title=title
        self.content=content
        self.blog_id=blog_id
        self.author=author
        if id is None:
            self.id=uuid.uuid4().hex
        else:
            self.id=id
        self.date=date
    def save(self):
        Database.insert(collection='posts',data=self.json())
    def json(self):
        return {"title":self.title,
                "content":self.content
                ,"author":self.author
                ,"date":self.date
                ,"id":self.id
                ,"blog_id":self.blog_id}
    @classmethod
    def from_mongo(cls,id):
        post_data=Database.find_one(collection='posts',data={'id':id})
        return cls(title=post_data['title'],content=post_data['content'],blog_id=post_data['blog_id'],author=post_data['author'],
                   date=post_data['date'])
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',data={'blog_id':id})]
