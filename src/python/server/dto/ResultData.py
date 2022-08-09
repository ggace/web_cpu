class ResultData():
    resultCode: str
    msg:str
    dataName: str
    data: object
    def __init__(self, resultCode: str, msg: str, dataName: str, data: object):
        self.resultCode = resultCode
        self.msg = msg
        self.dataName = dataName
        self.data = data

    def to_string(self):
        return """{
            'resultCode': {},
            'msg' : {},
            'dataName' : {},
            'data' : {}
        }""".format(self.resultCode, self.msg, self.dataName, self.data)
