#include <bits/stdc++.h>

using namespace std;

// Definitions
#define fi first
#define se second
#define pb push_back
#define mp make_pair 
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).end()
#define tr(it, x) for(auto it = x.begin(); it != x.end(); it++)
#define trr(it, x) for (auto it = x.rbegin(); it != x.rend(); it++)
#define for0(i, n) for (int i = 0; i < n; ++i)
#define for1(i, n) for (int i = 1; i <= n; ++i)
#define fork(i, k, n) for (int i = k; i < n; ++i)
#define PI 3.14159265358979323846

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;
typedef vector<vector<ll>> vvl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<pii> vii;
typedef vector<pll> vll;

inline int _gcd(int a, int b){
    return b ? _gcd(b, a % b) : a;
}

double gcd(double x, double y)
{
    return fabs(y) < 1e-6 ? x : gcd(y, fmod(x, y));
}

/*---------------------------------------------------------------*/
/*---------------------------------------------------------------*/
/*---------------------------------------------------------------*/

void test_case(){

}

int main(){
    ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    
    int t;
    cin >> t;
    while (t--)
        test_case();
    return 0;
}
