""" 
1. 目標をTODOリストとして書き出す
2. TODOリストから一つピックアップし、テストを書く
3. テストコードを実行して失敗させる（レッド）
4. 実装コードを書く（仮実装）
5. できる限り最短でテストが通るコードを実装する（グリーン）
6. コードの重複を除去する（リファクタリング）
7. 次のTODOを選び、2に進む
 """

#[ ] L,R,U,Dのいずれかの文字を渡した時、YesまたはNoを返す
    #[X] 文字Rを渡した時、Yesを返す
    #[ ] 文字Uを渡した時、Yesを返す
    #[ ] 文字Dを渡した時、Yesを返す
    #[X] 文字Lを渡した時、Noを返す

#[ ] 奇数文字目の少なくとも1つがLである場合、Noを返す
    #[ ] 文字列LRRを渡した時、Noを返す
#[ ] 偶数文字目の少なくとも1つがRである場合、Noを返す
    #[ ] 文字列LRRを渡した時、Noを返す

import unittest


class SampleTest(unittest.TestCase):
    sample = None

    def setUp(self):
        self.sample = Sample()

    def testReturnR(self):
        result = self.sample.solve('R')
        self.assertEqual('Yes',result)

    def testReturnL(self):
        result = self.sample.solve('L')
        self.assertEqual('No',result)


class Sample:
    def solve(self,s):
        if s == 'L':
            return 'No'
        
        return 'Yes'


if __name__ == '__main__':
    unittest.main()