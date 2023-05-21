# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    queries = []
    for i in range(n):
        query = input().split()
        queries.append(Query(query))
    return queries

def write_responses(result):
    for response in result:
        print(response)

def process_queries(queries):
    result = []
    contacts = {}
    for query in queries:
        if query.type == 'add':
            contacts[query.number] = query.name
        elif query.type == 'del':
            if query.number in contacts:
                del contacts[query.number]
        else:
            response = 'not found'
            if query.number in contacts:
                response = contacts[query.number]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

