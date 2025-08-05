#include <stdio.h>
#include <stdbool.h>


int main(int arg, char **argv){
  

  printf("%s , %s\n", argv[0], argv[1]);
  printf("hello word \n");

  if (true){
    printf("hello true \n");
  }

  for(int i=0; i <= 5; i++){
    printf("number is: %d \n", i);
  }

  return 0;
}