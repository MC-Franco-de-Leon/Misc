
#python ~/Documents/'more applications'/ElementsofProgrammingInterviews/tetsingHRsherlocksAndAnagrams.py
import unittest
import HRsherlocksAndAnagrams




class testHRsherlocksAndAnagrams(unittest.TestCase):
	def test_strings(self):
		string2='abba'
		string3='abcd'
		string4='ifailuhkqq'
		string5='kkkk'
		string6='cdcd'
		self.assertEqual(HRsherlocksAndAnagrams.sherlockAndAnagrams(string2),4)
		self.assertEqual(HRsherlocksAndAnagrams.sherlockAndAnagrams(string3),0)
		self.assertEqual(HRsherlocksAndAnagrams.sherlockAndAnagrams(string4),3)
		self.assertEqual(HRsherlocksAndAnagrams.sherlockAndAnagrams(string5),10)
		self.assertEqual(HRsherlocksAndAnagrams.sherlockAndAnagrams(string6),5)






if __name__=='__main__':
	print('Unit testing HRsherlocksAndAnagrams')
	unittest.main()


	
	
