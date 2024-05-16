#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int n;cin>>n;
  int m;cin>>m;
  int sum = 0;
  int start = 0, end = n - 1;
  vector<int> nums(n);

  for(int i=0;i<n;i++) {
    cin>>nums[i];
  }

  sort(nums.begin(), nums.end());
  while(start < n) {
    if ((nums[start] + nums[end]) < m) start++;
    else if ((nums[start] + nums[end]) > m) end--;
    else if ((nums[start] + nums[end]) == m) {
      sum++;
      start++, end--;
    }
  }

  cout<<sum / 2;
  return 0;
}