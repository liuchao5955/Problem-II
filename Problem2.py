'''
Created on 2012-8-10

@author: Administrator
'''
i = -123
def method(n):
    result = 0
    if n < 0:
        n = n * -1
        while n != 0:
            result = result * 10 + n % 10
            n /= 10
        return result * -1    
    while n != 0:
        result = result * 10 + n % 10
        n /= 10
    return result
print method(i)
       
                                                           tow     ++++++++++++++++++++++++++++
