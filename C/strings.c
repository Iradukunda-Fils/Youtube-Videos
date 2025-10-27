#include <stdio.h>

int main(){
	char str[] = "Hello, world";
	char name[9] = {'J','o','h','n',' ','D','o','e', '\0'};

	printf("%s\n", name); 
	for (int i=0; i < sizeof(name); i++){
		printf("%c\n", name[i]);
	}
	return 0;
}
