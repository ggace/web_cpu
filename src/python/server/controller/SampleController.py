import dto.ResultData as ResultData

import service.SampleService as sampleService

def sample(params):
    resultData = ResultData.ResultData("S-1", "샘플 출력", "sample", sampleService.sample(params["sample"]))
    return resultData