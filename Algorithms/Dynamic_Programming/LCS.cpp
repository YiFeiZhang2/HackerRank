//finding longest common subsequence of 2 integer sequences

#include <iostream>
using namespace std;

void print_arr(int* lengths[], int n, int m){
    for(int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            cout << lengths[i][j] << " ";
        }
        cout << endl;
    }
}

void print_subseq(int* lengths[], int nSeq[], int mSeq[], int i, int j){
    if (i !=0 && j != 0){
        if (lengths[i][j] > lengths[i][j-1] && lengths[i][j] > lengths[i-1][j]){
            print_subseq(lengths, nSeq, mSeq, i-1, j-1);
            cout << nSeq[i-1] << " ";
        } else {
            if (lengths[i-1][j] > lengths[i][j-1])
                print_subseq(lengths, nSeq, mSeq, i-1, j);
            else
                print_subseq(lengths, nSeq, mSeq, i, j-1);
        }
    }
}

int main() {
    int n, m;
    cin >> n;
    cin >> m;
    int nSeq[n]; 
    int mSeq[m];
    for (int i = 0; i < n; i++)
        cin >> nSeq[i];
    for (int i = 0; i < m; i++)
        cin >> mSeq[i];
    int* sLengths[n+1] = {};
    for (int i = 0; i < n+1; i++)
        sLengths[i] = new int[m+1];
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (nSeq[i] == mSeq[j]){
                sLengths[i+1][j+1] = sLengths[i][j] + 1;
            }
            else
                sLengths[i+1][j+1] = (sLengths[i][j+1] > sLengths[i+1][j]) ? (sLengths[i][j+1]) : (sLengths[i+1][j]);
        }
    }

    //print_arr(sLengths, n+1, m+1);
    print_subseq(sLengths, nSeq, mSeq, n, m); 
    return 0;
}
