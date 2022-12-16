import sys
import re

def reglink(html):
    try:
        return re.find(b'src="(http://.*?)"',html)
    except Exception:
        return None

html = input("HTML: ")
sys.exit(reglink(html))