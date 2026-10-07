# @author Jakub Kijek, Informatyka, sem. 1, gr. 2
# @date 2026.10.07

import math
import random

# We can approximate the area of a disk enclosed in
# a square by using the distance formula to determine
# if random points lay inside or ouside the disk.
# From the ratio of these areas we can derive pi.
# 
# ratio = disk_num / square_num
# disk_num = pi * r ^ 2
# square_num = 4 * r ^ 2
# ratio = 4 / pi
# pi = 4 * ratio


def calc_pi(iter: int) -> float:
    num = 0

    for _ in range(iter):
        x = random.random()
        y = random.random()
        
        if math.hypot(x, y) <= 1:
            num += 1

    return (num / iter) * 4    

pi = calc_pi(1000)
print(f"{pi=}")
