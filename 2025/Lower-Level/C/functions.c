#include <stdio.h>

int add(int a, int b);

int product(int a, int b){
	return a * b;
}

int divide(int a, int b){
	return a / b;
}


int (*apply(int (*func)(int, int), char opt))(int, int){
	switch(opt){
		case '+': return add;
		case '*': return product;
	        case '/': return divide;
	        default: return func;
		}
}


int add(int a, int b){ return a + b; }

int main(){
	int (*fptr)(int, int);
	fptr = add;

	int (*apply_add)(int, int) = apply(add, '+');

	int (*divde)(int, int) = apply(divide, '/');

	int (*invl)(int, int) = apply(product, 't');

	printf("the applied addition is: %d\n", apply_add(2,1));

        printf("The bytes of the function is: %zu\n", sizeof(fptr));
	printf("The address of the function is: %p\n", fptr);
	printf("the test value is: %i\n", add(2,1));
	return 0;
}
