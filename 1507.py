class Solution:
    def reformatDate(self, date: str) -> str:
        month = date[-8:-5]
        try:
            int(date[1])
            day = date[:2]
        except ValueError:
            day = '0'+date[:1]
        month_to_num = {'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'}
        return f'{date[-4:]}-{month_to_num[month]}-{day}'
