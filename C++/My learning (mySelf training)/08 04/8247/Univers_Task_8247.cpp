#include <iostream>
#include <string>
using namespace std;

int n;
long long tree[101];

void update(int i, long long val) {
    while (i <= n) {
        tree[i] += val;
        i = i + (i & (-i));
    }
}

int main() {
    cin >> n;
    
    long long a[101];
    for (int i = 1; i <= n; i++) {
        cin >> a[i];
    }
    
    for (int i = 1; i <= n; i++) {
        update(i, a[i]);
        
        for (int j = 1; j <= n; j++) {
            if (j > 1) cout << " ";
            cout << tree[j];
        }
        cout << "\n";
    }
    
    return 0;
}