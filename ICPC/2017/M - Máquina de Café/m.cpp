#include <bits/stdc++.h>

using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  int x = a*4 + b*2;
  int y = b*2 + c*4;
  int z = a*2 + c*2;

  if(x < y && x < z) cout << x << endl;
  else if(y < z) cout << y << endl;
  else cout << z << endl;
}