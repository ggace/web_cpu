import dao.SampleDao as sampleDao

def sample(sample):
    dbResult = sampleDao.sample(sample)
    
    return dbResult[0]