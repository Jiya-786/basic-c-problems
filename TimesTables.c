/*Method 1*/

#include <stdio.h>

int main(){

printf("Enter the number whose times table you require- \n");
int a;
scanf("%d", &a);

printf("%d x 1 = %d\n",a,a*1);
printf("%d x 2 = %d\n",a,a*2);
printf("%d x 3 = %d\n",a,a*3);
printf("%d x 4 = %d\n",a,a*4);
printf("%d x 5 = %d\n",a,a*5);



  return 0;
}

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#include <stdio.h>

int main(){

  printf("Enter the number whose times tables you want - \n");
  int a;
  scanf("%d", &a);

  for(int i=1; i<=10; i++){

    printf("%d x %d = %d\n",a,i,a*i);
  }

  

 return 0;
}
