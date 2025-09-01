#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void quickSort( int[], int, int);
int partition( int[], int, int);

void generate_random_array(int arr[], int size, int min, int max) {
    // Seed the random number generator once
    static int seeded = 0;
    if (!seeded) {
        srand(time(NULL));
        seeded = 1;
    }

    for (int i = 0; i < size; ++i) {
        arr[i] = min + rand() % (max - min + 1); // random in [min, max]
    }
}

void main()
{
int i,a[10];
	generate_random_array(a,10,1,10);

printf("\n\nUnsorted array is: ");
for(i = 0; i < 9; ++i)
printf(" %d ", a[i]);
quickSort( a, 0, 8);
printf("\n\nSorted array is: ");
for(i = 0; i < 9; ++i)
printf(" %d ", a[i]);
}

void quickSort( int a[], int l, int r)
{
int j;
if( l < r ) { // divide and conquer
j = partition( a, l, r);
quickSort( a, l, j-1);
quickSort( a, j+1, r);
}
}

int partition( int a[], int l, int r)
{
int pivot, i, j, t;
pivot = a[l];
i = l;
j = r+1;
while( 1) {
do{
++i;
} while(a[i]<=pivot && i<=r);
do{
--j;
} while( a[j] > pivot );
if( i >= j ) break;
t = a[i];
a[i] = a[j];
a[j] = t;
}
t = a[l];
a[l] = a[j];
a[j] = t;
return j;
}




