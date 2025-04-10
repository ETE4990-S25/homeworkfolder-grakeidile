#Grace Brisco
#sorry i didnt start sooner, Ive spent the entire break doing my senior project and working a lot to pay the bills


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

def highest_prime_calculator(queue, duration = 180): #Im not gonna lie, i tried to do this my own way without the shared, then the evil ai told me to used a shared prime and then queue so i tried both 
    start_time = time.time() #Its only putting out a number sometimes hrmmm
    n = 0
    highest_prime = 1
    while time.time() - start_time < 180:
        if is_prime(n):
            highest_prime = n #this is the kind of method I wanted to use on the game but wasnt sure how until now!
        n += 1
    queue.put(highest_prime)
#i was checking a bunch of places like stackoverflow, quora and reddit, but they all used like different imports so this seemed like the best fit

        
def main():
    duration = 180 #is this redundant to put it twice

    print("finding your primes...i guess")

    queue = multiprocessing.Queue()
    mp_prime = multiprocessing.Process(target=highest_prime_calculator, args=(queue,duration))
    mp_prime.start()
    mp_prime.join()

    t_prime = []
    thread_prime = threading.Thread(target=)
    thread_prime.start()
    thread_prime.join()

    a_prime = asyncio.run()

    mp_prime = queue.get()
    thread_prime = t_prime[0]
    async_prime = a_prime

    print(f"Multiprocessing : {mp_prime}")
    print(f"Threading : {thread_prime}")
    print(f"Async : {async_prime}")

if __name__ == "__main__":
    main()
#yes i know it doesnt run well at all
#please spare me I am dying 