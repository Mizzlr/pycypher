from pycypher import parse
import json

query_string = "MATCH (n) RETURN Count(n);"
statement = """MATCH (is:IfStatement)-[:condition]->(le:LiteralExpression) WHERE toLower(le.type) =~ ".*bool.*" AND le.value = "false" RETURN is.col as col, is.line as line, is.file as file UNION MATCH (is:IfStatement)-[:condition]->()-[:tree_edge*0..7]->(ie:InfixExpression)-[:left|right]->(le:LiteralExpression) WHERE toLower(le.type) =~ ".*bool.*" AND le.value = "false" AND ie.operator = "&&" RETURN is.col as col, is.line as line, is.file as file UNION MATCH (md:MethodDeclaration)-[:body]->(:Block)-[:statement]->(st) WITH md, count(st) as stcnt WHERE stcnt > 1 MATCH (md)-[:body]->(:Block)-[:statement]->(rs:ReturnStatement) WITH md, count(rs) as rscnt, stcnt WHERE rscnt = stcnt RETURN md.col as col, md.line as line, md.file as file"""


query_string = """
MATCH (is:IfStatement)-[:condition]->(le:LiteralExpression)
WHERE toLower(le.type) =~ ".*bool.*"
AND le.value = "false"
RETURN is.col as col, is.line as line, is.file as file
UNION
MATCH (is:IfStatement)-[:condition]->()-[:tree_edge*0..7]->
(ie:InfixExpression)-[:left|right]->(le:LiteralExpression)
WHERE toLower(le.type) =~ ".*bool.*"
AND le.value = "false" AND ie.operator = "&&"
RETURN is.col as col, is.line as line, is.file as file
"""

q = """
UNION MATCH (md:MethodDeclaration)-[:body]->(:Block)-[:statement]->(st)
WITH md, count(st) as stcnt
WHERE stcnt > 1
MATCH (md)-[:body]->(:Block)-[:statement]->(rs:ReturnStatement)
WITH md, count(rs) as rscnt, stcnt WHERE rscnt = stcnt
RETURN md.col as col, md.line as line, md.file as file;
"""


print(json.dumps(parse(query_string), indent=4))
