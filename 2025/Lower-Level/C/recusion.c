#include <stdio.h>


int factorial(int n){
	if (n == 0)
		return 1;

         return n * factorial(n - 1);
}


int main(){
        printf("The factorial of %d is: %d\n", 2, factorial(2));
	return 0;
}
