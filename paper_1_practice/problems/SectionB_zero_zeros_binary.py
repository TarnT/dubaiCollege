def zeroZeroesBinary(num):

    return int(f"0{bin(num).replace('0', '')}", base=2) if num > 0 else -1

print(zeroZeroesBinary(-10))