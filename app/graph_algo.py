import time
import matplotlib.pyplot as plt

class FastExponentiation:
    @staticmethod
    def get_time(base, exp):
        start = time.time()
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result *= base
            base *= base
            exp //= 2
        end = time.time()
        return end - start


class NaiveExponentiation:
    @staticmethod
    def get_time(base, exp):
        start = time.time()
        result = 1
        for _ in range(exp):
            result *= base
        end = time.time()
        return end - start


class Simulation:
    def __init__(self):
        self.base = 2
        self.start_exponent = int(input("Enter starting exponent: "))
        self.end_exponent = int(input("Enter ending exponent: "))
        self.step = int(input("Enter step size: "))

    def graph(self):
        x_values = []
        fast_times = []
        naive_times = []

        exponent = self.start_exponent

        while exponent <= self.end_exponent:
            fast_time = FastExponentiation.get_time(self.base, exponent)
            naive_time = NaiveExponentiation.get_time(self.base, exponent)

            x_values.append(exponent)
            fast_times.append(fast_time)
            naive_times.append(naive_time)

            exponent += self.step

        plt.plot(x_values, fast_times, marker='o', label='Fast Exponentiation')
        plt.plot(x_values, naive_times, marker='x', label='Naive Exponentiation')
        plt.xlabel("Exponent")
        plt.ylabel("Runtime (seconds)")
        plt.title("Fast vs Naive Exponentiation Simulation")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


def main():
    sim = Simulation()
    sim.graph()


if __name__ == "__main__":
    main()
