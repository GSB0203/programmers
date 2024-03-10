#include<stdio.h>

int main() {
    int n;
    int i;
    scanf("%d", &n);
    
    for(i=1;i<=n;i++, puts(""))
        printf("%d", i);
    
    return 0;
}