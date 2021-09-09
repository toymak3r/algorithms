import time

def pow(i,p):
	if p >= 1:
		return i * pow(i,p - 1)
	else:
		return 1


def pow1(base, power):
   if ( power != 0 ):
           result = base
           for n in range(power - 1):
               result = result * base
                
           return result        
   else:
         return 1


def test(base,power,resultado):
    result = base ** power
    pair = "("+str(base)+","+str(power)+")"
    if ( result == resultado ):
        RESP = "[OK] "
    else:
        RESP = "[NOK] "

    print ( RESP + pair + " - " + str(result) + " resp: " + str(resultado)+"\n" )



sequence = [(2,3),(4,2),(3,3)]
for x,y in sequence:
       print("Testing Function pow()")
       start_time = time.time()
       test(x,y,pow(x,y)) 
       print("--- %s seconds ---" % (time.time() - start_time)+"\n")

       print("Testing Function pow1()")
       start_time = time.time()
       test(x,y,pow1(x,y))
       print("--- %s seconds ---" % (time.time() - start_time)+"\n")

