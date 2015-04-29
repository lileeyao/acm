#include<stdio.h>
#include<string.h>
#include<limits.h>
//typical a copy from g4g
typedef int bool;
#define true 1
#define false 0

#define min(a ,b) (a < b)? a: b;

int minPalPartion(char* str) {
    int n = strlen(str);

    int C[n][n];
    bool P[n][n];
    int i, j, k, L;
    for (i = 0;i < n;i++) {
        P[i][i] = true;
        C[i][i] = 0;
    }

    for (L = 2;L <= n; L++) {
        for (i = 0;i < n-L+1;i++) {
            j = i + L - 1;
            if (L == 2)
                P[i][j] = (str[i] == str[j]);
            else
                P[i][j] = ((str[i] == str[j]) &&
                        P[i+1][j-1]);
            if (P[i][j] == true)
                C[i][j] = 0;
            else {
                C[i][j] = INT_MAX;
                for(k = i; k <= j-1; k++)
                    C[i][j] = min(C[i][j], C[i][k]+
                        C[k+1][j]+1);
            }
        }
    }
    return C[0][n-1];
}

int main(){

    char str[] = "ababbbabbababa";
    printf("min cuts:%d", minPalPartion(str));
    return 0;
}
