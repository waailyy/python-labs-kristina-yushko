que_elements_gen(lst):
    seen = set()
    for elem in lst:
        if elem not in seen:
            seen.add(elem)
            yield elem


def reverse_list_gen(lst):
    for elem in reversed(lst):
        yield elem


def cartesian_product_gen(lst1, lst2):
    for elem1 in lst1:
        for elem2 in lst2:
            yield (elem1, elem2)


def permutations_gen(lst):
    for perm in itertools.permutations(lst):
        yield perm


def combinations_gen(lst):
    for r in range(1, len(lst) + 1):
        for comb in itertools.combinations(lst, r):
            yield comb


def tuple_list_gen(lst):
    for tup in lst:
        yield tup


def parallel_lists_gen(*lists):
    for elems in zip(*lists):
        yield elems


def flatten_list_gen(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_gen(item)
        else:
            yield item


def nested_dict_gen(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_gen(value)
        else:
            yield (key, value)


def powers_of_two_gen(n):
    for i in range(n + 1):
        yield 2  i


def powers_of_base_gen(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base


def squares_gen(start, end):
    for num in range(start, end + 1):
        yield num  2


def cubes_gen(start, end):
    for num in range(start, end + 1):
        yield num  3


def factorials_gen(n):
    for i in range(n + 1):
        yield math.factorial(i)


def collatz_seq_gen(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1


def geometric_prog_gen(initial, ratio, limit):
    """Generates a geometric progression up to a limit."""
    term = initial
    while term <= limit:
        yield term
        term *= ratio


""" Task 33: Arithmetic Progression Generator """


def arithmetic_prog_gen(initial, diff, limit):
    term = initial
    while term <= limit:
        yield term
        term += diff


""" Task 34: Running Sum Generator """


def running_sum_gen(nums):
    """Generates running sums of a list of numbers."""
    total = 0
    for num in nums:
        total += num
        yield total


""" Task 35: Running Product Generator """


def running_product_gen(nums):
    """Generates running products of a list of numbers."""
    total = 1
    for num in nums:
        total *= num
        yield total
зроби мені з цього коду зіп файл