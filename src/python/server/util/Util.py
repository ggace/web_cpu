import cryptocode

def reverse(text):
    return text[::-1]

def encoding(text):
    charList =[]

    for t in text:
        charList.append(ord(t))

    rsText = ""

    for c in charList:
        temp = chr(int(reverse(str(c))))
        
        rsText += temp
        
    return rsText
  


def get_params(params_str:str):
    params = {}
    for s in params_str.split("&"):
        param = s.split("=")
        if(param != []):
            params[param[0]] = param[1]
    return params

def pw_encoding(text: str):
    passkey = "cpuServer"
    cipher = cryptocode.encrypt(encoding(text), passkey)
    return cipher