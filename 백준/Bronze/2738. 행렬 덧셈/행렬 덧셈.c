#include<stdio.h>
int main() {
    int n, m;
    int i, j;
    int a[101][101] = {};
    int b[101][101] = {};
    scanf("%d %d", &n, &m);
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            scanf("%d", &a[i][j]);
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            scanf("%d", &b[i][j]);
    
    for(i=0;i<n;i++, puts(""))
        for(j=0;j<m;j++)
            printf("%d ", a[i][j] + b[i][j]);
    return 0;
}