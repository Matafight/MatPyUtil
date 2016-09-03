import re

m= re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world')

print "m.string:",m.string
print "m.re:",m.re
print "m.pos:",m.pos
print "m.endpos:",m.endpos
print "m.lastindex:",m.lastindex
print "m.lastgroup:",m.lastgroup
print "m.group():",m.group(1)
