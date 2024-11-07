def rail_fence_encrypt(text, rails):
    if rails == '':
        rails = int(5)
    else:
        rails = int(rails)
    fence = [[] for _ in range(rails)]
    rail = 0
    var = 1

    for char in text:
        fence[rail].append(char)
        rail += var
        if rail == 0 or rail == rails - 1:
            var = -var

    return ''.join(''.join(row) for row in fence)

def rail_fence_decrypt(cipher, rails):
    if rails == '':
        rails = int(5)
    else:
        rails = int(rails)
    fence = [[] for _ in range(rails)]
    rail = 0
    var = 1

    for i in range(len(cipher)):
        fence[rail].append(None)
        rail += var
        if rail == 0 or rail == rails - 1:
            var = -var

    idx = 0
    for row in fence:
        for j in range(len(row)):
            row[j] = cipher[idx]
            idx += 1

    rail = 0
    var = 1
    result = []
    for i in range(len(cipher)):
        result.append(fence[rail].pop(0))
        rail += var
        if rail == 0 or rail == rails - 1:
            var = -var

    return ''.join(result)