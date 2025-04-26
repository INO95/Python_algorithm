import re

pattern = re.compile(r'\w{3,4}')

print(pattern)

# r-string에서 r은 raw로 문자열 그대로 사용하게 해준다.


pattern2 = re.compile('[a-z]+')
m = pattern2.match('helloworld')
print(m)

m2 = pattern2.match('HelloWorld')
print(m2)

pattern3 = re.compile('[a-z]+', re.IGNORECASE)
m3 = pattern3.match('HelloWorld')
print(m3)

pattern4 = re.compile('[a-z]+')
m4 = pattern4.search('This is for search()')
print(m4)

m5 = pattern4.findall('This is for findall()')
print(m5)
