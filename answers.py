def isIncreasing(list):
    count = 0
    first = list[0]
    for i in list:
        if first < i:
            i
    #     else:
    #         return False
    # return True
            
   
 
        
        
def numconvert(num):
    result = ""
    
    for i in num:
        x = str(i)
        y = "".join(x)
        result = result + y
        answer = int(result)
    return result
   


def bitconvert(binary):
    result = 0
    value = 1
    bin = str(binary)
    for i in bin[::-1]:
        if i == "1":
            result = result + value
        value = value * 2
    return result 
        




def test():
    increasing_nums = [1,2,3]
    print(isIncreasing(increasing_nums))
    print(numconvert([3,5,1]))
    print(bitconvert(10))

if __name__ == "__main__":
    test()
    