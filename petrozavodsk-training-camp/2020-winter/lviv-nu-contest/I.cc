#include <cstdio>
#include <vector>
#include <algorithm>

int rec(std::vector<int> &A, std::vector<int> &B) {
  if (A.empty() || A.back() < B[0]) return 0;
  if (A[0] > B.back()) return A.size();
  int n = A.size();
  int best_i = -n, best_j = n;
  for (int i = 0, j = 0; i < n; ++i) {
    while (j < n && A[i] >= B[j]) ++j;
    if (j < n && best_i - best_j < i - j) {
      best_i = i;
      best_j = j;
    }
  }
  A.erase(A.begin() + best_i);
  B.erase(B.begin() + best_j);
  return n - 1 - rec(B, A);
}

int main() {
  int n;
  scanf("%d", &n);
  std::vector<int> A(n), B(n);
  for (int i = 0; i < n; ++i) scanf("%d", &A[i]);
  for (int i = 0; i < n; ++i) scanf("%d", &B[i]);
  std::sort(A.begin(), A.end());
  std::sort(B.begin(), B.end());
  printf("%d\n", rec(A, B));
  return 0;
}