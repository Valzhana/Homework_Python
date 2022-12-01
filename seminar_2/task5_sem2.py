#Task5

import time
start = int(input('Enter start_number: '))
end = int(input('Enter end_number: '))
rand_num = int((time.time() % 1) * (end - start) + start)
print(rand_num)
