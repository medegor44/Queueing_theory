#M/M/1

import random
import math

L = 1
M = 3


def generate_incoming_requests(n):
    t = [0]
    for i in range(n - 1):
        w = random.random()
        t.append(-math.log(1 - w) / L + t[-1])

    return t


def generate_service_times(n):
    y = []

    for i in range(n):
        w = random.random()
        y.append(-math.log(1 - w) / M)

    return y


def main():
    n = int(input())

    incoming = generate_incoming_requests(n)
    service_time = generate_service_times(n)

    current_time = 0

    gamma_queue = 0
    gamma_system = 0
    queue_time = 0

    print("Поступила в СМО     | Поступила на прибор | Вышла из СМО        | Время в очереди     | Время на приборе    | Время в системе    ")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    for i in range(n):
        current_time = max(current_time, incoming[i])
        queued_time = current_time - incoming[i]
        done_time = current_time + service_time[i]
        on_system_time = done_time - incoming[i]

        print(f"{incoming[i]:=19.5f} | {current_time:=19.5f} | {done_time:=19.5f} | {queued_time:=19.5f} | {service_time[i]:=19.5f} | {on_system_time:=19.5f}")

        current_time = done_time
        queue_time = done_time - service_time[i]

        gamma_queue += queued_time
        gamma_system += done_time

    print(f"Средняя длина очереди: {gamma_queue / queue_time}")
    print(f"Средняя длина очереди (стационарное значение): {(L/M)**2 / (1 - L/M)}")

    T_t = gamma_system / n
    lambda_t = n / current_time
    N_t = gamma_system / current_time

    print(f"T_t = {T_t}")
    print(f"lambda_t = {lambda_t}")
    print(f"N_t = {N_t}")


main()
