import hashlib

print("디코딩할 SHA256 코드를 아래에 넣어주십시오.")
sha256_string = input('> ')

print("디코딩 중..")

try:
    for i in range(10):
        str = str.replace(hashlib.sha256(chr(i).encode()).hexdigest(), chr(i))

    print("디코딩에 성공하였습니다.")
    print('결과: ' + str)
except:
    print("디코딩에 실패하였습니다.")
    print("해당 코드가 정확한지 확인해주십시오.")