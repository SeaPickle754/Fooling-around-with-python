import matplotlib.pyplot as plt
import random

def main():
    while True:
        numbers=[]
        seed_input=int(input('Enter A seed: '))
        if seed_input == 0000:
            break
        random.seed(seed_input)
        for i in range(1,100):
            rand=random.randint(1,100)
            numbers.append(rand)
        fig,ax=plt.subplots()
        plt.plot(numbers)
        plt.show()
main()
