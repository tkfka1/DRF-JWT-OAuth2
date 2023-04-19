import base64

code = '7JWI64WVPw=='
code_bytes = code.encode('ascii')

decoded = base64.b64decode(code_bytes)
str = decoded.decode('UTF-8')
print(str)


str = 'test'
bytes = str.encode('UTF-8')

result = base64.b64encode(bytes)
result_str = result.decode('ascii')
print(result_str)