#include <stdio.h>
#include <string.h>

#define False 0
#define True 1

int underScore(int trk, char suit)
{
    if (suit == 'T')
        return 40 + 30 * (trk - 1);
    else if (suit == 'H' || suit == 'S')
        return trk * 30;
    else
        return trk * 20;
}

int overScore(int overs, char suit)
{
    if (suit == 'C' || suit == 'D')
        return overs * 20;
    else return overs * 30;
}

int (*)[4] bridge2009(int games, int records[][4])
{
    int scors[games][4];

    int teams[2] = {50, 50}; // both not vulnerable at first
    int restart = False;

    for (int i = 0; i < games; i++ ) 
    {
        int rec[4];
        memcpy(rec, records[i], sizeof(records[i]));

        int scr[4] = {0, 0, 0, 0};
        if (i > 0)
            for (int s = 0; s < 4; s++)
                scr[s] = scors[i - 1][s];

        if (restart)
        {
            scr[0] = 0, scr[2] = 0;
            teams[0] = 50, teams[1] = 50;
        }
        restart = False;

        int winner = -1;
        int bider = rec[0] - 1;
        int operx = ( bider + 1 ) % 2;

        int bid = rec[1] + 6;
        int got = rec[2];
        char suit = rec[3];
        if (bid <= got)
        {
            // win
            scr[bider * 2] += underScore(bid - 6, suit);
            scr[bider * 2 + 1] += overScore(got - bid, suit);
            winner = bider;
        }
        else // lose
        {
            int penalty = teams[ bider ];
            scr[operx * 2 + 1] += penalty * (bid - got);
            winner = operx;
        }
        
        teams[winner] = 100; // vulnerable
        
        if (scr[winner * 2] >= 100)
            restart = True;
            
        // scors[i] = scr.copy()
        for (int k = 0; k < 4; k++)
            scors[i][k] = scr[k];
    }

    return scors;
}

#define N 100

int arr[N][4];

int main()
{
    memset(arr, 0, N * 4);
    int i = 0;
    for(; i < N; i++)
    {
        scanf("%d", arr[i]);
        
        if (strlen(arr[i]) == 0)
            break;
    }

    // i is game count
    int** ansr = bridge2009(i, arr); 

    printf("%d %d %d %d\n", ansr[i]);
}