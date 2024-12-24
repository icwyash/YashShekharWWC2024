#include <iostream>
using namespace std;

class Solution {
public:
    int minNonZeroProduct(int p) {
        const int MOD = 1e9 + 7;
        long long maxNum = (1LL << p) - 1;
        long long power = maxNum / 2;
        long long result = 1;
        long long base = maxNum - 1;

        while (power > 0) {
            if (power % 2 == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            power /= 2;
        }

        result = (result * maxNum) % MOD;
        return result;
    }
};

int main() {
    Solution solution;
    int p = 3;
    cout << "The minimum non-zero product is: " << solution.minNonZeroProduct(p) << endl;
    return 0;
}
