from database import Database
from blog import Blog
class Menu(object):
    def __init__(self):
        self.user=input("Enter auther name ")
        self.user_blog=None
        if self._check() :
            print('Welcome Back {}'.format(self.user))
        else:
            self._newpost()
    
    def _check(self):
        blog=Database.find_one('blogs',{"author":self.user})
        if blog is not None:
            self.user_blog=Blog.from_mongo(blog['id'])
            return True
        else:
            return False
        
        
    def _newpost(self):
        description=input("Enter content ")
        title=input("Enter title ")
        blog=Blog(author=self.user,title=title,description=description)
        blog.save()
        self.user_blog=blog
    def run_menu(self):
        rw=input("Do you want to R or W")
        if rw is 'R':
            self._list()
            self._view()
        elif rw is 'W':
            (self.user_blog).new_post()
        else:
            print('Thanku')

    def _list(self):
        posts=Database.find('blogs',data={})
        for post in posts:
            print("ID:{},author:{},title:{}".format(post['id'], post['author'], post['title']))
    def _view(self):
        id=input("Enter id ")
        blog=Blog.from_mongo(id)
        posts=blog.get_posts()
        for post in posts:
            
            print('Date:{},title:{}/n/n,content:{}'.format(post['date'],post['title'],post['content']))
