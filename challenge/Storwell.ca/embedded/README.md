# About

G1.c & g2.c are answers to Storwell challenges.

# Compile & run

Note: This sources are tested on Ubuntu 16.0.4 LTS, gcc 5.4.0.

Download files in this folder,

- q1

```commandline
    g++ g1.c
    ./a.out 12 12
    12x12
```

- q2

About the question:

The outputs can be base 62 expressions of integer values.

For question a), function *f(Ai)* is a string function which express a integer value with base 62
presentation. E.g.

```commandline
    cGp = (c) * 62 ^ 2 + (G) * 62  + (p) = 15840
```

where (c), (G), (p) are base 62 digits with values equals base 10 values 4, 7 & 30 respectively, see
[q2.h](https://github.com/odys-z/hello/blob/master/challenge/Storwell.ca/embedded/q2.h).

Here is what the data in the Spreedsheet have told us:

```commandline
    base 10:  0 1 2 3 4 ...
    base 62:  C 7 x i c ...
```

See g2.h. (q2-digits-parser.py is a script to figure out what is each base 62 digit's value in base 10)

So cCC in base 62 is actually 4 * 62 ^ 2 + 0 + 0 in decimal. 

For question b), run g2.c with integer argument (stirng in CLI), like:

```commandline
    ./a.out 30001
    GIF
    ./a.out 55555
    NOi
    ./a.out 77788
    VNQ
```

For question c), there shouldn't be a max value limit to an arbitary base's expression. But if we implemented the function
by converting digital string into c/c++ int type, it will be the max int value which is depending on the runtime context.

For question d), see g2.c.

To run g2.c,

```commandline
    g++ g2.c
    ./a.out 15840
    cGp
```

Or test with the Python script for verifying all the inputs:

```commandline
    g++ g2.c
    pytyon3 test.py
    15840   cGp
    ...
```
