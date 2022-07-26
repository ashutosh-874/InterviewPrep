from collections import deque


def find_letter_case_string_permutations(str):
    permutations = deque()
    permutations.append("")

    for c in str:
        ln = len(permutations)
        print(permutations)
        for _ in range(ln):
            el = permutations.popleft()
            permutations.append(el + c)
            if not c.isnumeric():
                permutations.append(el + c.swapcase())

    return list(permutations)


def main():
    print("String permutations are: " +
            str(find_letter_case_string_permutations("a1b2")))
    print("String permutations are: " +
            str(find_letter_case_string_permutations("3z4")))


main()
