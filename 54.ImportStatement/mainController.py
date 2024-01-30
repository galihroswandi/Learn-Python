
def mathematicsController(*args, **kwargs)->float:
    if(kwargs["option"] == "tambah"):
        output = 0
        for i in args:
            output += i
        return output
    elif(kwargs['option'] == "kali"):
        output = 1
        for i in args:
            output *= i
        return output
    else: 
        return "Tidak ada opersi yang dikerjakan"