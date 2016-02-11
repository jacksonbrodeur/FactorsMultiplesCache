
def print_factors(num_list):
    sorted_list = sorted(num_list)
    factor_list = {}
    for i in range(0, len(sorted_list)):
        factors = []
        for j in range(0, i):
            if sorted_list[i] % sorted_list[j] == 0:
                factors.append(sorted_list[j])
        factor_list[sorted_list[i]] = factors

    print(factor_list)

if __name__ == "__main__":
    nums = [10, 5, 2, 20]
    print_factors(nums)

