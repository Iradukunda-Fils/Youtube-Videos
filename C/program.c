#include <stdio.h>
#include <stdbool.h>


int main(){
	// comment
	/* 
	 *
	 *
	 * multilne comments
	 */
	printf("boolean is: %ld\n", sizeof(short));
	long int a, b, c;
	float g = 2.0;
	double  d = 323.4242452345342342;
	char i = 'A';
	int h = 3;

	printf("sum is: %d\n", 6 * 3);

	printf("float is: %f, double is: %lf", g, d);
	printf("%ld, %ld, %ld\n", a, b, c);
	printf("hello, World!\n");
	return 0;
}
