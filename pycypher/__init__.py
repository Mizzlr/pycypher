from antlr4 import InputStream, CommonTokenStream
from pycypher.lexer import CypherLexer
from pycypher.parser import CypherParser


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
        return {
            'parent': node.parentCtx.__class__.__name__.split('.')[-1][3:-7],
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
    input_stream = InputStream(query_string)
    lexer = CypherLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    tree = parser.oC_Cypher()
    visitor = ParseTreeVisitor()
    result = visitor.visit(tree)
    return result
