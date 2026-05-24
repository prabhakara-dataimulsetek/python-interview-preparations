from collections import OrderedDict

def simulate_lru(capacity, operations):
    cache = OrderedDict()
    result = []
    for op in operations:
        if op[0] == "GET":
            key = op[1]
            if key in cache:
                cache.move_to_end(key)
                result.append(cache[key])
            else:
                result.append(-1)
        else:
            _, key, value = op
            if key in cache:
                cache.move_to_end(key)
            cache[key] = value
            if len(cache) > capacity:
                cache.popitem(last=False)
    return result, list(cache.items())
