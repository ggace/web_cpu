import dao.PostDao as postDao

def getPosts():
    return postDao.getPosts()

def getPost(id):
    return postDao.getPost(id)[0]

def insert(title, content, userid):
    return postDao.insert(title, content, userid);