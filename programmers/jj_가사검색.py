# 트라이
from collections import defaultdict

class Node(object):
    """
    A node that consist of a trie.
    """

    def __init__(self, char, length = None, data=None):
        self.char = char
        self.data = None
        self.children={}
        self.length = defaultdict(int)

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    트라이에 문자열을 삽입합니다.
    """
    def insert(self,string):
        curr_node = self.head
        curr_node.length[len(string)] += 1

        for char in string :
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            # 해당 노드를 거쳐가는 문자열 중 길이가 len(string)인 것의 개수를 저장한다.
            curr_node.children[char].length[len(string)] += 1
            curr_node = curr_node.children[char]

            # string의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.data = string

    def start_with(self,prefix, length):
        """
        주어진 prefix로 시작하고 길이가 같은 단어의 수를 트라이에서 찾아 반환합니다.
        """
        curr_node = self.head

        # 트라이에서 prefix를 찾고
        # prefix의 마지막 글자 노드를 subtrie로 설정
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0

        return curr_node.length[length]


def solution(words, queries):
    answer = []
    front = Trie()
    back = Trie()

    for word in words:
        front.insert(word)
        back.insert(word[::-1])
    for word in queries:
        # 전부 ? 일 경우 - 문자열 길이만 일치하면 된다.
        if word == "?"*len(word):
            answer.append(front.head.length[len(word)])

        # 맨 앞 글자가 ?인 경우는 역방향 트라이를 사용한다.
        elif word[0] == '?':
            prefix = word[::-1].split("?")[0]
            answer.append(back.start_with(prefix,len(word)))
        else:
            prefix = word.split('?')[0]
            answer.append(front.start_with(prefix,len(word)))
    return answer

word = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?","?????"]

print(solution(word,queries))