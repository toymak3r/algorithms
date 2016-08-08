import time

def inverse(word):
        n = int(len(word))
        i = 1
        new_word = ''
        while (i <= n):
                new_word += word[n-i]
                i += 1
        return new_word              


print("Using Own Rever Function: \n")
start_time = time.time()
print(inverse("casa"))
print("--- %s seconds ---" % (time.time() - start_time)+"\n")

print("Using Python's Reverse Function: \n")
start_time = time.time()
print(("casa")[::-1])
print("--- %s seconds ---" % (time.time() - start_time)+"\n")
