import math
import Model

L = 1/3
M = 2/3

K = 1
alpha = 3


def main():
    def incoming(w):
        return -math.log(1 - w) / L

    def service_exp(w):
        return -math.log(1 - w) / M

    def service_pa(w):
        return K / math.pow(1 - w, 1 / alpha)

    def queue_length_exp():
        return (L / M) ** 2 / (1 - L / M)

    def queue_length_pa():
        return None

    n = int(input())
    Model.compute(incoming, service_exp, queue_length_exp, n)
    Model.compute(incoming, service_pa, queue_length_pa, n)


main()
