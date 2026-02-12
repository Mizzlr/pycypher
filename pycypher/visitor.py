# Generated from CypherParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CypherParser import CypherParser
else:
    from CypherParser import CypherParser

# This class defines a complete generic visitor for a parse tree produced by CypherParser.

class CypherParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CypherParser#script.
    def visitScript(self, ctx:CypherParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#query.
    def visitQuery(self, ctx:CypherParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#regularQuery.
    def visitRegularQuery(self, ctx:CypherParser.RegularQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singleQuery.
    def visitSingleQuery(self, ctx:CypherParser.SingleQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#standaloneCall.
    def visitStandaloneCall(self, ctx:CypherParser.StandaloneCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#returnSt.
    def visitReturnSt(self, ctx:CypherParser.ReturnStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#withSt.
    def visitWithSt(self, ctx:CypherParser.WithStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#skipSt.
    def visitSkipSt(self, ctx:CypherParser.SkipStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#limitSt.
    def visitLimitSt(self, ctx:CypherParser.LimitStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#projectionBody.
    def visitProjectionBody(self, ctx:CypherParser.ProjectionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#projectionItems.
    def visitProjectionItems(self, ctx:CypherParser.ProjectionItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#projectionItem.
    def visitProjectionItem(self, ctx:CypherParser.ProjectionItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#orderItem.
    def visitOrderItem(self, ctx:CypherParser.OrderItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#orderSt.
    def visitOrderSt(self, ctx:CypherParser.OrderStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#singlePartQ.
    def visitSinglePartQ(self, ctx:CypherParser.SinglePartQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#multiPartQ.
    def visitMultiPartQ(self, ctx:CypherParser.MultiPartQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#matchSt.
    def visitMatchSt(self, ctx:CypherParser.MatchStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#unwindSt.
    def visitUnwindSt(self, ctx:CypherParser.UnwindStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#readingStatement.
    def visitReadingStatement(self, ctx:CypherParser.ReadingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#updatingStatement.
    def visitUpdatingStatement(self, ctx:CypherParser.UpdatingStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#deleteSt.
    def visitDeleteSt(self, ctx:CypherParser.DeleteStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#removeSt.
    def visitRemoveSt(self, ctx:CypherParser.RemoveStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#removeItem.
    def visitRemoveItem(self, ctx:CypherParser.RemoveItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#queryCallSt.
    def visitQueryCallSt(self, ctx:CypherParser.QueryCallStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryCall.
    def visitSubqueryCall(self, ctx:CypherParser.SubqueryCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#parenExpressionChain.
    def visitParenExpressionChain(self, ctx:CypherParser.ParenExpressionChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#yieldItems.
    def visitYieldItems(self, ctx:CypherParser.YieldItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#yieldItem.
    def visitYieldItem(self, ctx:CypherParser.YieldItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mergeSt.
    def visitMergeSt(self, ctx:CypherParser.MergeStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mergeAction.
    def visitMergeAction(self, ctx:CypherParser.MergeActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#setSt.
    def visitSetSt(self, ctx:CypherParser.SetStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#setItem.
    def visitSetItem(self, ctx:CypherParser.SetItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#nodeLabels.
    def visitNodeLabels(self, ctx:CypherParser.NodeLabelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#createSt.
    def visitCreateSt(self, ctx:CypherParser.CreateStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#foreachSt.
    def visitForeachSt(self, ctx:CypherParser.ForeachStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternWhere.
    def visitPatternWhere(self, ctx:CypherParser.PatternWhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#where.
    def visitWhere(self, ctx:CypherParser.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#pattern.
    def visitPattern(self, ctx:CypherParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expression.
    def visitExpression(self, ctx:CypherParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#xorExpression.
    def visitXorExpression(self, ctx:CypherParser.XorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#andExpression.
    def visitAndExpression(self, ctx:CypherParser.AndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#notExpression.
    def visitNotExpression(self, ctx:CypherParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:CypherParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#comparisonSigns.
    def visitComparisonSigns(self, ctx:CypherParser.ComparisonSignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#addSubExpression.
    def visitAddSubExpression(self, ctx:CypherParser.AddSubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#multDivExpression.
    def visitMultDivExpression(self, ctx:CypherParser.MultDivExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#powerExpression.
    def visitPowerExpression(self, ctx:CypherParser.PowerExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#unaryAddSubExpression.
    def visitUnaryAddSubExpression(self, ctx:CypherParser.UnaryAddSubExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#atomicExpression.
    def visitAtomicExpression(self, ctx:CypherParser.AtomicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#listExpression.
    def visitListExpression(self, ctx:CypherParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringExpression.
    def visitStringExpression(self, ctx:CypherParser.StringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringExpPrefix.
    def visitStringExpPrefix(self, ctx:CypherParser.StringExpPrefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#nullExpression.
    def visitNullExpression(self, ctx:CypherParser.NullExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#propertyOrLabelExpression.
    def visitPropertyOrLabelExpression(self, ctx:CypherParser.PropertyOrLabelExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#propertyExpression.
    def visitPropertyExpression(self, ctx:CypherParser.PropertyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternPart.
    def visitPatternPart(self, ctx:CypherParser.PatternPartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternElem.
    def visitPatternElem(self, ctx:CypherParser.PatternElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#shortestPathPattern.
    def visitShortestPathPattern(self, ctx:CypherParser.ShortestPathPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternElemChain.
    def visitPatternElemChain(self, ctx:CypherParser.PatternElemChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#properties.
    def visitProperties(self, ctx:CypherParser.PropertiesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#nodePattern.
    def visitNodePattern(self, ctx:CypherParser.NodePatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#atom.
    def visitAtom(self, ctx:CypherParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#lhs.
    def visitLhs(self, ctx:CypherParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#relationshipPattern.
    def visitRelationshipPattern(self, ctx:CypherParser.RelationshipPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#relationDetail.
    def visitRelationDetail(self, ctx:CypherParser.RelationDetailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#relationshipTypes.
    def visitRelationshipTypes(self, ctx:CypherParser.RelationshipTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#unionSt.
    def visitUnionSt(self, ctx:CypherParser.UnionStContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#subqueryExist.
    def visitSubqueryExist(self, ctx:CypherParser.SubqueryExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#invocationName.
    def visitInvocationName(self, ctx:CypherParser.InvocationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#functionInvocation.
    def visitFunctionInvocation(self, ctx:CypherParser.FunctionInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:CypherParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#filterWith.
    def visitFilterWith(self, ctx:CypherParser.FilterWithContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#patternComprehension.
    def visitPatternComprehension(self, ctx:CypherParser.PatternComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#relationshipsChainPattern.
    def visitRelationshipsChainPattern(self, ctx:CypherParser.RelationshipsChainPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#listComprehension.
    def visitListComprehension(self, ctx:CypherParser.ListComprehensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#filterExpression.
    def visitFilterExpression(self, ctx:CypherParser.FilterExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#countAll.
    def visitCountAll(self, ctx:CypherParser.CountAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#expressionChain.
    def visitExpressionChain(self, ctx:CypherParser.ExpressionChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#caseExpression.
    def visitCaseExpression(self, ctx:CypherParser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#parameter.
    def visitParameter(self, ctx:CypherParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#literal.
    def visitLiteral(self, ctx:CypherParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#rangeLit.
    def visitRangeLit(self, ctx:CypherParser.RangeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#boolLit.
    def visitBoolLit(self, ctx:CypherParser.BoolLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#numLit.
    def visitNumLit(self, ctx:CypherParser.NumLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#stringLit.
    def visitStringLit(self, ctx:CypherParser.StringLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#charLit.
    def visitCharLit(self, ctx:CypherParser.CharLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#listLit.
    def visitListLit(self, ctx:CypherParser.ListLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mapLit.
    def visitMapLit(self, ctx:CypherParser.MapLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#mapPair.
    def visitMapPair(self, ctx:CypherParser.MapPairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#name.
    def visitName(self, ctx:CypherParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#symbol.
    def visitSymbol(self, ctx:CypherParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CypherParser#reservedWord.
    def visitReservedWord(self, ctx:CypherParser.ReservedWordContext):
        return self.visitChildren(ctx)



del CypherParser