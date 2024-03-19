class Solution:
    def defangIPaddr(self, address: str) -> str:
        nums = address.split('.')
        output = ''
        for num in nums:
            output += num + '[.]'
        return output[:-3]
