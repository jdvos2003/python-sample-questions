def find_outlier(integers):
    odd = filter(lambda x: x % 2 == 1, integers)
    even = filter(lambda x: x % 2 == 0, integers)
    return odd[0] if len(odd) == 1 else even[0]