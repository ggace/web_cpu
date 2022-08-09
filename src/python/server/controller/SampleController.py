import dto.ResultData as ResultData

import dto.ErrorCode as errorCode
import service.SampleService as sampleService

def sample(params):
    if "sample" in params:
    
        resultData = ResultData.ResultData(errorCode.S_1, "샘플 출력", "sample", sampleService.sample(params["sample"]))
    else:
        resultData = ResultData.ResultData(errorCode.F_null, "null exception")
    return resultData