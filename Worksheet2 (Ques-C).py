# [Exercise D]

# Goal: Generate a certain sequence of 10 real numbers and add them together
# The sequence is for a given real number x find the sum:
#             1+1/x+1/x^2... (10 terms, the last being 1/x^9)
# The idea for main() is as follows:
# 1. Declare and read in a value for x using scanf("%f",&x);
# 2. Declare two variables
#        a. one called sum to model the sum of the terms of the series
#        b. one called term to model the successive terms of the series
# 3. Initialize sum to zero
# 4. Initialize term to be zero
# 5. Use a loop counter i initialized to zero
# 6. while i is less than 10 do the following in a loop
#         (a) if i is 0 then set term=1;
#         (b) if i is greater than zero set term=term/x
#                      (think: what is this step doing?)
#         (c) update the value of sum by adding term
#         (d) increment the loop counter
# 7. print the value of sum using printf("%10.5f\n",sum); Note the 10.5


#-------------------------------------------------------------------first try----------------------------------------------------------
#include <stdio.h>

int main(){

	float i,x;
	scanf("%f",&x);
	
	float sum,term;
	
	float sum=0;
	float term=0;
	
	i=0;
	while(i<10){
		
		if(i=0){
			float term=0;
		}
		else if (i>0){
			float term= term/x;
		}

		sum= sum + term;
		
	} i++
	
	print("%10.5f\n",sum);
	
	return 0;
}

________________________________________________________________________________
#|But declaring variables two times is not allowed in c, declare only once ie:  |
#|                                                                              | 
#|  float sum,term;                                                             | 
#|	                                                                            |
#|	float sum=0;                                                                |
#|	float term=0;                                                               |
#|                                                                              |
#|this is not allowed                                                           |
# |-----------------------------------------------------------------------------|
# |MISTAKES-                                                                    |
# |                                                                             |__
# |Variable types-                                                                |
# |You want real numbers (fractions), so x, sum, term should be float, not int.   |
# |                                                                               |
# |scanf mismatch-                                                                |
# |You wrote scanf("%f",&x); but declared x as int. Mismatch → undefined behavior.|
# |                                                                               |
# |Redeclaration inside loop-                                                     |
# |You wrote int term=0; inside the loop multiple times. Don’t redeclare — just   | 
# |update.                                                                        |
# |                                                                               |
# |if(i=0) mistake-                                                               |
# |= is assignment, == is comparison.                                             |
# |if(i=0) always sets i to 0 (and is false).                                     |
# |                                                                               |
# |Loop increment-                                                                |
# |You wrote } i++ → should be inside the loop, before the closing brace.         | 
# |                                                                               |
# |print vs printf-                                                               |
# |C uses printf, not print.                                                      |
# |_______________________________________________________________________________|

#-----------------------------------------------------------try-2--------------------------------------------------------------------

#include <stdio.h>

int main(){
	float x;
	scanf("%f",&x);
	
	float sum=0;
	float term=0;
	
	int i=0;
	while(i<10){
		
		if(i==0){
			term=1;
		}
		
		else if (i>0){
			term= term/x;
		}

		sum= sum + term;
		i++;
	} 
	
 
	printf("%10.5f\n",sum);
	
	return 0;
}

