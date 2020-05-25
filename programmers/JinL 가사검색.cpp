#include <iostream>
#include <string>
#include <vector>

using namespace std;
const int ALPHABET = 26;
// 소문자를 index로 바꾸기
int char_to_index(char c) {
    int index;
    if (c == '?')                               //와일드 키 ?를 확인하기
        index = 26;
    else
        index = (c) - 'a';
    return index;
}
struct trie{
    bool is_terminal;                           // 문자열의 끝을 확인
    trie* next[ALPHABET];

    trie():is_terminal(false){
        for (int i = 0; i < ALPHABET; i++)
            next[i] = 0;
    }
    ~trie() {
        for (int i = 0; i < ALPHABET; i++)
            if (next[i])
                delete(next[i]);
    }
    void insert(const char* key) {
        if (*key == '\0')
            is_terminal = true;
        else {
            int index = char_to_index(*key);
            if (next[index] == 0)
                next[index] = new trie();
            next[index]->insert(key + 1);
        }
    }
    bool is_exist(const char* key,const char* word) {
        if (*key == 0 && is_terminal)
            return true;
        if (*word == 0)
            return false;
        int index = char_to_index(*key);
        int index2 = char_to_index(*word);
        if (index == 26) {
            index = index2;
        }
        else if (index != index2)
            return false;
        if (next[index] == 0)
            return false;
        return next[index]->is_exist(key + 1,word+1);
    }
};

vector<int> solution(vector<string> words, vector<string> queries) {
    vector<int> answer;
    answer = vector<int>(queries.size(), 0);
    trie* root = new trie();
    vector<string>::iterator iter = words.begin();
    while (iter != words.end()) {
        root->insert((*iter).c_str());
        iter++;
    }
    iter = words.begin();
    while (iter != words.end()) {
        for (int i = 0; i < queries.size(); i++) {
            string key = queries.at(i);
            
            if (key.size() != (*iter).size())
                continue;
            else {
                if (root->is_exist(queries.at(i).c_str(), (*iter).c_str()))
                    answer[i]++;
            }
        }
        iter++;
    }
    delete(root);
    return answer;
}
