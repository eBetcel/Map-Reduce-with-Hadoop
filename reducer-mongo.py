from pymongo_hadoop import BSONReducer

def reducer(key, values):
    _count = _sum = 0
    for v in values:
        _count += 1
        _sum += v['bc10Year']
    return {'_id': key, 'avg': _sum / _count,
            'count': _count, 'sum': _sum }

BSONReducer(reducer)
