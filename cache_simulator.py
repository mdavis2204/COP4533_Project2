import sys

DEFAULT_INPUT_FILE = "inputs/test_input1.txt"

# "First In First Out" algorithm
def fifo(cache_size, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache:
            continue
        misses += 1
        if len(cache) < cache_size:
            cache.append(request)
        else:
            cache.pop(0)
            cache.append(request)
    return misses

# Least Recently Used algorithm
def lru(cache_size, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache:
            cache.pop(cache.index(request))
            cache.append(request)
        else:
            misses += 1
            if len(cache) < cache_size:
                cache.append(request)
            else:
                cache.pop(0)
                cache.append(request)
    return misses

# Farthest Future algorithm (OPTFF)
def optff(cache_size, requests):
    cache = []
    misses = 0
    n = len(requests)

    # Finds next occurence of ID after lookahead_index
    def next_use(item, lookahead_index):
        for j in range(lookahead_index + 1, n):
            if requests[j] == item:
                return j
        return n

    for i, request in enumerate(requests):
        if request in cache:
            continue
        misses += 1
        if len(cache) < cache_size:
            cache.append(request)
        else:
            farthest_index = -1
            evict_item = None
            for item in cache:
                j = next_use(item, i)
                if j > farthest_index:
                    farthest_index = j
                    evict_item = item
            cache.remove(evict_item)
            cache.append(request)
    return misses

if __name__ == '__main__':
    # input files are stored in the inputs folder, pass the path as a argument
    input_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT_FILE

    with open(input_file) as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()

    k = int(first_line.split(" ")[0])

    requests = []
    for i, request in enumerate(second_line.split(" ")):
        request = int(request)
        requests.append(request)

    fifo_misses = fifo(k, requests.copy())
    lru_misses = lru(k, requests.copy())
    optff_misses = optff(k, requests.copy())

    out_str = (
        f"FIFO  : {fifo_misses}\n"
        f"LRU   : {lru_misses}\n"
        f"OPTFF : {optff_misses}"
    )


    # output to console and file
    print(out_str)

    with open("cache_simulator.out", "w") as file:
        file.write(out_str)