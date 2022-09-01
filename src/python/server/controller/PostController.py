import service.PostService as postService
from dto import * 

def getAll(params):
    resultData = ResultData.ResultData(ErrorCode.S_1, "post들 입니다.", "posts", postService.getPosts())
    
    return resultData

def getEach(params):
    
    if "id" in params:
        resultData = ResultData.ResultData(ErrorCode.S_1, f"{params['id']}번 post입니다.", "post", postService.getPost(params["id"]))

    else:
        resultData = ResultData.ResultData(ErrorCode.F_null, "id를 입력해주세요", None, None)
    
    return resultData

def create(params):
    if not("title" in params):
        resultData = ResultData.ResultData(ErrorCode.F_null, "title를 입력해주세요", None, None)
    elif not("content" in params):
        resultData = ResultData.ResultData(ErrorCode.F_null, "content를 입력해주세요", None, None)

    else:
        userid = 1
        postService.insert(params["title"], params["content"], userid)
        resultData = ResultData.ResultData(ErrorCode.S_1, "post 작성을 완료하였습니다.", None, None)
    
    return resultData