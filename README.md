# pycypher

A Python parser for the [Cypher](https://neo4j.com/docs/cypher-manual/current/) graph query language. Parses Cypher query strings into Abstract Syntax Trees (ASTs).

Built on [ANTLR 4](https://www.antlr.org/) with a patched [openCypher](https://opencypher.org/) grammar that supports modern Cypher features including subqueries, FOREACH, shortestPath, and more.

## Installation

```bash
pip install pycypher
```

## Quick Start

```python
from pycypher import parse

result = parse('MATCH (n:Person)-[:KNOWS]->(m) WHERE m.age > 30 RETURN n.name, m.name;')

# Check for parse errors
print(result['errors'])  # []

# Access the AST
for node in result['result']:
    print(node['node']['parent'], '->', node['node']['text'][:50])
```

## API

### `parse(query_string) -> dict`

Parses a Cypher query string and returns an AST dictionary.

**Parameters:**
- `query_string` (str): A Cypher query (e.g., `"MATCH (n) RETURN n;"`)

**Returns:** A dict with two keys:
- `result` - List of AST nodes. Each node has:
  - `node` - Dict with `parent` (rule name), `text` (source text), `sourceInterval` (token range)
  - `children` - Nested dict with `result` (child nodes) and `errors` (child parse errors)
- `errors` - List of top-level parse error nodes

### `__version__`

Package version string (e.g., `"1.0.0"`).

## Supported Cypher Features

### Clauses
MATCH, OPTIONAL MATCH, WHERE, RETURN, WITH, UNWIND, UNION, ORDER BY, SKIP, LIMIT, DISTINCT

### Mutations
CREATE, MERGE (ON CREATE / ON MATCH), SET, DELETE, DETACH DELETE, REMOVE, FOREACH

### Expressions
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `^`
- Comparison: `=`, `<>`, `<`, `>`, `<=`, `>=`
- Boolean: `AND`, `OR`, `XOR`, `NOT`
- String: `STARTS WITH`, `ENDS WITH`, `CONTAINS`
- Null: `IS NULL`, `IS NOT NULL`
- Lists: `IN`, list literals, list comprehensions
- Maps: map literals, map projections
- CASE / WHEN / THEN / ELSE / END
- Parameters: `$param`

### Patterns
- Node patterns: `(n)`, `(n:Label)`, `(n:Label {prop: value})`
- Relationship patterns: `-[r:TYPE]->`, `<-[:TYPE]-`, `-[:TYPE]-`
- Variable-length paths: `[*]`, `[*2]`, `[*1..3]`, `[*..5]`
- `shortestPath()` and `allShortestPaths()`
- Multiple labels: `(n:Person:Employee)`
- Multiple relationship types: `-[:KNOWS|LIKES]->`

### Functions
- Aggregation: `count()`, `collect()`, `sum()`, `avg()`, `min()`, `max()`
- `count(*)`, `count(DISTINCT x)`
- Namespaced functions: `apoc.text.join()`
- Predicate functions: `ALL()`, `ANY()`, `NONE()`, `SINGLE()`

### Subqueries
- `CALL { ... }` inline subqueries
- `EXISTS { ... }` existence checks (pattern and full-query forms)
- `CALL procedure() YIELD ...` procedure calls

### Other
- Backtick-escaped identifiers: `` `My Label` ``
- Block comments: `/* ... */`
- Line comments: `// ...`
- Case-insensitive keywords

## Examples

### Basic Query
```python
from pycypher import parse

result = parse('MATCH (n:Person) RETURN n.name;')
assert result['errors'] == []
```

### Relationship Traversal
```python
result = parse('''
    MATCH (a:Person)-[:KNOWS]->(b:Person)-[:LIVES_IN]->(c:City)
    WHERE b.age > 25
    RETURN a.name, b.name, c.name
    ORDER BY b.age DESC
    LIMIT 10
''')
```

### Mutations
```python
result = parse('''
    MERGE (n:User {id: $userId})
    ON CREATE SET n.created = timestamp()
    ON MATCH SET n.lastSeen = timestamp()
    RETURN n
''')
```

### Subqueries
```python
result = parse('''
    MATCH (n:Person)
    WHERE EXISTS {
        MATCH (n)-[:KNOWS]->(m)
        WHERE m.age > 30
    }
    CALL { MATCH (x) RETURN x LIMIT 1 }
    RETURN n.name
''')
```

### Error Detection
```python
result = parse('THIS IS NOT VALID CYPHER')
if result['errors']:
    print(f"Parse errors found: {len(result['errors'])}")
```

## Grammar

The parser is built from ANTLR 4.13 grammar files located in `grammar/`:

- `CypherLexer.g4` - Token definitions (keywords, operators, literals)
- `CypherParser.g4` - Parser rules (statements, clauses, expressions, patterns)

Based on the [antlr/grammars-v4](https://github.com/antlr/grammars-v4/tree/master/cypher) Cypher grammar (BSD license) by Boris Zhguchev, with patches for:
- FOREACH clause
- CALL {} subqueries (Cypher 5)
- EXISTS { full-query } subqueries
- shortestPath / allShortestPaths
- Numeric token precedence fix

### Regenerating the Parser

If you modify the grammar:

```bash
# Download ANTLR
curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar

# Generate Python files
java -jar antlr-4.13.2-complete.jar \
    -Dlanguage=Python3 -visitor \
    grammar/CypherLexer.g4 grammar/CypherParser.g4

# Copy generated files into the package
cp CypherLexer.py pycypher/lexer.py
cp CypherParser.py pycypher/parser.py
cp CypherParserVisitor.py pycypher/visitor.py
cp CypherParserListener.py pycypher/listener.py
```

## Development

```bash
git clone https://github.com/Mizzlr/pycypher
cd pycypher
python -m venv .venv && source .venv/bin/activate
pip install antlr4-python3-runtime pytest
python -m pytest tests/ -v
```

## License

MIT License. See [LICENSE](LICENSE) for details.
