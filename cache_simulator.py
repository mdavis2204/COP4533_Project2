import sys

DEFAULT_INPUT_FILE = "inputs/example_input1.txt"

# "First In First Out" algorithm
def fifo(cache_size, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache:
            continue
        if len(cache) < cache_size:
            cache.append(request)
        else:
            cache.pop(0)
            cache.append(request)
            misses += 1
    return misses

if __name__ == '__main__':
    # input files are stored in the inputs folder, pass the path as a argument
    input_file = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT_FILE

    with open(input_file) as file:
        first_line = file.readline().strip()
        second_line = file.readline().strip()

    k = int(first_line.split(" ")[0])
    print("[INFO]: Cache size: ", k)
    
    requests = []
    for i, request in enumerate(second_line.split(" ")):
        request = int(request)
        requests.append(request)
    print("[INFO]: Requests: ", requests)

    fifo_misses = fifo(k, requests.copy())

    print("[OUTPUT]: FIFO misses: ", fifo_misses)