
#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/HRsherlocksAndAnagrams.py

#counts the number of anagrams substrings in a given string


class savers:
	def __init__(self, hashes=None,hash_table=None):
		self.hashes=dict()
		self.hash_table=dict()
	def gethash(self,s):
		if s in self.hashes:
			hash_val=self.hashes[s]
		else:
			hash_val=1
			for char in s:
				hash_val*=prime_map(char)		
		self.hashes[s]=hash_val
		return hash_val
	def save_hash(self,string2,hash1):
		hash2=self.gethash(string2)
		if hash1==hash2:
			if hash2 in self.hash_table:
				self.hash_table[hash2]+=1
			else:
				self.hash_table[hash2]=1
def prime_map(c):
	primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101)
	#print(ord(c))
	return primes[ord(c) - ord('a')]


def sherlockAndAnagrams(string):
	ns=len(string)
	saver=savers()
	#print(saver.hashes)
	#print(saver.hash_table)
	for length in range(1,ns):
		for idx_start in range(0,ns-length):
			string1=string[idx_start:idx_start+length]
			hash1=saver.gethash(string1)
			for j in range(idx_start+1,ns-length+1):
				string2=string[j:j+length]
				saver.save_hash(string2,hash1)
	return sum([val for (key,val) in saver.hash_table.items()])
if __name__=='__main__':
	print('Number of anagrammatic substrings')
	string='aa'
	string2='abba'
	string3='abcd'
	string4='ifailuhkqq'
	string5='kkkk'
	string6='cdcd'

#	print('number of anagrams',sherlockAndAnagrams(string))
	print('number of anagrams 2',sherlockAndAnagrams(string2))
	print('number of anagrams 3',sherlockAndAnagrams(string3))
	print('number of anagrams 4',sherlockAndAnagrams(string4))
	print('number of anagrams 5',sherlockAndAnagrams(string5))
	print('number of anagrams 6',sherlockAndAnagrams(string6))
	
