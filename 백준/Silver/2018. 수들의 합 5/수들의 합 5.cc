#include <iostream>
using namespace std;

int main() {
  int n;cin>>n;
  int start = 1, end = 1;
  int sum = 0;
  int cnt = 0;

  while(start <= end && end <= n) {

    if(sum < n) sum += end++;
    else {
      if(sum == n) cnt++;
      sum -= start++;
    }
  }
  cout<<cnt + 1;
  return 0;
}