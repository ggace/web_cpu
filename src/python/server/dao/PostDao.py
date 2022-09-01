import dao.Connect as connect

def getPosts():
    sql = '''
SELECT p.id, p.title, p.updateDate, u.nickname
FROM posts AS p
JOIN `user` AS u
ON u.id = p.userid
ORDER BY p.updateDate DESC
    '''

    result = connect.sqlRun(sql)

    return result;

def getPost(id):
    sql = f"""
SELECT p.id, p.title, p.updateDate, u.nickname
FROM posts AS p
JOIN `user` AS u
ON u.id = p.userid
WHERE p.id = {id}
ORDER BY p.updateDate DESC
"""
    result = connect.sqlRun(sql)

    return result;

def insert(title, content, userid):
    sql = f"""
INSERT INTO posts(title, content, regDate, updateDate, userid)
VALUES(\"{title}\", \"{content}\", NOW(), NOW(), {userid});
"""
    result = connect.sqlRun(sql)

    return result;