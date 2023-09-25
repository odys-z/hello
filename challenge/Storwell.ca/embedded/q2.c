/*
 * Compile: g++ q2.c
 * Tested on gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12)
 */
 
#include <stdlib.h>
#include <iostream>
using namespace std;

#define B62 (62)

#include "q2.h"

void base62(int);

int main(int argc, char *argv[])
{
    if (2 != argc) {
        cout << "useage: q2 number(base10)" << endl;
        exit(-1);
    }

    int n = atoi(argv[1]);

    base62(n);
    cout << endl;
}

// char digits[] = {
//     'C', '7', 'x', 'i', 'c', 'P', 'M', 'G', 'v', 'z', 'A', 'Z', 'y', 'T', 'N', 'o', 'd', 'm', 'w', 'n', 'V', '?', 'D', '3', 'B', '6', 'H', '0', 'O', 'u', 'p',
//     '8', 'E', '2', '1', 'W', '9', '?', 'q', 'L', 'Q', 'X', '4', 'Y', 'j', 'S', 'e', 'U', 'h', 'I', 'R', 'J', 'g', 'a', 'f', 'F', 't', 'r', 'K', 'l', 'b', 'k'};

void base62(int n) {
    if (n > 0) {
        base62(n / B62);
        cout << digits[n % B62];
    }
}
