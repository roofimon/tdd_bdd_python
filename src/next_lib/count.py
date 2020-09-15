from functools import reduce

def some_function():
    return 42

def cucumber(start):
    return dict(start=start, eat=0)

# def convertx(number):
#     condition = [(number % 3 == 0), (number % 5 == 0), (number % 7 == 0)]
#     if condition == [False, False,  False]:
#         message = str(number)
#     if condition == [True,  False,  False]:
#         message = "Pling"
#     if condition == [False, True,   False]:
#         message = "Plang"
#     if condition == [False, False,  True]:
#         message = "Plong"        
#     if condition == [True,  True,   False]:        
#         message = "PlingPlang"
#     if condition == [False, True,   True]:        
#         message = "PlangPlong"        
#     if condition == [True,  False,  True]:        
#         message = "PlingPlong"        
#     if condition == [True,  True,   True]:        
#         message = "PlingPlangPlong"              
#     return message

def convert(number):
    message = pling_plang_plong(number)
    return or_else(message, number)

pling_plang_plong = lambda number: reduce((lambda x, y: x+y), [pling(number), plang(number), plong(number)])
or_else = lambda message, number: message if message != '' else str(number)

def pling(number):
    return "Pling" if (number % 3 == 0) else ""

def plang(number):
    return "Plang" if (number % 5 == 0) else ""

def plong(number):
    return "Plong" if (number % 7 == 0) else ""


# def convert(number):
#     r = pling_plang_plong(number)
#     return r["message"]
    
# pling_plang_plong = lambda number: any_of(plong(plang(pling({"number": number, "message": ""}))))

# def pling(dic):
#     if (dic["number"] % 3 == 0): 
#         dic["message"] = dic["message"]+"Pling"
#     return dic

# def plang(dic):
#     if (dic["number"] % 5 == 0): 
#         dic["message"] = dic["message"]+"Plang"
#     return dic

# def plong(dic):
#     if (dic["number"] % 7 == 0): 
#         dic["message"] = dic["message"]+"Plong"
#     return dic

# def any_of(dic):
#     return dic["message"] if dic["message"] != "" else {"message": str(dic["number"])}