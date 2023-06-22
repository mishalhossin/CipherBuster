import string
import itertools
import time
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

max_length = 8

def check_code(code):
    """
    Function to check if the given code matches the target code.
    """
    if code == target_code:
        return code
    return None

def brute_force(length):
    """
    Function to perform brute-forcing for a given code length.
    """
    for code in itertools.product(charset, repeat=length):
        code = ''.join(code)
        result = check_code(code)
        if result:
            return result

if __name__ == '__main__':
    target_code = input("Enter the target code: ")

    found = False

    for length in range(1, max_length + 1):
        pool = Pool(cpu_count())
        codes = pool.map(brute_force, [length] * cpu_count())
        pool.close()

        for code in tqdm(codes, desc=f"Length {length}", unit="code"):
            if code:
                found = True
                break

        if found:
            break

    if found:
        print(f"Code found: {code}")
    else:
        print("Code not found.")
