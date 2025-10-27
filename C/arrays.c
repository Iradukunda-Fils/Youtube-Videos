#include <stdio.h>

int main(){
	int arr[7] = {432, 42322, 42,324,234,24,67782};
        
	int len = sizeof(arr) / sizeof(arr[0]);

	/* for (int i=0; i < len ; i++){
		printf("The element is: %d\n", arr[i]);
	}
	*/

	for(int i=0; i < 7; i++){ 
		if (i == 3){
			break;
	        }
		printf("element is: %d\n", arr[i]);
	}
	
	return 0;

}
