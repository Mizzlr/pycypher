from pycypher import parse
import json

query_string = "MATCH (n) RETURN Count(n);"
print(json.dumps(parse(query_string), indent=4))
