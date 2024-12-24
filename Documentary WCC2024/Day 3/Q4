#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int findWinner(int n, int k) {
        if (n == 1) {
            return 1; 
        }
        return (findWinner(n - 1, k) + k - 1) % n + 1;
    }

    int findTheWinner(int n, int k) {
        return findWinner(n, k);
    }
};

int main() {
    Solution solution;
    int n = 5, k = 2;
    cout << "The winner is: " << solution.findTheWinner(n, k) << endl;
    return 0;
}
