import pickle
factor_cache = {}
muliple_cache = {}

def init_cache():
    global factor_cache
    global muliple_cache
    try:
        cache_file = open("factor_cache.in", "rb")
        factor_cache = pickle.load(cache_file)
        cache_file.close()
    except:
        pass

    try:
        cache_file = open("multiple_cache.in", "rb")
        muliple_cache = pickle.load(cache_file)
        cache_file.close()
    except:
        pass

def save_cache():
    cache_file = open("factor_cache.in", "wb")
    pickle.dump(factor_cache, cache_file)
    cache_file.close()

    cache_file = open("multiple_cache.in", "wb")
    pickle.dump(muliple_cache, cache_file)
    cache_file.close()

def print_factors(num_list):
    global factor_cache
    sorted_list = sorted(num_list)
    key = tuple(sorted_list)
    if key in factor_cache:
        # Already calculated this one
        # No need to do it again
        print("CACHE")
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
        print("CACHE")
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
    init_cache()

    nums = [10, 5, 2, 20]
    print_factors(nums)
    print_factors(nums)
    print_factors(nums)
    print_multiples(nums)
    print_multiples(nums)

    save_cache()

