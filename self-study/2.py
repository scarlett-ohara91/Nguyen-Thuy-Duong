import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242 and 415-555-4243.')
print('Phone number found: ' + mo.groups())          # chi search ra 1 cai dau tien ah?