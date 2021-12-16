def isIncreasing(list):
    first = list[0]
    for i in range(len(list)-2):
        if list[i] < list[i+1] < list[i+2]<list[i+3]:
            return True
        else:
            return False
        
            
        
def numconvert(num):
    result = ""
    
    for i in num:
        x = str(i)
        y = "".join(x)
        result = result + y
        answer = int(result)
    return result
   


def binconvert(binary):
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
    print("Question 1")
    print("Example of Increascing Values [1,2,3,4]:", isIncreasing([1,2,3,4]))
    print("Example that will return False [1,2,1,4]:", isIncreasing([1,2,1,4]))
    print("")
    print("Question 2")
    print("[3,5,1] turns into:", numconvert([3,5,1]))
    print("")
    print("Question 3")
    print("binary 10 turns into decimal", binconvert(10))

if __name__ == "__main__":
    test()
    