#include<bits/stdc++.h>
using namespace std;

unsigned countBits(unsigned int number)
{
    return (int)log2(number)+1;
}

int main() {
   int t;
   cin>>t;
   for(int i=0;i<t;i++){
    
    int n;
    cin>>n;
    int pwr=countBits(n)-1;
    int ner_num=pow(2,pwr);
    
    int ans;
    if(n==1 || n==2){
        cout<<"1"<<"\n";
    }
    else if( (n & (n-1)) ==0){
        ans = n - (n>>1);
        cout<<ans<<"\n";
    }
    else{
        
        cout<<max( (n- ner_num +1) , ner_num - (ner_num>>1) )<<"\n";
    }
    
   }
    
    
	return 0;
}
