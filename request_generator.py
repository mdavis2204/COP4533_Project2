# Manually set cache size (non-zero based) and number of requests (non-zero based)
# Prints out cache size, number of requests, then a new line of

# Cache Size is the size of the cache excluding 0, 0 1 2 3 would be 4
cache_size = 16

# Request num is the number of requests excluding 0
request_num = 50

# Request multiplier times cache_size is the max number of requests
request_multiplier = 4

print(cache_size, request_num)

import random
for _ in range(request_num):
    print(random.randrange(0, cache_size * request_multiplier), end=" ")