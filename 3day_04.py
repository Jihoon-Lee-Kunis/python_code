def solution(k, a, b):
    return sum(sorted(a)[k:]+sorted(b)[:-k])
