#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int n;cin>>n;
  int start = 0, end = n - 1;
  int cnt = 0;
  vector<int> nums(n);

  for(int i=0;i<n;i++) {
    cin>>nums[i];
  }

  sort(nums.begin(), nums.end());

  for(int i=0;i<n;i++) {
    int val = nums[i];
    start = 0, end = n - 1;
    while(start < end) {
      int sum = nums[start] + nums[end];
      if ( sum == val) {
        if(start != i && end != i) {
          cnt++;
          break;
        }
        else if(start == i) start++;
        else if(end == i) end--;
      }
      else if(sum < val) start++;
      else end--;
    }
  }

  cout<<cnt;
  return 0;
}

