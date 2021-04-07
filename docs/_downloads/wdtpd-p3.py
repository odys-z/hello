
def wdtpd_problem3(A, B):
    '''
    A(0) = 12: A(1) = 41: A(2) = 52
    A(3) = 57: A(4) = 77: A(5) = -100
    B(0) = 17: B(1) = 34: B(2) = 81
    J = 0: K = 0: N = 0
    while A(J) > 0
      while B(K) <= A(J)
        C(N) = B(K)
        N = N + 1
        k = k + 1
      end while
      C(N) = A(J): N = N + 1: J = J + 1
    end while
    C(N) = B(K)
    '''
    C = [0] * (len(A) * len(B))
    J, K, N = 0, 0, 0
    print('J K N Aj Bk Cn')
    print(J, K, N, A[J], B[K], C[N])
    while A[J] > 0:
        while B[K] < A[J]:
            C[N] = B[K]
            print(J, K, N, A[J], B[K], C[N])
            N = N + 1
            K = K + 1

        C[N] = A[J]
        print(J, K, N, A[J], B[K], C[N])
        N, J = N + 1, J + 1

    C[N] = B[K]
    return C

c = wdtpd_problem3( [12, 41, 52, 57, 77, -100], [17, 34, 81] )
print('C4:', c[4])
