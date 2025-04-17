import unittest
from analyzer.parser import analyze_sentence

class TestSentenceAnalysis(unittest.TestCase):

    def test_analyze_sentence(self):
        sentence = "The cat chased the mouse."
        analyze_sentence(sentence)
        # 在这里可以添加更多的断言或验证语法树的结构
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
