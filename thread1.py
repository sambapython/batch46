"""
To explain threading
"""
from time import sleep
import threading


def fun():
    """
    to explain thread target
    """
    for i in range(5):
        sleep(1)
        print i


'''
t1=threading.Thread(target=fun)
t2=threading.Thread(target=fun)
t3=threading.Thread(target=fun)

fun()
fun()
fun()

t1.start()
t2.start()
t3.start()


for i in range(3):
    t1=threading.Thread(target=fun,name="thread%s"%i)
    t1.start()
'''


def send_msg(msg, phone):
    """
    to send message
    """
    print "sending message:%s to %s" % (msg, phone)
    sleep(2)
    print "sent message for %s" % phone


phone_numbers = map(lambda x: "number:%s" % x, range(100))
msg = "Today is the last day to batch45 and 46 student"
for num in phone_numbers:
    t1 = threading.Thread(target=send_msg, name="thread%s" % num,
                          args=(msg, num))
    t1.start()
