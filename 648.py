class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        output = []
        sentence_list = sentence.split()
        for word in sentence_list:
            replaced = False
            for root in dictionary:
                if word.startswith(root):
                    output.append(root)
                    replaced = True
                    break
            if not replaced:
                output.append(word)
        return ' '.join(output)
