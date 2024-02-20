// C++標準ライブラリinclude
#include <bits/stdc++.h>

// ACL一括include
#include <atcoder/all>

// 通常repマクロ
#define rep(i, n) for (ll i = 0; i < (ll)(n); ++i)

// 1~nバージョンrepマクロ
#define rep1(i, n) for (ll i = 1; i <= (ll)(n); ++i)

// m~nバージョンrepマクロ
#define rep2(i, m, n) for (ll i = (m); i < (ll)(n); ++i)

// n-1~0バージョンrepマクロ
#define rrep(i, n) for (ll i = (ll)(n)-1; i >= 0; --i)

// n~1バージョンrepマクロ
#define rrep1(i, n) for (ll i = (ll)(n); i > 0; --i)

// m～nバージョンマクロ
#define rrep2(i, m, n) for (ll i = (ll)(m); i > n; --i)

// vec[i]の形を利用してもエラーが見やすく表示される
#define _GLIBCXX_DEBUG

// 配列のイテレータを一括選択
#define all(a) a.begin(), a.end()

// 配列のイテレータを逆順に一括選択
#define rall(a) a.rbegin(), a.rend()

// 配列を小さい順にソート
#define SORT(a) sort(all(a));

// 配列を大きい順にソート
#define RSORT(a) sort(rall(a));

// 配列を逆順にする
#define REV(a) reverse(all(a));

// 配列の最小値
#define MIN(a) *min_element(all(a))

// 配列の最大値
#define MAX(a) *max_element(all(a))

// 配列の和
#define SUM(a) accumulate(all(a), 0LL)

// 二分探索
#define bs(a, x) binary_search(all(a), x)

// 配列の中でxを超えない最小の値の場所
#define lb(a, x) lower_bound(all(a), x) - a.begin()

// 配列の中でxより大きい最小の値の場所
#define ub(a, x) upper_bound(all(a), x) - a.begin()

// 文字列や配列などの大きさ
#define SZ(a) ll(a.size())

// x/yの答えの小数点以下繰り上げ
#define CEIL(x, y) (x + y - 1) / y

// 期待値mod998244353
#define smallexpect(a, b) (a % smallMOD) * pow_mod(b, smallMOD - 2, smallMOD) % smallMOD

// 期待値mod1000000007
#define bigexpect(a, b) (a % smallMOD) * pow_mod(b, bigMOD - 2, bigMOD) % bigMOD

// whileと共に使用し、nCr通りの組み合わせを試す
#define n_p next_permutation

// あるデータ型の変数を別のデータ型に変換する
#define s_c static_cast

// 特定の全ての部分文字列(x)を異なる部分文字列(y)に置き換える
#define r_r(a, x, y) regex_replace((a), regex((x)), (y))

// プログラム実行開始から何秒経過したかを整数で返す
#define restime cout << "Execution Time:" << (ld)1.0 * ((ld)endofrestime - (ld)startofrestime) / CLOCKS_PER_SEC << endl;

// 配列の先頭に要素を追加(List,dequeのみ)
#define pf push_front

// pairの1つ目の要素にアクセス
#define fi first

// pairの2つ目の要素にアクセス
#define se second

// 配列の最後尾に要素を追加
#define pb push_back

// 引数に合わせてベクターに挿入（基本こっちでOK）
#define eb emplace_back

// pairを作る
#define mp make_pair

// 配列の先頭から要素を削除(List,dequeのみ)
#define ppf pop_front()

// 配列の最後尾から要素を削除
#define ppb pop_back()

// 小数点以下の桁数を指定して出力
#define fixset(n, y) cout << fixed << setprecision(n) << y << endl;

// int型を宣言、入力
#define INT(...)     \
    int __VA_ARGS__; \
    scan(__VA_ARGS__)

// long long型を宣言、入力
#define LL(...)     \
    ll __VA_ARGS__; \
    scan(__VA_ARGS__)

// string型を宣言、入力
#define STRING(...)     \
    string __VA_ARGS__; \
    scan(__VA_ARGS__)

// char型を宣言、入力
#define CHAR(...)     \
    char __VA_ARGS__; \
    scan(__VA_ARGS__)

