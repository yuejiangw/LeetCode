// 位运算神器：bitset类
#include <bitset>
using std::bitset;
class Solution {
public:
    int hammingWeight(uint32_t n) {
        return bitset<32>(n).count();
    }
};