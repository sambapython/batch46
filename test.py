from app import fun
import unittest
class AppTest(unittest.TestCase):
	@classmethod
	def tearDownClass(cls):
		cls.user=None
		print "logout"
	def setUp(self):
		print self.user
	def tearDown(self):
		print "test completed"

	def test_10_20(self):
		#print self.user
		sop=30
		actop=fun(10,20)
		self.assertTrue(sop==actop,"test_10_20 is failed")
		#print "test completed"
	def test_s1_s2(self):
		#print self.user
		sop="s1s2"
		actop=fun("s1","s2")
		self.assertEqual(sop,actop,"test_s1_s2 is failed")
		#print "test completed"
	def test_s1_20(self):
		#print self.user
		sop=None
		actop=fun("s1",20)
		self.assertTrue(sop==actop,"test_s1_20 is failed")
		#print "test completed"
	def test_10_s2(self):
		print self.user
		sop=None
		actop=fun(10,"s2")
		self.assertTrue(sop==actop,"test_10_s2 is failed")
		#print "test completed"
	@classmethod
	def setUpClass(cls):
		print "this is for login"
		cls.user="usertname"
#unittest.main()