// double型を宣言、入力
#define DOUBLE(...)     \
    double __VA_ARGS__; \
    scan(__VA_ARGS__)

// long double型を宣言、入力
#define LD(...)     \
    ld __VA_ARGS__; \
    scan(__VA_ARGS__)

// yes/noの質問への回答の高速化
#define resYES        \
    {                 \
        print("YES"); \
    }

#define resYes        \
    {                 \
        print("Yes"); \
    }

#define resyes        \
    {                 \
        print("yes"); \
    }

#define resNO        \
    {                \
        print("NO"); \
    }

#define resNo        \
    {                \
        print("No"); \
    }

#define resno        \
    {                \
        print("no"); \
    }

#define resyn         \
    {                 \
        print("Yes"); \
    }                 \
    else              \
    {                 \
        print("No");  \
    }

// std::の省略
using namespace std;

// atcoder::の省略
using namespace atcoder;

// 型を省略して書く
// 0-dimensional
using ull = unsigned long long;

using ll = long long;

using ld = long double;

using i7 = __int128_t;

// n+n-dimensional
using pii = pair<int, int>;

using pid = pair<int, ld>;

using pis = pair<int, string>;

using pll = pair<ll, ll>;

using pld = pair<ll, ld>;

using pls = pair<ll, string>;

using pdi = pair<ld, int>;

using pdl = pair<ld, ll>;

using pdd = pair<ld, ld>;

using pds = pair<ld, string>;

using psi = pair<string, int>;

using psl = pair<string, ll>;

using psd = pair<string, ld>;

using pss = pair<string, string>;

using mii = map<int, int>;

using mid = map<int, ld>;

using mis = map<int, string>;

using mll = map<ll, ll>;

using mld = map<ll, ld>;

using mls = map<ll, string>;

using mdi = map<ld, int>;

using mdl = map<ld, ll>;

using mdd = map<ld, ld>;

using mds = map<ld, string>;

using msi = map<string, int>;

using msl = map<string, ll>;

using msd = map<string, ld>;

using mss = map<string, string>;

// 1-dimensional
using vi = vector<int>;

using vi7 = vector<i7>;

using vs = vector<string>;

using vl = vector<ll>;

using vc = vector<char>;

using vb = vector<bool>;

using vd = vector<ld>;

using vpii = vector<pii>;

using vpll = vector<pll>;

using vpsi = vector<psi>;

using vpis = vector<pis>;

using si = set<int>;

using sl = set<ll>;

using sc = set<char>;

using ss = set<string>;

using sd = set<ld>;

// 2-dimensional
using vvi = vector<vi>;

using vvi7 = vector<vi7>;

using vvl = vector<vl>;

using vvc = vector<vc>;

using vvs = vector<vs>;

using vvb = vector<vb>;

using vvd = vector<vd>;

using vvpii = vector<vpii>;

using vvpll = vector<vpll>;

using vsi = vector<si>;

using vsl = vector<sl>;

// 3-dimensional
using vvvi = vector<vvi>;

using vvvi7 = vector<vvi7>;

using vvvl = vector<vvl>;

using vvvc = vector<vvc>;

using vvvb = vector<vvb>;

using vvvd = vector<vvd>;

// others
using mint = modint998244353;

// template

// scanの引数を不要にする
void scan() {}

// vector配列にその大きさだけ入力
template <class T>
void scan(vector<T> &v)
{
    for (T &t : v)
    {
        cin >> t;
    }
}

// vector<vector>>配列にその大きさだけ入力
template <class T>
void scan(vector<vector<T>> &v)
{
    for (auto &row : v)
    {
        for (T &element : row)
        {
            cin >> element;
        }
    }
}

// aを小さい方に揃える
bool chmin(ll a,ll b){
    if(a>b){
        a=b;
        return true;
    }
    return false;
}

// aを大きい方に揃える
bool chmax(ll a,ll b){
    if(a<b){
        a=b;
        return true;
    }
    return false;
}

// class a,b,...;cin>>a>>b>>...;をCLASS(a,b,...)；にする
template <class Head, class... Tail>
void scan(Head &head, Tail &...tail)
{
    cin >> head;
    scan(tail...);
}

