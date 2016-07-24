from subprocess import call
import sys

if __name__ == "__main__":
    code = call(["xmllint", "--valid", "--noout", "rulebook.xml"])
    
    if code == 0:
        print "OK"
    else:
        sys.exit(1)