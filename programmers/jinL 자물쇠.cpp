#include<iostream>
#include <string>
#include <vector>

using namespace std;

void clockwise_rotate(vector<vector<int> >& key) {
    int m = key.size();
    vector<vector<int> > temp(m, vector<int>(m, 0));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            temp[i][j] = key[j][m - i - 1];
            //temp[i][j] = key[m - j - 1][i];
        }
    }
    key = temp;
    return;
}

bool solution(vector<vector<int> > key, vector<vector<int> > lock) {
    int lock_s = lock.size();
    int key_s = key.size();
    vector<int[2]> sol_lock;
    vector<int[2]> sol_key;
    bool answer = true;
    
    for (int i = 0; i < lock_s; i++) {
        for (int j = 0; j < lock_s; j++)
            if (lock[i][j] == 0)
                sol_lock.push_back({ i,j });
    }
    for (int i = 0; i < key_s; i++) {
        for (int j = 0; j < key_s; j++)
            if (key[i][j] == 1)
                sol_key.push_back({ i,j });
    }
    
    for(int i = 1 - key_s;i<lock_s - 1;i++)
        for (int j = 1 - key_s; j < lock_s - 1; j++) {
            vector<int[2]>::iterator iter = sol_lock.begin();
            vector<int[2]>::iterator iter2 = sol_key.begin();
            while (iter != sol_key.end()) {

            }
        }
            

    
    return answer;
}
