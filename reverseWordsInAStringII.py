class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        my_str = ''.join(str)
        str_list = my_str.split(' ')
        str_list.reverse()
        new_str = ' '.join(str_list)
        for i in range(len(new_str)):
            str[i] = new_str[i]