#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main() {
	int N;
	cin >> N;
	queue <int> cards;
	for (int i = 0; i < N; i++)
		cards.push(i + 1);

	while (cards.size() != 1) {
		cards.pop();
		cards.push(cards.front());
		cards.pop();
	}
	cout << cards.back() << endl;
}
