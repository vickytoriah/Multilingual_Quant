class Solution:
	
	def mergeAlternately(
		self,
		word1: str,
		word2: str,
	) -> str:
		"""
        You are given two strings word1 and word2.
        Merge the strings by adding letters in alternating order, starting with word1.
        If a string is longer than the other, append the additional letters onto the end of the merged string.
        Return the merged string.
        :param word1:
        :param word2:
        :return: Runtime 25 ms, beats 97.49%; memory 16.42 mb beats 72.20%
        """
		
		i = 0
		list_str = []
		while i < int(min(len(word1), len(word2)) * 2):
			if i % 2 == 0:
				list_str.append(word1[int(i // 2)])
			else:
				list_str.append(word2[int(i // 2)])
			i += 1
		
		if len(word1) == len(word2):
			return ''.join(list_str)
		else:
			diff_ind = int(len(word2) - len(word1))
			if diff_ind > 0:
				return ''.join(list_str) + word2[-diff_ind:]
			else:
				return ''.join(list_str) + word1[diff_ind:]
			


if __name__ == '__main__':
	breakpoint()
