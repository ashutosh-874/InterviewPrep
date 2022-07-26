# def generate_valid_parentheses(num):

#     # in the solution , i basically added '(' wherever it is possible like at 0th position
#     # or at the end, for inserting midway, '(' should not be inserted after ')
#     # i added each generated o/p to a set to overcome making duplicates
    
#     result = set()
#     result.add("()")

#     for i in range(num - 1):
#         # print(result)
#         old_set = set(result)
#         new_set = set()
#         for _ in range(len(old_set)):
#             el = old_set.pop()
#             x = 0
#             while x <= len(el):
#                 # print(f"{x}th iteration")
#                 # print(el[:x] + '(' + el[x:] + ')')
#                 if el[x - 1] != ")" or x == len(el):
#                     new_set.add(el[:x] + '(' + el[x:] + ')')
#                 x += 1

#         result = set(new_set)

#     return list(result)

from collections import deque

def countOpenClose(str):
    open = 0
    for i in str:
        if i == '(': open += 1
    return open, len(str) - open


def generate_valid_parentheses(num):

    results = deque()
    results.append('')
    
    cond = False
    while True:
        if cond:
            break
        ln = len(results)
        for _ in range(ln):
            open, close = countOpenClose(results[0])
            if open == close == num:
                cond = True
                break
            el = results.popleft()
            if open < num:
                results.append(el + '(')
            if close < open:
                results.append(el + ')')
            

    return list(results)






print(generate_valid_parentheses(1))
print(generate_valid_parentheses(2))
print(generate_valid_parentheses(3))
# print(generate_valid_parentheses(4))
# print(generate_valid_parentheses(5))
# print(generate_valid_parentheses(6))

# def main():
#     print("All combinations of balanced parentheses are: " +
#             str(generate_valid_parentheses(2)))
#     print("All combinations of balanced parentheses are: " +
#             str(generate_valid_parentheses(3)))


# main()
