#include <bits/stdc++.h>
using namespace std;
int main (){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("VTSO.INP","r",stdin);
    freopen("VTSO.OUT","w",stdout);
    int n;
    cin>>n;
    vector <long long>a(n*2);
    for (int i=0;i<n;i++){
        cin>>a[i];
        a[i+n]=a[i];
    }
//    long long s=0;
    for (int i=0;i<n;i++){
        if(a[i]>0){
                long long s=a[i];
            for (long long j=i+1;j<=i+n;j++){
                s+=a[j];
                if(s<=0){
                    break;
                }
                if(j==i+n){
                    cout<<i+1;
                    return 0;
                }
            }
        }
    }
        cout<<0;
    return 0;
}