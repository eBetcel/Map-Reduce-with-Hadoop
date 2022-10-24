from pymongo_hadoop import BSONMapper
def mapper(documents):
    for doc in documents:
    	yield {'_id': doc['user_id'], 'city': doc['location']['city']}

BSONMapper(mapper)
