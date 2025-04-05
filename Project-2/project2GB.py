#Grace Brisco
#sorry i didnt start sooner, Ive spent the entire break doing my senior project and working a lot
#I know Im doing this last minute which is my fault, sorry again


import threading
import time
import multiprocessing
import asyncio
 
def is_prime(n): #your function
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def highest_prime_threading(shared_prime): #Im not gonna lie, i tried to do this my own way without the shared, then the evil ai told me to used this shared prime and it worked (kinda)
    start_time = time.time()               #Its only putting out a number sometimes so I will be back on this to fix it in the next day or so
    number = 0
    while time.time() - start_time < 180:
        if is_prime(number):
            shared_prime.value = number
        number += 1

def highest_prime_mp(shared_prime): 
    start_time = time.time()
    number = 0
    while time.time() - start_time < 180:
        if is_prime(number):
            shared_prime.value = number
        number += 1
        
def main():
    highest_prime_threading_value = [0] #clearly the shared isnt working tho bc why the heck would they share a value when they are two different processes

    thread = threading.Thread(target= highest_prime, args=(highest_prime_threading,))
    thread.start()
    thread.join()
    print(f"The highest prime found: {highest_prime_threading_value[0]}")

    highest_prime_mp_value = multiprocessing.Value('i',0)

    prime_mp = multiprocessing.Process(target=highest_prime, args=(highest_prime_mp,))
    prime_mp.start()
    prime_mp.join()
    print(f"The highest prime found is : {highest_prime_mp_value}")



if __name__ == "__main__":
    main()
#yes i know it doesnt run well at all
#i have spent hours on this, I was working with the homies on it but I wanted to see if there were other ways to do it without totally ripping off of theirs like a freeloader
#apologies again, it will be done