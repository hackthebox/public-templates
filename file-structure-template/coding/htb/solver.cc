#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>

int main() {
    int T, N;
    std::cin >> T >> N;
    std::vector<int> nums(N);
    
    for (int i = 0; i < N; ++i) {
        std::cin >> nums[i];
    }
    
    std::unordered_map<int, bool> seen;
    for (int i = 0; i < N; ++i) {
        int complement = T - nums[i];
        if (seen.count(complement)) {
            int a = nums[i];
            int b = complement;
            if (a > b) std::swap(a, b);
            std::cout << a << " " << b << std::endl;
            return 0;
        }
        seen[nums[i]] = true;
    }

    return 0;
}
