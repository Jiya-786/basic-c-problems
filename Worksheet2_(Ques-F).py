#-----------------------------------------------------------try-1-------------------------------------------------------------
#include <stdio.h>

int main(){
	int n;
	scanf("%d",&n);
	
	int i=0;
	while(i<7){
	
		if (n%3==0){
			
			n=n/3;
			printf("%d",n);
			printf("\t");
		}
		
		else if (n%3==1){
			
			n=5*n+1;
			printf("%d",n);
			printf("\t");
		}
		
		else if (n%3==2){
			
			n=5*n+2;
			printf("%d",n);
			printf("\t");
		}
		
		i++;
	}

return 0;
}
 ____________________________________________________________________________________________
|Problems in this version:                                                                  |
|                                                                                           | 
|Printing format                                                                            |                                                                                          |
|You used "\t" (tab).                                                                       |                                                                                        |
|The problem statement says: use "%d " (number followed by a space).                        |                                                                                      |
|That means there should be a space after each number, not a tab.                           | 
|                                                                                     |
|Newline at the end                                                                         |                                                                                           |                                                                                 
|After the loop finishes (all 7 numbers printed), you should print exactly one newline.     |
|                                                                                           | 
|Right now, your code doesn’t print a newline at the end.                                   |
|___________________________________________________________________________________________|	

#-------------------------------------------------------------------try-2----------------------------------------------------------

#include <stdio.h>

int main(){
	int n;
	scanf("%d",&n);
	
	int i=0;
	while(i<7){

		if (n%3==0){
			n=n/3;
			printf("%d ",n);
		}
		
		else if (n%3==1){
			n=5*n+1;
			printf("%d ",n);
		}
		
		else if (n%3==2){
			n=5*n+2;
			printf("%d ",n);
		}
		
		i++;
	}

	printf("\n");
	
	return 0;
}

_______________________________________________________________________________________________
|# 2. Automated checking (in labs / assignments)                                               |
|----------------------------------------------------------------------------------------------|                                                                                              |
|# Many programming exercises are checked by automated systems.                                |
|----------------------------------------------------------------------------------------------|                                                                                              |
|# If the required output is:                                                                  |
|# 27 9 3 1 6 2 12                                                                             |
|                                                                                              |
|# and your program outputs:                                                                   |
|# 27 9 3 1 6 2 12                                                                             |
|# (with no \n at the end), the checker might mark it wrong because it expects a newline.      |
|----------------------------------------------------------------------------------------------|                                                                                              |
|# hence the last print("\n") statement is very imp for test case to pass                      |
|______________________________________________________________________________________________|
