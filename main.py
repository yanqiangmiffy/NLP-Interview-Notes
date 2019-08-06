def reorderedPowerOf2(N):
    m = [sorted(list(str(2 ** i))) for i in range(30)]
    if sorted(list(str(N))) in m:
        return True
    else:
        return False
if __name__ == '__main__':
    print(reorderedPowerOf2(64))
