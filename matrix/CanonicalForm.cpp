#include <stdio.h>
#include <math.h>

main()
{
	int i, j;
	float a[2][2], d, D, k1, k2;
	printf("For the general conic section equation    'a(x^2) + b(xy) + c(y^2) = d'    the coefficient matrix looks like: \n\n");
	printf("  a    (b/2)\n(b/2)    c");
	
	printf("\n\n\n\n\nEnter the value of intercept(d) of your conic section's equation: ");
	scanf("%f", &d);
	printf("\nEnter the coefficient matrix of your conic section's equation: \n");
	for (i=0; i<2; i++)
	{
		for (j=0; j<2; j++)
		{
			scanf("%f", &a[i][j]);
		}
	}
	
	D = pow((a[0][0] + a[1][1]), 2) - (4*((a[0][0]*a[1][1])-(a[1][0]*a[0][1])));
	
	if(D < 0)
	 printf("\n\n\n\nThe coefficient matrix isn't an hermitian matrix and hence doesn't have all real eigen values.");
	else
	 {
	 	k1 = ((a[0][0] + a[1][1]) + sqrt(D))/2;
	 	k2 = ((a[0][0] + a[1][1]) - sqrt(D))/2;
	 	printf("\n\nThe equation of the conic %g(x^2) + %g(xy) + %g(y^2) = %g relative to principal axes is    %g(x^2) + %g(y^2) = %g", a[0][0], (a[0][1]+a[1][0]), a[1][1], d, k1, k2, d);
	 }
	
	return 0;
}
