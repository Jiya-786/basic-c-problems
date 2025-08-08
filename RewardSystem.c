#include <stdio.h>

int main(){

  printf("how many subjects out of math and science have you passed? (answer as 1 or 2)\n");
  int p;
  scanf("%d",&p);
  
  if (p==1){
      
      printf("Congratulations! You get a reward of 15 points!");
      
  }
  
  else if (p==2){
      
      printf("Congratulations! You get a reward of 45 points!");
      
  }
  
  else {
      
      printf("Sorry, please invest more time in studying");
      
  }

  

 return 0;
}

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
my errors- 
  1) wrote &d in place of %d
  2) wrote p=1,p=2 instead of p==1,p==2
