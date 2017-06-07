//2 players with a 'tower' of bricks with individual values
//assuming each player plays optimally, what is the highest score
//player 1 may get?
//each player may remove 1, 2, or 3 bricks

#include <cmath>
#include <iostream>
using namespace std;

int main() {
    int numT, n, currNum;
    cin >> numT;
    for (int i = 0; i < numT; i++){
        cin >> n;
        long long numArr[n];
        long long scoreArr[n];
        long long sumArr[n];
        for (int i = 0; i < n; i++){
            cin >> numArr[n-i-1];
        }
        sumArr[0] = numArr[0];
        for (int i = 1; i < n; i++){
            sumArr[i] = numArr[i] + sumArr[i-1];
        }
        
        for (int i = 0; i < n; i++){
            if (i < 3)
                scoreArr[i] = sumArr[i];
            else
                scoreArr[i] = sumArr[i] - std::min(std::min(scoreArr[i-1], scoreArr[i-2]), scoreArr[i-3]);
        }
        cout << scoreArr[n-1] << endl;

    }

    return 0;
}
