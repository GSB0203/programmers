#include <iostream>
#include <vector>
using namespace std;

int main() {
  int s, p;cin>>s>>p;
  int a, c, g, t;
  int ac = 0, cc = 0, gc = 0, tc = 0;
  int l = 0, r = p - 1;
  int cnt = 0;
  string str;
  cin>>str;
  cin>>a>>c>>g>>t;
  for(int i=l;i<=r;i++) {
    if(str[i] == 'A') ac++;
    if(str[i] == 'C') cc++;
    if(str[i] == 'G') gc++;
    if(str[i] == 'T') tc++;
  }


  while(r < s) {
    if(a <= ac && c <= cc && g <= gc && t <= tc) cnt++;
    if(str[l] == 'A') ac--;
    else if(str[l] == 'C') cc--;
    else if(str[l] == 'G') gc--;
    else if(str[l] == 'T') tc--;

    l++, r++;

    if(str[r] == 'A') ac++;
    else if(str[r] == 'C') cc++;
    else if(str[r] == 'G') gc++;
    else if(str[r] == 'T') tc++;

  }

  cout<<cnt;
  return 0;
}