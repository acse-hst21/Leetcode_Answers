class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, im1 = num1.split('+')
        im1 = im1[:-1]
        real1, im1 = int(real1), int(im1)

        real2, im2 = num2.split('+')
        im2 = im2[:-1]
        real2, im2 = int(real2), int(im2)

        real_output = (real1 * real2) - (im1 * im2)
        im_output = (real1 * im2) + (real2 * im1)

        final_output = str(real_output) + '+' + str(im_output) + 'i'
        
        return final_output
