import logging
logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s-->>%(levelname)s==>%(message)s",
    filename="log.txt")
logging.info("program started")
a=raw_input("Enter a value:")
logging.info("Got the a value from the user")
b=raw_input("Enter b value:")
logging.info("Got the b value from the user")
logging.debug("before conversion a=%s,b=%s"%(a,b))
try:
    a=float(a)
    logging.info("safely converted a")
    b=float(b)
    logging.info("safely converted b")
    logging.debug("after conversion a=%s,b=%s"%(a,b))
    res=a/b
    logging.info("Result calculation completed")
    print "result=%s"%res
    logging.debug("result=%s"%res)
except ZeroDivisionError as err:
    print "ERROR:%s"%err.message
    logging.error("ERROR:%s"%err.message)
    print "Enter b value not equal to zero"    
    logging.error("Enter b value not equal to zero")
except Exception as err:
    logging.error("ERROR:%s"%err.message)
    print "ERROR:%s"%err.message
    logging.error("some error")
    print "some error"
print "other statements in program"
print "program ended"
print "main block"
logging.info("COMPLETED!!!")