// cout<<a<<endl;をprint(a);にする
template <class T>
void print(const T &t) { cout << t << endl; }

// cout<<a;をprin(a);にする
template <class T>
void prin(const T &t) { cout << t; }

// cout<<a<<b<<...<<endl;をprint(a,b,...)にする
template <class Head, class... Tail>
void print(const Head &head, const Tail &...tail)
{
    cout << head;
    print(tail...);
}

// vector配列を出力
// vecout(vec,' ');と書くとスペースで区切って出力される
// vecout(vec);と書くと一つずつ改行されて出力される
template <class T>
void vecout(const vector<T> &v, char div = '\n')
{
    rep(i, v.size()) cout << v[i] << (i == ll(v.size() - 1) ? '\n' : div);
}

// vec++;で配列の各要素に1が足される
template <class T>
vector<T> &operator++(vector<T> &v, ll)
{
    for (T &t : v)
        t++;
    return v;
}

// vec--;で配列の各要素から1が引かれる
template <class T>
vector<T> &operator--(vector<T> &v, ll)
{
    for (T &t : v)
        t--;
    return v;
}

// vec+=n;で配列の各要素にnが足される
template <class T>
vector<T> &operator+=(vector<T> &v, T x)
{
    for (T &t : v)
        t += x;
    return v;
}

// vec-=n;で配列の各要素からnが引かれる
template <class T>
vector<T> &operator-=(vector<T> &v, T x)
{
    for (T &t : v)
        t -= x;
    return v;
}

// vec*=n;で配列の各要素にnがかけられる
template <class T>
vector<T> &operator*=(vector<T> &v, T x)
{
    for (T &t : v)
        t *= x;
    return v;
}

// vec/=n;で配列の各要素からnが割られる
template <class T>
vector<T> &operator/=(vector<T> &v, T x)
{
    for (T &t : v)
        t /= x;
    return v;
}

// 配列をソートして重複している要素を削除する
template <class T>
void uni(T &a)
{
    sort(all(a));
    a.erase(unique(all(a)), a.end());
}

// 配列をずらして累積和を作る
// もとの配列を用意する
// vi v={a,b,c,d,e};
// 使用例1.ずらす場合
// vi shifted=cumsum<int>(v);
// 使用例2.ずらさない場合
// vi unshifted=cumsum<int>(v);
template <class T, class S>
vector<T> cumsum(const vector<S> &v, bool shift_one = true)
{
    int n = v.size();
    vector<T> res;
    if (shift_one)
    {
        res.resize(n + 1);
        rep(i, n) res[i + 1] = res[i] + v[i];
    }
    else
    {
        res.resize(n);
        if (n)
        {
            res[0] = v[0];
            rep2(i, 1, n) res[i] = res[i - 1] + v[i];
        }
    }
    return res;
}

// 関数
//何かの文字ごとに区切って（その文字は含めずに)elemに格納する
void split(vector<string> &elems, const string &s, char delim)
{
    stringstream ss(s);
    string item;
    while (getline(ss, item, delim))
    {
        if (!item.empty())
            elems.push_back(item);
    }
}

// 二項係数
ll ncr(ll n, ll r)
{
    vvl dp(n + 1, vl(r + 1));
    rep(i, n + 1) dp[i][0] = 1;
    rep(i, r + 1) dp[i][i] = 1;
    rep2(i, 1, n + 1)
    {
        rep2(j, 1, min((ll)i, r + 1))
        {
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
        }
    }
    return dp[n][r];
}

// ユークリッドの互除法(最小公倍数)
unsigned euclidean_gcd(unsigned long long a, unsigned long long b)
{
    if (a < b)
        return euclidean_gcd(b, a);
    unsigned long long r;
    while ((r = a % b))
    {
        a = b;
        b = r;
    }
    return b;
}

// 文字列('1'~'9'で構成される)を好きな数で割ったあまり
ll string_mod(string s, ll mod)
{
    ll rest = 0;
    for (char c : s)
    {
        ll v = c - '0';
        rest = (rest * 10 + v) % mod;
    }
    return rest;
}

