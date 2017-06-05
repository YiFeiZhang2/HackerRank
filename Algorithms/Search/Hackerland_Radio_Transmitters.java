/*

Hackerland is a one-dimensional city with n houses, where each house i is located at some x(i) on the x-axis. 
The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a range, k, 
meaning it can transmit a signal to all houses <=k units of distance away.

Given a map of Hackerland and the value of k, can you find and print the minimum number of transmitters needed 
to cover every house in the city? (Every house must be covered by at least one transmitter) Each transmitter must 
be installed on top of an existing house.

Input Format

The first line contains two space-separated integers describing the respective values of n (the number of houses in Hackerland)
and k (the range of each transmitter). 
The second line contains n space-separated integers describing the respective locations of each house.

Constraints

1 <= n, k <= 10^5
1 <= x(i) <= 10^5

There may be more than one house at the same location.
Subtasks

Output Format

Print a single integer denoting the minimum number of transmitters needed to cover all the houses.

*/

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] x = new int[100001];
        for(int x_i=0; x_i < n; x_i++){
            x[in.nextInt()] += 1;
        }
        int numTrans = 0;              //keeps track of current array x index
        int lastTrans = -1000001;
        for(int j = 0; j < 100001; j++){
            if (x[j] == 0) { continue; }                   //now there is a house at x[j]
            else {
                if (Math.abs(j - lastTrans) <= k) {          //house at x[j] is already covered by a previous transmitter
                    continue;
                } else {                //house at x[j] is not covered by transmitter
                    int maxRange = j + k;
                    int currMax = j;
                    for (; j <= maxRange; j++){
                        if (j < 100001 && x[j] != 0){
                            currMax = j;
                        }
                    }
                    lastTrans = currMax;
                    numTrans++;
                    j--;                //to undo the duplicate add from inner for loop
                }                    
            }
        }
        System.out.println(numTrans);
    }
}
