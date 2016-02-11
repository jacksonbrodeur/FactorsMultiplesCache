import pickle
factor_cache = {}
muliple_cache = {}

def init_factor_cache(file_name):
    global factor_cache
    cache_file = open(file_name, "rb")
    factor_cache = pickle.load(cache_file)
    cache_file.close()

def save_factor_cache(file_name):
    cache_file = open(file_name, "wb")
    pickle.dump(factor_cache, cache_file)
    cache_file.close()

def print_factors(num_list):
    global factor_cache
    sorted_list = sorted(num_list)
    key = tuple(sorted_list)
    if key in factor_cache:
        # Already calculated this one
        # No need to do it again
        print(factor_cache[key])
        return
    factor_list = {}
    for i in range(0, len(sorted_list)):
        factors = []
        for j in range(0, i):
            if sorted_list[i] % sorted_list[j] == 0:
                factors.append(sorted_list[j])
        factor_list[sorted_list[i]] = factors

    print(factor_list)
    factor_cache[key] = factor_list

def print_multiples(num_list):
    global muliple_cache
    sorted_list = sorted(num_list)
    key = tuple(sorted_list)
    if key in muliple_cache:
        # Already calculated this one
        # No need to do it again
        print(muliple_cache[key])
        return
    multiple_list = {}
    for i in range(0, len(sorted_list)):
        multiples = []
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] % sorted_list[i] == 0:
                multiples.append(sorted_list[j])
        multiple_list[sorted_list[i]] = multiples

    print(multiple_list)
    muliple_cache[key] = multiple_list


if __name__ == "__main__":
    init_factor_cache("factor_cache.in")

    nums = [10, 5, 2, 20]
    print_factors(nums)
    print_factors(nums)
    print_factors(nums)
    print_multiples(nums)
    print_multiples(nums)

    save_factor_cache("factor_cache.in")

