class Solution:
	def subsetSums(self, arr):
		sums = [0]
		
		for num in arr:
		  #  new_sums = []
		  #  for s in sums:
		  #      new_sums.append(s + num)
		  #  sums += new_sums
		  sums += [s + num for s in sums]
		return sums
		        
		