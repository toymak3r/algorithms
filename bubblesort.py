# bubble sort
from random import randint
import time

class BubbleSort:

    MAX_RANGE_INT=10000000

    def sort(self, numbers):
        changed = True
        while changed:
            changed = False
            for x in range(len(numbers)-1,0, -1):
                temp = numbers[x]
                if numbers[x] < numbers[x-1]:
                    numbers[x] = numbers[x-1]
                    numbers[x-1] = temp
                    changed = True
            
        return numbers
    
    def test(self, n_tests, n_elements):
        for x in range(1,n_tests):
            numbers = [randint(1,randint(1,self.MAX_RANGE_INT)) 
                        for _ in range(n_elements)]
            sorted_numbers = numbers
            sorted_numbers.sort()
            result = self.sort(numbers)
            
            if result == sorted_numbers:
                result_test = "OK"
            else:
                result_test = "NOK"

            print("teste {} : {}".format(x,result_test))
            print("sorted by sort(): {}".format(sorted_numbers))
            print("sorted by function: {}".format(result))


print("Using Own BubbleSort Function: \n")
numbers = [2,3,10,40,4,1,20]
b = BubbleSort()
start_time = time.time()
print(b.sort(numbers))
print("--- %s seconds ---" % (time.time() - start_time)+"\n")

print("Using Sort() Python Function: \n")
numbers = [2,3,10,40,4,1,20]
start_time = time.time()
numbers.sort()
print(numbers)
print("--- %s seconds ---" % (time.time() - start_time)+"\n")
