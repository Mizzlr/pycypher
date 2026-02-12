"""pycypher - A Python parser for the Cypher graph query language.

Parse Cypher query strings into Abstract Syntax Trees (ASTs).

Usage:
    >>> from pycypher import parse
    >>> result = parse('MATCH (n:Person) RETURN n.name;')
    >>> result['errors']
    []
"""

__version__ = "1.0.0"

from antlr4 import InputStream, CommonTokenStream
from pycypher.lexer import CypherLexer
from pycypher.parser import CypherParser


def _get_node_name(ctx):
    """Extract a clean rule name from an ANTLR context class."""
    name = ctx.__class__.__name__
    if name.endswith('Context'):
        name = name[:-7]
    return name


class ParseTreeVisitor(object):
    def __init__(self):
        self.errors = []

    def visit(self, tree):
        return tree.accept(self)

    def visitChildren(self, node):
        self.errors.append([])
        result = self.defaultResult()
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            childResult = child.accept(self)
            result = self.aggregateResult(result, child, childResult)
        errors = self.errors.pop()
        return {
            'result': result,
            'errors': errors,
        }

    def visitTerminal(self, node):
        parent_name = _get_node_name(node.parentCtx) if node.parentCtx else 'Root'
        return {
            'parent': parent_name,
            'text': node.getText(),
            'sourceInterval': node.getSourceInterval(),
        }

    def visitErrorNode(self, node):
        self.errors[-1].append(self.visitTerminal(node))
        return self.defaultResult()

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, child, nextResult):
        aggregate.append({
            'node': self.visitTerminal(child),
            'children': nextResult,
        })
        return aggregate


def parse(query_string):
    """Parse a Cypher query string and return an AST.

    Args:
        query_string: A Cypher query string (e.g. "MATCH (n) RETURN n;")

    Returns:
        A dict with 'result' (list of AST nodes) and 'errors' (list of parse errors).
        Each AST node has 'node' (with 'parent', 'text', 'sourceInterval') and 'children'.
    """
    input_stream = InputStream(query_string)
    lexer = CypherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    tree = parser.script()
    visitor = ParseTreeVisitor()
    result = visitor.visit(tree)
    return result
