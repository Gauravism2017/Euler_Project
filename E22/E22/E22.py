def sortNames(_from, _to, wordPos):
    for _word in range (ord('A') - 1, ord('Z') + 1):
        if(_to - _from  < 2 ):
            return
        _iter = 0
        curWord = chr(_word)
        for namePos in range(_iter + _from, _to):
            if wordPos >= len(allNames[namePos]) or allNames[namePos][wordPos] == curWord:
                if _iter + _from != namePos:
                    allNames[namePos], allNames[_iter + _from] = allNames[_iter + _from], allNames[namePos]
                _iter += 1
        if ( _iter >= 1):
            sortNames(_from, _iter + _from, wordPos + 1)
            _from = _iter + _from

allNames = [input() for _ in range(int(input()))]
sortNames(0, len(allNames), 0)

score = {}
points = [0 for _ in range(len(allNames))]
for inx, name in enumerate(allNames):
    for word in name:
        points[inx] += ord(word) - ord('A') + 1;
    score[name] = points[inx] * (inx  + 1)
for _ in range(int(input())):
    print(score[input()])
