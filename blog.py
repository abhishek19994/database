import uuid,datetime
from database import Database
from post import Post
class Blog(object):
    def __init__(self,author,title,description,id=None):
        self.author=author
        self.title=title
        self.description=description
        self.id=uuid.uuid4().hex if id is None else id
    def new_post(self):
        author=input("Enter auth ")
        title=input("enter title ")
        content=input("enter desc ")
        date=input("enter in DDMMYYYY ")
        if date=="":
            date=datetime.datetime.utcnow()
        else:
            date=datetime.datetime.strptime(date, "%d%m%Y")
        post=Post(title=title,
                  content=content,
                  blog_id=self.id,
                  author=author,date=date)
        post.save()
    def get_posts(self):
        return Post.from_blog(self.id)
    def save(self):
        Database.insert(collection="blogs",data=self.json())
    def json(self):
        return {
            "author":self.author,"title":self.title, "description":self.description
            ,"id":self.id}
    @classmethod
    def from_mongo(cls,id):
        blog_data=Database.find_one(collection="blogs",data={"id":id})
        return cls(author=blog_data['author'],title=blog_data['title'],description=blog_data['description'],
                   id=blog_data['id'])
        #it will return class object
        
        
