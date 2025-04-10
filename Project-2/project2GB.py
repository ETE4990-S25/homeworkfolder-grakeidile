#Grace Brisco
#sorry i didnt start sooner, Ive spent the entire break doing my senior project and working a lot to pay the bills

import threading
import time
import multiprocessing
#import asyncio
 
def is_prime(n): #your function
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def highest_prime_calculator(queue=None, result=None, duration = 10): #Im not gonna lie, i tried to do this my own way, then the evil ai told me to used a shared prime and then queue so i tried both 
    start_time = time.time() #Its only putting out a number sometimes hrmmm
    n = 0
    highest_prime = 1
    while time.time() - start_time < duration:
        if is_prime(n):
            highest_prime = n #this is the kind of method I wanted to use on the game but wasnt sure how until now!
        n += 1
    queue.append(highest_prime)

#i was checking a bunch of places like stackoverflow, quora and reddit, but they all used like different imports we dont know so this seemed like the best fit

        
def main():
    duration = 10
    print("finding your primes...i guess")

    queue = multiprocessing.Queue()
    mp_prime = multiprocessing.Process(target=highest_prime_calculator, args=(queue,None, duration))
    mp_prime.start()

    t_prime = []
    thread_prime = threading.Thread(target=highest_prime_calculator, args=(None, t_prime, duration))
    thread_prime.start()

    #a_prime = asyncio.run(highest_prime_calculator(duration))
    #so I would run this but sources are telling me it is throwing an error because of the base I am using for python and that it is the wrong version
    mp_prime.join()
    thread_prime.join()

    mp_prime = queue.get()
    thread_prime = t_prime[0]
    #async_prime = a_prime

    print(f"Multiprocessing : {mp_prime}")
    print(f"Threading : {thread_prime}")
    #print(f"Async : {async_prime}")

if __name__ == "__main__":
    main()
#yes i know it doesnt run well at all
#I used chatgpt and the homies codes as references but im still having trouble. Its timing fine, just not calculating
#tbh im trying to get my meds approved so I dont go into a flare and im mega stressed out so I will get back to this soon again
#sorry