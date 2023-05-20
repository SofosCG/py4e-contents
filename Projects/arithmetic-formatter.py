import sys


def operation(p):
    a = p[0:p.find(" ")]
    b = p[(p.find(" ")+3):]
    strs = [a, b]

    nums = []
    for n in strs:
        nums.append(int(n))

    if "+" in p:
        nums.append(nums[0]+nums[1])
        nums.append("+")
    else:
        nums.append(nums[0]-nums[1])
        nums.append("-")

    return nums


def with_solution(p):
    nums = operation(p)
    arranged = """{:>10}
    {}{:>5}
    ------
    {:>6}""".format(
        nums[0], nums[3], nums[1], nums[2])

    return arranged


def without_solution(p):
    nums = operation(p)
    arranged = """{:>10}
    {}{:>5}
    ------""".format(
        nums[0], nums[3], nums[1])

    return arranged


def arithmetic_arranger(problems, solution=False):
    if len(problems) > 5:
        sys.exit("Error: Too many problems.")
    for problem in problems:
        if not (("+" in problem) or ("-" in problem)):
            sys.exit("Error: Operator must be '+' or '-'.")

        a = problem[0:problem.find(" ")]
        b = problem[(problem.find(" ")+3):]
        strs = [a, b]

        for num in strs:
            if len(num) > 4:
                sys.exit("Error: Numbers cannot be more than four digits.")

        nums = []
        for n in strs:
            try:
                nums.append(int(n))
            except:
                sys.exit("Error: Numbers must only contain digits.")

    strs = []
    if solution:
        for problem in problems:
            strs.append(with_solution(problem))
    else:
        for problem in problems:
            strs.append(without_solution(problem))

    if len(strs) == 1:
        arranged_problems = strs[0]
    else:
        lines = [strs[i].splitlines() for i in range(len(problems))]

        if len(problems) == 5:
            arranged_problems = '\n'.join(
                [v+w+x+y+z for v, w, x, y, z in zip(*lines)])
        elif len(problems) == 4:
            arranged_problems = '\n'.join(
                [w+x+y+z for w, x, y, z in zip(*lines)])
        elif len(problems) == 3:
            arranged_problems = '\n'.join([x+y+z for x, y, z in zip(*lines)])
        elif len(problems) == 2:
            arranged_problems = '\n'.join([y+z for y, z in zip(*lines)])

    return arranged_problems


print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
