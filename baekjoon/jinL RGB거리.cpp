#include <iostream>
using namespace std;
const int INF = 1000000000;
int cost[1000][3] = { INF };			//0: 빨강 비용, 1: 초록 비용, 2: 파랑 비용
int dp[1000][3] = { INF };
//			        현재 집    이전 집 색깔
int find_min(int index, int last_color) {
	if (index < 0)
		return 3;
	int result = 0;
	if (last_color == 0)
		result++;
	for (int i = 0; i < 3; i++)
		if (i == last_color)
			continue;
		else
			result = dp[index][i] < dp[index][result] ? i : result;
	return result;
}

int main() {
	int input;
	
	cin >> input;
	for (int i = 0; i < input; i++) {
		cin >> cost[i][0] >> cost[i][1] >> cost[i][2];
	}
  // 첫번째 집은 비용 그대로
	for (int i = 0; i < 3; i++)
		dp[0][i] = cost[0][i];
  // bottom up
	for (int i = 1; i < input; i++) {
		for (int j = 0; j < 3; j++) {

			dp[i][j] = cost[i][j] + dp[i - 1][find_min(i - 1, j)];
		}
	}
	input--;
	int min = dp[input][0] < dp[input][1] ? dp[input][0] : dp[input][1];
	min = min < dp[input][2] ? min : dp[input][2];
	cout << min << endl;
}
