#ifndef Q172_H
#define Q172_H


class Q172
{
public:
    Q172();

    /** 100%
     */
    int trailingZeroes(int n) {
       int zeros = 0;
       int pow2 = 5, ex = 1;
       while (pow2 <= n) {
           zeros += n / pow2;
           ex++;
           pow2 *= 5;
       }
       return zeros;
    }
};

#endif // Q172_H
