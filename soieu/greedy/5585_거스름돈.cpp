#include <iostream>
#include <vector>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    vector<int> money = {500, 100, 50, 10, 5, 1};

    int result = 0;

    int remain = 0;

    cin >> remain;
    remain = 1000 - remain;
    for ( int i = 0; i<money.size() ; i++)
    {
        result += remain / money[i];
        remain = remain % money[i];
    }
    cout<<result;
    


    return 0;
}