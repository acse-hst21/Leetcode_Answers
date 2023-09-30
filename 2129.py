class Solution:
    def capitalizeTitle(self, title: str) -> str:
        if len(title) == 1 or len(title) == 2:
            return title.lower()
        lower_title = title.lower()

        if lower_title[1] == ' ' or lower_title[2] == ' ':
            where_words_start = []
        else:
            where_words_start = [0]

        for index, value in enumerate(lower_title[:-3]):
            if value == ' ' and lower_title[index + 2] != ' ' and lower_title[index + 3] != ' ':
                where_words_start.append(index + 1)
        
        output = ''

        for index, value in enumerate(lower_title):
            if index in where_words_start:
                output += value.upper()
            else:
                output += value
        return output
