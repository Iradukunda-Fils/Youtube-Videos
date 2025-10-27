#include <stdio.h>

int main(){
	int a = 5;

	printf("The address in memory is: %p\n", &a);

	int* prt = &a;

	printf("the value is: %d\n", *prt);

	return 0;
}
