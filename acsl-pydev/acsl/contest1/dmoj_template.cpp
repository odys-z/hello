#include <stdio.h>
#include <string.h>
    
int N = 100;

char arr[20][4];

int main()
{
    memset(arr, 0, 20 * 4);
    // scanf("%d", &N);
    for(int i = 0; i < N; i++)
    {
        scanf("%s", arr[i]);
        // 128H2310S118T258C1512D
        // printf(arr[i]);
        
        if (strlen(arr[i]) == 0)
            break;
        /* 1
        2
        8
        H
        2
        ...
         */
        printf("%s\n", arr[i]);
        
    }
}