// 素数判定
bool IsPrime(ll num)
{
    if (num < 2)
        return false;
    else if (num == 2)
        return true;
    // 偶数はあらかじめ除く
    else if (num % 2 == 0)
        return false;
    double sqrtNum = sqrt(num);
    for (ll i = 3; i <= sqrtNum; i += 2)
    {
        if (num % i == 0)
        {
            // 素数ではない
            return false;
        }
    }
    // 素数である
    return true;
}

// 平方数判定(ニュートン法)
bool isSquare(int n)
{
    int i = n;
    while (i * i > n)
    {
        i = (i + n / i) / 2;
    }
    return i * i == n;
}

// 各桁の和
ll digit_sum(ll n)
{
    ll sum = 0;
    while (n)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// 桁数を返す
ll digit_get(ll num)
{
    ll digit = 0;
    while (num != 0)
    {
        num /= 10;
        digit++;
    }
    return digit;
}

// 文字列の種類
ll kind_char(string s)
{
    SORT(s);
    auto itr = unique(s.begin(), s.end());
    s.erase(itr, s.end());
    return SZ(s);
}

// Union Find(dsu)木
struct UnionFind
{
    vector<int> par, rank, siz;

    // 構造体の初期化
    UnionFind(int n) : par(n, -1), rank(n, 0), siz(n, 1) {}

    // 根を求める
    int root(int x)
    {
        if (par[x] == -1)
            return x; // x が根の場合は x を返す
        else
            return par[x] = root(par[x]); // 経路圧縮
    }

    // x と y が同じグループに属するか (= 根が一致するか)
    bool issame(int x, int y)
    {
        return root(x) == root(y);
    }

    // x を含むグループと y を含むグループを併合する
    bool unite(int x, int y)
    {
        int rx = root(x), ry = root(y); // x 側と y 側の根を取得する
        if (rx == ry)
            return false; // すでに同じグループのときは何もしない
        // union by rank
        if (rank[rx] < rank[ry])
            swap(rx, ry); // ry 側の rank が小さくなるようにする
        par[ry] = rx;     // ry を rx の子とする
        if (rank[rx] == rank[ry])
            rank[rx]++;     // rx 側の rank を調整する
        siz[rx] += siz[ry]; // rx 側の siz を調整する
        return true;
    }

    // x を含む根付き木のサイズを求める
    int size(int x)
    {
        return siz[root(x)];
    }
};

// ライブラリ使用のための関数

// ここから
// N進→10進変換(N<=36)
int ntodec(const char c)
{
    switch (c)
    {
    case '0':
        return 0;
    case '1':
        return 1;
    case '2':
        return 2;
    case '3':
        return 3;
    case '4':
        return 4;
    case '5':
        return 5;
    case '6':
        return 6;
    case '7':
        return 7;
    case '8':
        return 8;
    case '9':
        return 9;
    case 'A':
        return 10;
    case 'B':
        return 11;
    case 'C':
        return 12;
    case 'D':
        return 13;
    case 'E':
        return 14;
    case 'F':
        return 15;
    case 'G':
        return 16;
    case 'H':
        return 17;
    case 'I':
        return 18;
    case 'J':
        return 19;
    case 'K':
        return 20;
    case 'L':
        return 21;
    case 'M':
        return 22;
    case 'N':
        return 23;
    case 'O':
        return 24;
    case 'P':
        return 25;
    case 'Q':
        return 26;
    case 'R':
        return 27;
    case 'S':
        return 28;
    case 'T':
        return 29;
    case 'U':
        return 30;
    case 'V':
        return 31;
    case 'W':
        return 32;
    case 'X':
        return 33;
    case 'Y':
        return 34;
    case 'Z':
        return 35;
    default:
        return -1;
    }
}

// 10進→N進変換(N<=36)
char decton(const ll n)
{
    switch (n)
    {
    case 0:
        return '0';
    case 1:
        return '1';
    case 2:
        return '2';
    case 3:
        return '3';
    case 4:
        return '4';
    case 5:
        return '5';
    case 6:
        return '6';
    case 7:
        return '7';
    case 8:
        return '8';
    case 9:
        return '9';
    case 10:
        return 'A';
    case 11:
        return 'B';
    case 12:
        return 'C';
    case 13:
        return 'D';
    case 14:
        return 'E';
    case 15:
        return 'F';
    case 16:
        return 'G';
    case 17:
        return 'H';
    case 18:
        return 'I';
    case 19:
        return 'J';
    case 20:
        return 'K';
    case 21:
        return 'L';
    case 22:
        return 'M';
    case 23:
        return 'N';
    case 24:
        return 'O';
    case 25:
        return 'P';
    case 26:
        return 'Q';
    case 27:
        return 'R';
    case 28:
        return 'S';
    case 29:
        return 'T';
    case 30:
        return 'U';
    case 31:
        return 'V';
    case 32:
        return 'W';
    case 33:
        return 'X';
    case 34:
        return 'Y';
    case 35:
        return 'Z';
    default:
        return '\0';
    }
}

// べき乗計算(long long型）
inline long long pow_ll(long long x, long long n)
{
    long long ret = x;
    if (n == 0)
        return 1;
    for (long long i = 1; i < n; i++)
    {
        ret *= x;
    }
    return ret;
}
// ここまで

// 文字列strをn進数からm進数に変換
string n_ary(string str, ll n, ll m)
{
    unsigned long tmp = 0;
    string ret;
    for (ll i = 0; i < (ll)str.length(); i++)
    {
        tmp += (unsigned long)ntodec(str[str.length() - 1 - i]) * pow_ll(n, i);
    }
    if (tmp == 0)
        return "0";
    while (tmp != 0)
    {
        ret = decton(tmp % m) + ret;
        tmp /= m;
    }
    return ret;
}

ll mmax(ll a, ll b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

ll mmin(ll a, ll b)
{
    if (a < b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

// const
// 円周率
const ld PI = 3.1415926535897932;
// infinity
const int INF = 1001001001;
const ll LINF = 1001001001001001001;
// mod
const int bigMOD = 1000000007;
int smallMOD = 998244353;
// direction
const int dx[] = {0, 1, 0, -1, 1, -1, 1, -1};
const int dy[] = {1, 0, -1, 0, 1, 1, -1, -1};
// alphabet
const string ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string alphabet = "abcdefghijklmnopqrstuvwxyz";
/*memo
最小公倍数 lcm
最大公約数 gcd
絶対値 abs

配列の先頭に要素を追加 vec.insert(vec.begin(),n)

型変換 s_c<変更先の型>(変更前の値)

x^n mod m pow_mod(x,n,m)
*/
/*-----------------------------------------------------*/

/*----------------------main code----------------------*/
// global変数の定義、関数の作成など
/*-----------------------------------------------------*/
int main()
{
// 入出力を高速化
cin.tie(nullptr);
cout.tie(nullptr);
// cinとcoutの同期を切る
ios::sync_with_stdio(false);
// 小数の出力を小数点以下15桁にする
cout << fixed << setprecision(15);
// 実行ごとに乱数生成結果を変える
srand((unsigned)time(NULL));
// 実行時間の計測開始
// int startofrestime=clock();
/*-----------------------------------------------------*/
/*---------------------------実装-----------------------*/
INT(m);vs s(3);

rep(i,3){
    cin>>s[i];
}

vvb flag(3,vb(10,0));vi no;

rep(i,10){
    rep(j,3){
        rep(k,m){
            if(s[j][k]==i+'0'){
                flag[j][i]=1;
            }
        }
    }
}

rep(i,10){
    if(!(flag[0][i]&&flag[1][i]&&flag[2][i])){
        no.pb(i);
    }
}
//ここまであってる
if(SZ(no)==10){
    print(-1);
    return 0;
}
//ここまであってる
int num[]={0,1,2};
int mn=1e9;
rep(i,10){
    bool noflag=0;
    rep(j,SZ(no)){
        if(no[j]==i){
            noflag=1;
        }
    }
    if(noflag){
        continue;
    }
    //ここまであってる
    //順列全探索
    do{
        int ans=0;
        rep(j,3){
            rep2(k,ans+1,m*3+1){
                if(s[num[j]][k%m]==i+'0'){
                    ans=k;
                    break;
                }
            }
        }
        if(ans<=mn){
            mn=ans;
        }
    }while(next_permutation(num,num+3));
}

print(mn);
// 実行時間の計測終了
// int endofrestime=clock();restime
}