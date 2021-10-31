#include<iostream>
using namespace std;
int main()
{
	int i,j;
	cout<<&i<<endl<<&j<<endl;
	int k = &i;
	cout<<k;
	return 0 ;
}
