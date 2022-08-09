def get_params(params_str:str):
    params = {}
    for s in params_str.split("&"):
        param = s.split("=")
        if(param != []):
            params[param[0]] = param[1]
    return params