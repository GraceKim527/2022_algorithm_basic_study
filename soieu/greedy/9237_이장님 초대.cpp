#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    vector<int> t;

    int a =0, n = 0, endday=0 ;
    cin>> n;

    

    for (int i = 0; i <n ; i++)
    {
        cin>>a;
        t.push_back(a);
    }

    sort(t.rbegin(), t.rend());

    for( int i = 0 ; i < t.size() ; i++)
    {
        t[i] += i;
    }
    endday = *max_element(t.begin(),t.end());
    cout<< endday +2;



    return 0;
}