"""
https://blog.robertelder.org/diff-algorithm/
"""
def shortest_edit_script_length(old, new):
    print(old)
    print(new)
    N = len(old)
    M = len(new)
    MAX = N + M

    V = [None] * (2 * MAX + 2)
    V[1] = 0
    for D in range(0, MAX + 1):
        for k in range(-D, D + 1, 2):
            if k == -D or k != D and V[k - 1] < V[k + 1]:
                x = V[k + 1]
            else:
                x = V[k - 1] + 1
            y = x - k
            while x < N and y < M and old[x] == new[y]:
                x = x + 1
                y = y + 1
            V[k] = x
            print(x, old[x] if x < len(old) else ' ', ':', y, new[y] if y < len(new) else ' ', k, V)
            if x >= N and y >= M:
                return D


if __name__ == '__main__':
    shortest_edit_script_length('abc', 'bc')
    shortest_edit_script_length('abc', 'abb')
