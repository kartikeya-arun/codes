#include<stdio.h>
#include<conio.h>
void main()
{
    int n,i;
    printf("Enter the number of terms to print the fibonacci series\t");
    scanf("%d",&n);
    printf("The fibonacci series is as follows\n");
    for(i=0;i<=n;i++)
    {
        printf("%d",fib(i));
    }
    getch();
}
int fib(n)
{
        if (n==0 || n==1)
        {
            return 1;
        }
        else
        {
            return fib(n-1)+fib(n-2);
        }
}
