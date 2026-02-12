# Generated from CypherParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CypherParser import CypherParser
else:
    from CypherParser import CypherParser

# This class defines a complete listener for a parse tree produced by CypherParser.
class CypherParserListener(ParseTreeListener):

    # Enter a parse tree produced by CypherParser#script.
    def enterScript(self, ctx:CypherParser.ScriptContext):
        pass

    # Exit a parse tree produced by CypherParser#script.
    def exitScript(self, ctx:CypherParser.ScriptContext):
        pass


    # Enter a parse tree produced by CypherParser#query.
    def enterQuery(self, ctx:CypherParser.QueryContext):
        pass

    # Exit a parse tree produced by CypherParser#query.
    def exitQuery(self, ctx:CypherParser.QueryContext):
        pass


    # Enter a parse tree produced by CypherParser#regularQuery.
    def enterRegularQuery(self, ctx:CypherParser.RegularQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#regularQuery.
    def exitRegularQuery(self, ctx:CypherParser.RegularQueryContext):
        pass


    # Enter a parse tree produced by CypherParser#singleQuery.
    def enterSingleQuery(self, ctx:CypherParser.SingleQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#singleQuery.
    def exitSingleQuery(self, ctx:CypherParser.SingleQueryContext):
        pass


    # Enter a parse tree produced by CypherParser#standaloneCall.
    def enterStandaloneCall(self, ctx:CypherParser.StandaloneCallContext):
        pass

    # Exit a parse tree produced by CypherParser#standaloneCall.
    def exitStandaloneCall(self, ctx:CypherParser.StandaloneCallContext):
        pass


    # Enter a parse tree produced by CypherParser#returnSt.
    def enterReturnSt(self, ctx:CypherParser.ReturnStContext):
        pass

    # Exit a parse tree produced by CypherParser#returnSt.
    def exitReturnSt(self, ctx:CypherParser.ReturnStContext):
        pass


    # Enter a parse tree produced by CypherParser#withSt.
    def enterWithSt(self, ctx:CypherParser.WithStContext):
        pass

    # Exit a parse tree produced by CypherParser#withSt.
    def exitWithSt(self, ctx:CypherParser.WithStContext):
        pass


    # Enter a parse tree produced by CypherParser#skipSt.
    def enterSkipSt(self, ctx:CypherParser.SkipStContext):
        pass

    # Exit a parse tree produced by CypherParser#skipSt.
    def exitSkipSt(self, ctx:CypherParser.SkipStContext):
        pass


    # Enter a parse tree produced by CypherParser#limitSt.
    def enterLimitSt(self, ctx:CypherParser.LimitStContext):
        pass

    # Exit a parse tree produced by CypherParser#limitSt.
    def exitLimitSt(self, ctx:CypherParser.LimitStContext):
        pass


    # Enter a parse tree produced by CypherParser#projectionBody.
    def enterProjectionBody(self, ctx:CypherParser.ProjectionBodyContext):
        pass

    # Exit a parse tree produced by CypherParser#projectionBody.
    def exitProjectionBody(self, ctx:CypherParser.ProjectionBodyContext):
        pass


    # Enter a parse tree produced by CypherParser#projectionItems.
    def enterProjectionItems(self, ctx:CypherParser.ProjectionItemsContext):
        pass

    # Exit a parse tree produced by CypherParser#projectionItems.
    def exitProjectionItems(self, ctx:CypherParser.ProjectionItemsContext):
        pass


    # Enter a parse tree produced by CypherParser#projectionItem.
    def enterProjectionItem(self, ctx:CypherParser.ProjectionItemContext):
        pass

    # Exit a parse tree produced by CypherParser#projectionItem.
    def exitProjectionItem(self, ctx:CypherParser.ProjectionItemContext):
        pass


    # Enter a parse tree produced by CypherParser#orderItem.
    def enterOrderItem(self, ctx:CypherParser.OrderItemContext):
        pass

    # Exit a parse tree produced by CypherParser#orderItem.
    def exitOrderItem(self, ctx:CypherParser.OrderItemContext):
        pass


    # Enter a parse tree produced by CypherParser#orderSt.
    def enterOrderSt(self, ctx:CypherParser.OrderStContext):
        pass

    # Exit a parse tree produced by CypherParser#orderSt.
    def exitOrderSt(self, ctx:CypherParser.OrderStContext):
        pass


    # Enter a parse tree produced by CypherParser#singlePartQ.
    def enterSinglePartQ(self, ctx:CypherParser.SinglePartQContext):
        pass

    # Exit a parse tree produced by CypherParser#singlePartQ.
    def exitSinglePartQ(self, ctx:CypherParser.SinglePartQContext):
        pass


    # Enter a parse tree produced by CypherParser#multiPartQ.
    def enterMultiPartQ(self, ctx:CypherParser.MultiPartQContext):
        pass

    # Exit a parse tree produced by CypherParser#multiPartQ.
    def exitMultiPartQ(self, ctx:CypherParser.MultiPartQContext):
        pass


    # Enter a parse tree produced by CypherParser#matchSt.
    def enterMatchSt(self, ctx:CypherParser.MatchStContext):
        pass

    # Exit a parse tree produced by CypherParser#matchSt.
    def exitMatchSt(self, ctx:CypherParser.MatchStContext):
        pass


    # Enter a parse tree produced by CypherParser#unwindSt.
    def enterUnwindSt(self, ctx:CypherParser.UnwindStContext):
        pass

    # Exit a parse tree produced by CypherParser#unwindSt.
    def exitUnwindSt(self, ctx:CypherParser.UnwindStContext):
        pass


    # Enter a parse tree produced by CypherParser#readingStatement.
    def enterReadingStatement(self, ctx:CypherParser.ReadingStatementContext):
        pass

    # Exit a parse tree produced by CypherParser#readingStatement.
    def exitReadingStatement(self, ctx:CypherParser.ReadingStatementContext):
        pass


    # Enter a parse tree produced by CypherParser#updatingStatement.
    def enterUpdatingStatement(self, ctx:CypherParser.UpdatingStatementContext):
        pass

    # Exit a parse tree produced by CypherParser#updatingStatement.
    def exitUpdatingStatement(self, ctx:CypherParser.UpdatingStatementContext):
        pass


    # Enter a parse tree produced by CypherParser#deleteSt.
    def enterDeleteSt(self, ctx:CypherParser.DeleteStContext):
        pass

    # Exit a parse tree produced by CypherParser#deleteSt.
    def exitDeleteSt(self, ctx:CypherParser.DeleteStContext):
        pass


    # Enter a parse tree produced by CypherParser#removeSt.
    def enterRemoveSt(self, ctx:CypherParser.RemoveStContext):
        pass

    # Exit a parse tree produced by CypherParser#removeSt.
    def exitRemoveSt(self, ctx:CypherParser.RemoveStContext):
        pass


    # Enter a parse tree produced by CypherParser#removeItem.
    def enterRemoveItem(self, ctx:CypherParser.RemoveItemContext):
        pass

    # Exit a parse tree produced by CypherParser#removeItem.
    def exitRemoveItem(self, ctx:CypherParser.RemoveItemContext):
        pass


    # Enter a parse tree produced by CypherParser#queryCallSt.
    def enterQueryCallSt(self, ctx:CypherParser.QueryCallStContext):
        pass

    # Exit a parse tree produced by CypherParser#queryCallSt.
    def exitQueryCallSt(self, ctx:CypherParser.QueryCallStContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryCall.
    def enterSubqueryCall(self, ctx:CypherParser.SubqueryCallContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryCall.
    def exitSubqueryCall(self, ctx:CypherParser.SubqueryCallContext):
        pass


    # Enter a parse tree produced by CypherParser#parenExpressionChain.
    def enterParenExpressionChain(self, ctx:CypherParser.ParenExpressionChainContext):
        pass

    # Exit a parse tree produced by CypherParser#parenExpressionChain.
    def exitParenExpressionChain(self, ctx:CypherParser.ParenExpressionChainContext):
        pass


    # Enter a parse tree produced by CypherParser#yieldItems.
    def enterYieldItems(self, ctx:CypherParser.YieldItemsContext):
        pass

    # Exit a parse tree produced by CypherParser#yieldItems.
    def exitYieldItems(self, ctx:CypherParser.YieldItemsContext):
        pass


    # Enter a parse tree produced by CypherParser#yieldItem.
    def enterYieldItem(self, ctx:CypherParser.YieldItemContext):
        pass

    # Exit a parse tree produced by CypherParser#yieldItem.
    def exitYieldItem(self, ctx:CypherParser.YieldItemContext):
        pass


    # Enter a parse tree produced by CypherParser#mergeSt.
    def enterMergeSt(self, ctx:CypherParser.MergeStContext):
        pass

    # Exit a parse tree produced by CypherParser#mergeSt.
    def exitMergeSt(self, ctx:CypherParser.MergeStContext):
        pass


    # Enter a parse tree produced by CypherParser#mergeAction.
    def enterMergeAction(self, ctx:CypherParser.MergeActionContext):
        pass

    # Exit a parse tree produced by CypherParser#mergeAction.
    def exitMergeAction(self, ctx:CypherParser.MergeActionContext):
        pass


    # Enter a parse tree produced by CypherParser#setSt.
    def enterSetSt(self, ctx:CypherParser.SetStContext):
        pass

    # Exit a parse tree produced by CypherParser#setSt.
    def exitSetSt(self, ctx:CypherParser.SetStContext):
        pass


    # Enter a parse tree produced by CypherParser#setItem.
    def enterSetItem(self, ctx:CypherParser.SetItemContext):
        pass

    # Exit a parse tree produced by CypherParser#setItem.
    def exitSetItem(self, ctx:CypherParser.SetItemContext):
        pass


    # Enter a parse tree produced by CypherParser#nodeLabels.
    def enterNodeLabels(self, ctx:CypherParser.NodeLabelsContext):
        pass

    # Exit a parse tree produced by CypherParser#nodeLabels.
    def exitNodeLabels(self, ctx:CypherParser.NodeLabelsContext):
        pass


    # Enter a parse tree produced by CypherParser#createSt.
    def enterCreateSt(self, ctx:CypherParser.CreateStContext):
        pass

    # Exit a parse tree produced by CypherParser#createSt.
    def exitCreateSt(self, ctx:CypherParser.CreateStContext):
        pass


    # Enter a parse tree produced by CypherParser#foreachSt.
    def enterForeachSt(self, ctx:CypherParser.ForeachStContext):
        pass

    # Exit a parse tree produced by CypherParser#foreachSt.
    def exitForeachSt(self, ctx:CypherParser.ForeachStContext):
        pass


    # Enter a parse tree produced by CypherParser#patternWhere.
    def enterPatternWhere(self, ctx:CypherParser.PatternWhereContext):
        pass

    # Exit a parse tree produced by CypherParser#patternWhere.
    def exitPatternWhere(self, ctx:CypherParser.PatternWhereContext):
        pass


    # Enter a parse tree produced by CypherParser#where.
    def enterWhere(self, ctx:CypherParser.WhereContext):
        pass

    # Exit a parse tree produced by CypherParser#where.
    def exitWhere(self, ctx:CypherParser.WhereContext):
        pass


    # Enter a parse tree produced by CypherParser#pattern.
    def enterPattern(self, ctx:CypherParser.PatternContext):
        pass

    # Exit a parse tree produced by CypherParser#pattern.
    def exitPattern(self, ctx:CypherParser.PatternContext):
        pass


    # Enter a parse tree produced by CypherParser#expression.
    def enterExpression(self, ctx:CypherParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#expression.
    def exitExpression(self, ctx:CypherParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#xorExpression.
    def enterXorExpression(self, ctx:CypherParser.XorExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#xorExpression.
    def exitXorExpression(self, ctx:CypherParser.XorExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#andExpression.
    def enterAndExpression(self, ctx:CypherParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#andExpression.
    def exitAndExpression(self, ctx:CypherParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#notExpression.
    def enterNotExpression(self, ctx:CypherParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#notExpression.
    def exitNotExpression(self, ctx:CypherParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:CypherParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:CypherParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#comparisonSigns.
    def enterComparisonSigns(self, ctx:CypherParser.ComparisonSignsContext):
        pass

    # Exit a parse tree produced by CypherParser#comparisonSigns.
    def exitComparisonSigns(self, ctx:CypherParser.ComparisonSignsContext):
        pass


    # Enter a parse tree produced by CypherParser#addSubExpression.
    def enterAddSubExpression(self, ctx:CypherParser.AddSubExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#addSubExpression.
    def exitAddSubExpression(self, ctx:CypherParser.AddSubExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#multDivExpression.
    def enterMultDivExpression(self, ctx:CypherParser.MultDivExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#multDivExpression.
    def exitMultDivExpression(self, ctx:CypherParser.MultDivExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#powerExpression.
    def enterPowerExpression(self, ctx:CypherParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#powerExpression.
    def exitPowerExpression(self, ctx:CypherParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#unaryAddSubExpression.
    def enterUnaryAddSubExpression(self, ctx:CypherParser.UnaryAddSubExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#unaryAddSubExpression.
    def exitUnaryAddSubExpression(self, ctx:CypherParser.UnaryAddSubExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#atomicExpression.
    def enterAtomicExpression(self, ctx:CypherParser.AtomicExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#atomicExpression.
    def exitAtomicExpression(self, ctx:CypherParser.AtomicExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#listExpression.
    def enterListExpression(self, ctx:CypherParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#listExpression.
    def exitListExpression(self, ctx:CypherParser.ListExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#stringExpression.
    def enterStringExpression(self, ctx:CypherParser.StringExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#stringExpression.
    def exitStringExpression(self, ctx:CypherParser.StringExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#stringExpPrefix.
    def enterStringExpPrefix(self, ctx:CypherParser.StringExpPrefixContext):
        pass

    # Exit a parse tree produced by CypherParser#stringExpPrefix.
    def exitStringExpPrefix(self, ctx:CypherParser.StringExpPrefixContext):
        pass


    # Enter a parse tree produced by CypherParser#nullExpression.
    def enterNullExpression(self, ctx:CypherParser.NullExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#nullExpression.
    def exitNullExpression(self, ctx:CypherParser.NullExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#propertyOrLabelExpression.
    def enterPropertyOrLabelExpression(self, ctx:CypherParser.PropertyOrLabelExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#propertyOrLabelExpression.
    def exitPropertyOrLabelExpression(self, ctx:CypherParser.PropertyOrLabelExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#propertyExpression.
    def enterPropertyExpression(self, ctx:CypherParser.PropertyExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#propertyExpression.
    def exitPropertyExpression(self, ctx:CypherParser.PropertyExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#patternPart.
    def enterPatternPart(self, ctx:CypherParser.PatternPartContext):
        pass

    # Exit a parse tree produced by CypherParser#patternPart.
    def exitPatternPart(self, ctx:CypherParser.PatternPartContext):
        pass


    # Enter a parse tree produced by CypherParser#patternElem.
    def enterPatternElem(self, ctx:CypherParser.PatternElemContext):
        pass

    # Exit a parse tree produced by CypherParser#patternElem.
    def exitPatternElem(self, ctx:CypherParser.PatternElemContext):
        pass


    # Enter a parse tree produced by CypherParser#shortestPathPattern.
    def enterShortestPathPattern(self, ctx:CypherParser.ShortestPathPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#shortestPathPattern.
    def exitShortestPathPattern(self, ctx:CypherParser.ShortestPathPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#patternElemChain.
    def enterPatternElemChain(self, ctx:CypherParser.PatternElemChainContext):
        pass

    # Exit a parse tree produced by CypherParser#patternElemChain.
    def exitPatternElemChain(self, ctx:CypherParser.PatternElemChainContext):
        pass


    # Enter a parse tree produced by CypherParser#properties.
    def enterProperties(self, ctx:CypherParser.PropertiesContext):
        pass

    # Exit a parse tree produced by CypherParser#properties.
    def exitProperties(self, ctx:CypherParser.PropertiesContext):
        pass


    # Enter a parse tree produced by CypherParser#nodePattern.
    def enterNodePattern(self, ctx:CypherParser.NodePatternContext):
        pass

    # Exit a parse tree produced by CypherParser#nodePattern.
    def exitNodePattern(self, ctx:CypherParser.NodePatternContext):
        pass


    # Enter a parse tree produced by CypherParser#atom.
    def enterAtom(self, ctx:CypherParser.AtomContext):
        pass

    # Exit a parse tree produced by CypherParser#atom.
    def exitAtom(self, ctx:CypherParser.AtomContext):
        pass


    # Enter a parse tree produced by CypherParser#lhs.
    def enterLhs(self, ctx:CypherParser.LhsContext):
        pass

    # Exit a parse tree produced by CypherParser#lhs.
    def exitLhs(self, ctx:CypherParser.LhsContext):
        pass


    # Enter a parse tree produced by CypherParser#relationshipPattern.
    def enterRelationshipPattern(self, ctx:CypherParser.RelationshipPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#relationshipPattern.
    def exitRelationshipPattern(self, ctx:CypherParser.RelationshipPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#relationDetail.
    def enterRelationDetail(self, ctx:CypherParser.RelationDetailContext):
        pass

    # Exit a parse tree produced by CypherParser#relationDetail.
    def exitRelationDetail(self, ctx:CypherParser.RelationDetailContext):
        pass


    # Enter a parse tree produced by CypherParser#relationshipTypes.
    def enterRelationshipTypes(self, ctx:CypherParser.RelationshipTypesContext):
        pass

    # Exit a parse tree produced by CypherParser#relationshipTypes.
    def exitRelationshipTypes(self, ctx:CypherParser.RelationshipTypesContext):
        pass


    # Enter a parse tree produced by CypherParser#unionSt.
    def enterUnionSt(self, ctx:CypherParser.UnionStContext):
        pass

    # Exit a parse tree produced by CypherParser#unionSt.
    def exitUnionSt(self, ctx:CypherParser.UnionStContext):
        pass


    # Enter a parse tree produced by CypherParser#subqueryExist.
    def enterSubqueryExist(self, ctx:CypherParser.SubqueryExistContext):
        pass

    # Exit a parse tree produced by CypherParser#subqueryExist.
    def exitSubqueryExist(self, ctx:CypherParser.SubqueryExistContext):
        pass


    # Enter a parse tree produced by CypherParser#invocationName.
    def enterInvocationName(self, ctx:CypherParser.InvocationNameContext):
        pass

    # Exit a parse tree produced by CypherParser#invocationName.
    def exitInvocationName(self, ctx:CypherParser.InvocationNameContext):
        pass


    # Enter a parse tree produced by CypherParser#functionInvocation.
    def enterFunctionInvocation(self, ctx:CypherParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by CypherParser#functionInvocation.
    def exitFunctionInvocation(self, ctx:CypherParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by CypherParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:CypherParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:CypherParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#filterWith.
    def enterFilterWith(self, ctx:CypherParser.FilterWithContext):
        pass

    # Exit a parse tree produced by CypherParser#filterWith.
    def exitFilterWith(self, ctx:CypherParser.FilterWithContext):
        pass


    # Enter a parse tree produced by CypherParser#patternComprehension.
    def enterPatternComprehension(self, ctx:CypherParser.PatternComprehensionContext):
        pass

    # Exit a parse tree produced by CypherParser#patternComprehension.
    def exitPatternComprehension(self, ctx:CypherParser.PatternComprehensionContext):
        pass


    # Enter a parse tree produced by CypherParser#relationshipsChainPattern.
    def enterRelationshipsChainPattern(self, ctx:CypherParser.RelationshipsChainPatternContext):
        pass

    # Exit a parse tree produced by CypherParser#relationshipsChainPattern.
    def exitRelationshipsChainPattern(self, ctx:CypherParser.RelationshipsChainPatternContext):
        pass


    # Enter a parse tree produced by CypherParser#listComprehension.
    def enterListComprehension(self, ctx:CypherParser.ListComprehensionContext):
        pass

    # Exit a parse tree produced by CypherParser#listComprehension.
    def exitListComprehension(self, ctx:CypherParser.ListComprehensionContext):
        pass


    # Enter a parse tree produced by CypherParser#filterExpression.
    def enterFilterExpression(self, ctx:CypherParser.FilterExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#filterExpression.
    def exitFilterExpression(self, ctx:CypherParser.FilterExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#countAll.
    def enterCountAll(self, ctx:CypherParser.CountAllContext):
        pass

    # Exit a parse tree produced by CypherParser#countAll.
    def exitCountAll(self, ctx:CypherParser.CountAllContext):
        pass


    # Enter a parse tree produced by CypherParser#expressionChain.
    def enterExpressionChain(self, ctx:CypherParser.ExpressionChainContext):
        pass

    # Exit a parse tree produced by CypherParser#expressionChain.
    def exitExpressionChain(self, ctx:CypherParser.ExpressionChainContext):
        pass


    # Enter a parse tree produced by CypherParser#caseExpression.
    def enterCaseExpression(self, ctx:CypherParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#caseExpression.
    def exitCaseExpression(self, ctx:CypherParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by CypherParser#parameter.
    def enterParameter(self, ctx:CypherParser.ParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#parameter.
    def exitParameter(self, ctx:CypherParser.ParameterContext):
        pass


    # Enter a parse tree produced by CypherParser#literal.
    def enterLiteral(self, ctx:CypherParser.LiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#literal.
    def exitLiteral(self, ctx:CypherParser.LiteralContext):
        pass


    # Enter a parse tree produced by CypherParser#rangeLit.
    def enterRangeLit(self, ctx:CypherParser.RangeLitContext):
        pass

    # Exit a parse tree produced by CypherParser#rangeLit.
    def exitRangeLit(self, ctx:CypherParser.RangeLitContext):
        pass


    # Enter a parse tree produced by CypherParser#boolLit.
    def enterBoolLit(self, ctx:CypherParser.BoolLitContext):
        pass

    # Exit a parse tree produced by CypherParser#boolLit.
    def exitBoolLit(self, ctx:CypherParser.BoolLitContext):
        pass


    # Enter a parse tree produced by CypherParser#numLit.
    def enterNumLit(self, ctx:CypherParser.NumLitContext):
        pass

    # Exit a parse tree produced by CypherParser#numLit.
    def exitNumLit(self, ctx:CypherParser.NumLitContext):
        pass


    # Enter a parse tree produced by CypherParser#stringLit.
    def enterStringLit(self, ctx:CypherParser.StringLitContext):
        pass

    # Exit a parse tree produced by CypherParser#stringLit.
    def exitStringLit(self, ctx:CypherParser.StringLitContext):
        pass


    # Enter a parse tree produced by CypherParser#charLit.
    def enterCharLit(self, ctx:CypherParser.CharLitContext):
        pass

    # Exit a parse tree produced by CypherParser#charLit.
    def exitCharLit(self, ctx:CypherParser.CharLitContext):
        pass


    # Enter a parse tree produced by CypherParser#listLit.
    def enterListLit(self, ctx:CypherParser.ListLitContext):
        pass

    # Exit a parse tree produced by CypherParser#listLit.
    def exitListLit(self, ctx:CypherParser.ListLitContext):
        pass


    # Enter a parse tree produced by CypherParser#mapLit.
    def enterMapLit(self, ctx:CypherParser.MapLitContext):
        pass

    # Exit a parse tree produced by CypherParser#mapLit.
    def exitMapLit(self, ctx:CypherParser.MapLitContext):
        pass


    # Enter a parse tree produced by CypherParser#mapPair.
    def enterMapPair(self, ctx:CypherParser.MapPairContext):
        pass

    # Exit a parse tree produced by CypherParser#mapPair.
    def exitMapPair(self, ctx:CypherParser.MapPairContext):
        pass


    # Enter a parse tree produced by CypherParser#name.
    def enterName(self, ctx:CypherParser.NameContext):
        pass

    # Exit a parse tree produced by CypherParser#name.
    def exitName(self, ctx:CypherParser.NameContext):
        pass


    # Enter a parse tree produced by CypherParser#symbol.
    def enterSymbol(self, ctx:CypherParser.SymbolContext):
        pass

    # Exit a parse tree produced by CypherParser#symbol.
    def exitSymbol(self, ctx:CypherParser.SymbolContext):
        pass


    # Enter a parse tree produced by CypherParser#reservedWord.
    def enterReservedWord(self, ctx:CypherParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by CypherParser#reservedWord.
    def exitReservedWord(self, ctx:CypherParser.ReservedWordContext):
        pass



del CypherParser