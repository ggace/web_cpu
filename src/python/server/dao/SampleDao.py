import dao.Connect as connect

def sample(sample):
    
    sql = f'''
        SELECT test2 FROM sample WHERE test1=\"{sample}\"
    '''
    
    result = connect.sqlRun(sql)
    return result