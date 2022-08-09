import dao.Connect as connect

def sample(sample):
    
    sql = f'''
        SELECT test2 FROM sample WHERE test1=\"{sample}\"
    '''
    
    connect.connect()
    result = connect.execute(sql)
    connect.closeDB()
    return result;