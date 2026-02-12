"""Comprehensive tests for pycypher parser."""

import pytest
from pycypher import parse, __version__


def count_errors(obj):
    """Recursively count all errors in the AST."""
    total = 0
    if isinstance(obj, dict):
        total += len(obj.get('errors', []))
        for v in obj.values():
            total += count_errors(v)
    elif isinstance(obj, list):
        for item in obj:
            total += count_errors(item)
    return total


def assert_parses_clean(query):
    """Assert that a query parses with zero errors at any depth."""
    result = parse(query)
    errors = count_errors(result)
    assert errors == 0, f"Expected 0 errors, got {errors} for: {query}"
    # Ensure we got actual AST content
    top_nodes = [r for r in result.get('result', []) if r.get('node', {}).get('text', '')]
    assert len(top_nodes) > 0, f"Empty AST for: {query}"
    return result


class TestVersion:
    def test_version_exists(self):
        assert __version__ is not None
        assert isinstance(__version__, str)

    def test_version_format(self):
        parts = __version__.split('.')
        assert len(parts) == 3
        assert all(p.isdigit() for p in parts)


class TestBasicQueries:
    def test_match_return(self):
        assert_parses_clean('MATCH (n) RETURN n;')

    def test_match_return_no_semicolon(self):
        assert_parses_clean('MATCH (n) RETURN n')

    def test_match_with_label(self):
        assert_parses_clean('MATCH (n:Person) RETURN n;')

    def test_match_with_property(self):
        assert_parses_clean('MATCH (n {name: "Alice"}) RETURN n;')

    def test_match_with_label_and_property(self):
        assert_parses_clean('MATCH (n:Person {name: "Alice"}) RETURN n;')

    def test_return_literal(self):
        assert_parses_clean('RETURN 42;')

    def test_return_string(self):
        assert_parses_clean('RETURN "hello";')

    def test_return_boolean_true(self):
        assert_parses_clean('RETURN true;')

    def test_return_boolean_false(self):
        assert_parses_clean('RETURN false;')

    def test_return_null(self):
        assert_parses_clean('RETURN null;')

    def test_return_map(self):
        assert_parses_clean('RETURN {name: "Alice", age: 30};')

    def test_return_list(self):
        assert_parses_clean('RETURN [1, 2, 3];')


class TestRelationships:
    def test_outgoing(self):
        assert_parses_clean('MATCH (a)-[:KNOWS]->(b) RETURN a, b;')

    def test_incoming(self):
        assert_parses_clean('MATCH (a)<-[:KNOWS]-(b) RETURN a, b;')

    def test_undirected(self):
        assert_parses_clean('MATCH (a)-[:KNOWS]-(b) RETURN a, b;')

    def test_with_labels(self):
        assert_parses_clean('MATCH (a:Person)-[:KNOWS]->(b:Person) RETURN a.name, b.name;')

    def test_chain(self):
        assert_parses_clean('MATCH (a)-[:KNOWS]->(b)-[:LIVES_IN]->(c) RETURN a, b, c;')

    def test_with_variable(self):
        assert_parses_clean('MATCH (a)-[r:KNOWS]->(b) RETURN type(r);')

    def test_multiple_types(self):
        assert_parses_clean('MATCH (a)-[r:KNOWS|LIKES]->(b) RETURN r;')


class TestVariableLengthPaths:
    def test_fixed_length(self):
        assert_parses_clean('MATCH (a)-[*2]->(b) RETURN a, b;')

    def test_range(self):
        assert_parses_clean('MATCH p = (a)-[*1..3]->(b) RETURN p;')

    def test_min_only(self):
        assert_parses_clean('MATCH (a)-[*2..]->(b) RETURN a, b;')

    def test_max_only(self):
        assert_parses_clean('MATCH (a)-[*..5]->(b) RETURN a, b;')

    def test_unbounded(self):
        assert_parses_clean('MATCH (a)-[*]->(b) RETURN a, b;')

    def test_shortest_path(self):
        assert_parses_clean('MATCH p = shortestPath((a)-[*..5]->(b)) RETURN p;')

    def test_all_shortest_paths(self):
        assert_parses_clean('MATCH p = allShortestPaths((a)-[*]->(b)) RETURN p;')


class TestClauses:
    def test_where(self):
        assert_parses_clean('MATCH (n) WHERE n.age > 25 RETURN n;')

    def test_order_by(self):
        assert_parses_clean('MATCH (n) RETURN n ORDER BY n.name;')

    def test_order_by_desc(self):
        assert_parses_clean('MATCH (n) RETURN n ORDER BY n.age DESC;')

    def test_limit(self):
        assert_parses_clean('MATCH (n) RETURN n LIMIT 10;')

    def test_skip(self):
        assert_parses_clean('MATCH (n) RETURN n SKIP 5;')

    def test_skip_and_limit(self):
        assert_parses_clean('MATCH (n) RETURN n SKIP 5 LIMIT 10;')

    def test_distinct(self):
        assert_parses_clean('MATCH (n) RETURN DISTINCT n.name;')

    def test_optional_match(self):
        assert_parses_clean(
            'MATCH (a:Person) OPTIONAL MATCH (a)-[:LIVES_IN]->(c:City) RETURN a.name, c.name;'
        )

    def test_with(self):
        assert_parses_clean('MATCH (n) WITH n, count(*) AS cnt WHERE cnt > 1 RETURN n;')

    def test_unwind(self):
        assert_parses_clean('UNWIND [1, 2, 3] AS x RETURN x;')

    def test_union(self):
        assert_parses_clean('MATCH (n:Cat) RETURN n.name UNION MATCH (n:Dog) RETURN n.name;')

    def test_union_all(self):
        assert_parses_clean('MATCH (n:Cat) RETURN n.name UNION ALL MATCH (n:Dog) RETURN n.name;')


class TestMutations:
    def test_create(self):
        assert_parses_clean('CREATE (n:Person {name: "Alice", age: 30}) RETURN n;')

    def test_create_empty(self):
        assert_parses_clean('CREATE ();')

    def test_create_relationship(self):
        assert_parses_clean('MATCH (a:Person), (b:Person) CREATE (a)-[:KNOWS]->(b);')

    def test_merge(self):
        assert_parses_clean('MERGE (n:User {id: 42}) RETURN n;')

    def test_merge_on_create(self):
        assert_parses_clean(
            'MERGE (n:User {id: 42}) ON CREATE SET n.created = timestamp() RETURN n;'
        )

    def test_merge_on_match(self):
        assert_parses_clean(
            'MERGE (n:User {id: 1}) ON MATCH SET n.lastSeen = timestamp() RETURN n;'
        )

    def test_set(self):
        assert_parses_clean('MATCH (n {name: "Bob"}) SET n.age = 31 RETURN n;')

    def test_set_add_label(self):
        assert_parses_clean('MATCH (n {name: "Bob"}) SET n:Employee RETURN n;')

    def test_set_plus_equals(self):
        assert_parses_clean('MATCH (n) SET n += {age: 31} RETURN n;')

    def test_delete(self):
        assert_parses_clean('MATCH (n:Temp) DELETE n;')

    def test_detach_delete(self):
        assert_parses_clean('MATCH (n) DETACH DELETE n;')

    def test_remove_property(self):
        assert_parses_clean('MATCH (n:Person) REMOVE n.age RETURN n;')

    def test_remove_label(self):
        assert_parses_clean('MATCH (n:Person:Employee) REMOVE n:Employee RETURN n;')

    def test_foreach(self):
        assert_parses_clean(
            'MATCH p = (a)-[*]->(b) FOREACH (n IN nodes(p) | SET n.marked = true);'
        )


class TestExpressions:
    def test_property_access(self):
        assert_parses_clean('MATCH (n) RETURN n.name;')

    def test_chained_property(self):
        assert_parses_clean('MATCH (n) RETURN n.address.city;')

    def test_arithmetic(self):
        assert_parses_clean('RETURN 1 + 2 * 3;')

    def test_comparison(self):
        assert_parses_clean('MATCH (n) WHERE n.age >= 18 AND n.age < 65 RETURN n;')

    def test_boolean_and(self):
        assert_parses_clean('MATCH (n) WHERE n.a AND n.b RETURN n;')

    def test_boolean_or(self):
        assert_parses_clean('MATCH (n) WHERE n.a OR n.b RETURN n;')

    def test_boolean_xor(self):
        assert_parses_clean('MATCH (n) WHERE n.a XOR n.b RETURN n;')

    def test_boolean_not(self):
        assert_parses_clean('MATCH (n) WHERE NOT n.active RETURN n;')

    def test_complex_boolean(self):
        assert_parses_clean(
            'MATCH (n) WHERE (n.age > 18 AND n.active = true) OR n.role = "admin" RETURN n;'
        )

    def test_is_null(self):
        assert_parses_clean('MATCH (n) WHERE n.age IS NULL RETURN n;')

    def test_is_not_null(self):
        assert_parses_clean('MATCH (n) WHERE n.age IS NOT NULL RETURN n;')

    def test_in_list(self):
        assert_parses_clean('MATCH (n) WHERE n.status IN ["active", "pending"] RETURN n;')

    def test_starts_with(self):
        assert_parses_clean('MATCH (n) WHERE n.name STARTS WITH "A" RETURN n;')

    def test_ends_with(self):
        assert_parses_clean('MATCH (n) WHERE n.name ENDS WITH "son" RETURN n;')

    def test_contains(self):
        assert_parses_clean('MATCH (n) WHERE n.name CONTAINS "li" RETURN n;')

    def test_case_when(self):
        assert_parses_clean(
            'MATCH (n) RETURN CASE WHEN n.age < 18 THEN "minor" ELSE "adult" END AS category;'
        )

    def test_case_simple(self):
        assert_parses_clean(
            'MATCH (n) RETURN CASE n.status WHEN "A" THEN "Active" WHEN "I" THEN "Inactive" END;'
        )

    def test_negative_number(self):
        assert_parses_clean('MATCH (n) WHERE n.balance > -100 RETURN n;')

    def test_not_equal(self):
        assert_parses_clean('MATCH (n) WHERE n.status <> "deleted" RETURN n;')


class TestFunctions:
    def test_count_star(self):
        assert_parses_clean('MATCH (n) RETURN count(*);')

    def test_count(self):
        assert_parses_clean('MATCH (n) RETURN count(n);')

    def test_collect(self):
        assert_parses_clean('MATCH (n) RETURN collect(n.name);')

    def test_nested_functions(self):
        assert_parses_clean('MATCH (n) RETURN toUpper(trim(n.name));')

    def test_distinct_in_function(self):
        assert_parses_clean('MATCH (n) RETURN count(DISTINCT n.name);')

    def test_namespaced_function(self):
        assert_parses_clean('MATCH (n) RETURN apoc.text.join(collect(n.name), ", ");')


class TestPredicateFunctions:
    def test_all(self):
        assert_parses_clean('MATCH (n) WHERE ALL(x IN n.list WHERE x > 0) RETURN n;')

    def test_any(self):
        assert_parses_clean('MATCH (n) WHERE ANY(x IN n.list WHERE x > 0) RETURN n;')

    def test_none(self):
        assert_parses_clean('MATCH (n) WHERE NONE(x IN n.list WHERE x > 0) RETURN n;')

    def test_single(self):
        assert_parses_clean('MATCH (n) WHERE SINGLE(x IN n.list WHERE x > 0) RETURN n;')


class TestComprehensions:
    def test_list_comprehension(self):
        assert_parses_clean('MATCH (n) RETURN [x IN n.list WHERE x > 0 | x * 2];')

    def test_list_comprehension_no_filter(self):
        assert_parses_clean('MATCH (n) RETURN [x IN n.list | x * 2];')

    def test_pattern_comprehension(self):
        assert_parses_clean('MATCH (n) RETURN [(n)-[:KNOWS]->(m) | m.name];')

    def test_pattern_comprehension_with_where(self):
        assert_parses_clean(
            'MATCH (n) RETURN [(n)-[:KNOWS]->(m) WHERE m.age > 30 | m.name];'
        )


class TestSubqueries:
    def test_call_subquery(self):
        assert_parses_clean('CALL { MATCH (n) RETURN n LIMIT 1 } RETURN n;')

    def test_exists_pattern(self):
        assert_parses_clean('MATCH (n) WHERE EXISTS { (n)-[:KNOWS]->(:Person) } RETURN n;')

    def test_exists_query(self):
        assert_parses_clean(
            'MATCH (n) WHERE EXISTS { MATCH (n)-[:KNOWS]->(m) WHERE m.age > 30 } RETURN n;'
        )


class TestProcedureCalls:
    def test_standalone_call(self):
        assert_parses_clean('CALL db.labels();')

    def test_call_with_yield(self):
        assert_parses_clean('CALL db.labels() YIELD label RETURN label;')

    def test_call_in_query(self):
        assert_parses_clean('CALL db.labels() YIELD label RETURN label;')

    def test_call_yield_star(self):
        assert_parses_clean('CALL db.stats.retrieve("GRAPH COUNTS") YIELD *;')


class TestParameters:
    def test_dollar_parameter(self):
        assert_parses_clean('MATCH (n) WHERE n.id = $id RETURN n;')

    def test_parameter_in_create(self):
        assert_parses_clean('CREATE (n:Person $props) RETURN n;')


class TestLabels:
    def test_multiple_labels(self):
        assert_parses_clean('MATCH (n:Person:Employee) RETURN n;')

    def test_backtick_label(self):
        assert_parses_clean('MATCH (n:`My Label`) RETURN n;')

    def test_backtick_property(self):
        assert_parses_clean('MATCH (n) RETURN n.`strange prop`;')


class TestStringEscapes:
    def test_escaped_backslash(self):
        assert_parses_clean('RETURN "hello\\\\nworld";')

    def test_double_quoted(self):
        assert_parses_clean('RETURN "hello world";')

    def test_single_quoted(self):
        assert_parses_clean("RETURN 'x';")


class TestComplexQueries:
    def test_with_aggregation(self):
        assert_parses_clean(
            'MATCH (n)-[:KNOWS]->(m) WITH n, collect(m) AS friends '
            'RETURN n.name, size(friends);'
        )

    def test_multi_match_with_pipeline(self):
        assert_parses_clean(
            'MATCH (user:User) '
            'WITH user '
            'MATCH (user)-[:POSTED]->(post:Post) '
            'RETURN user.name, count(post) AS postCount '
            'ORDER BY postCount DESC '
            'LIMIT 10;'
        )

    def test_merge_with_both_actions(self):
        assert_parses_clean(
            'MERGE (n:User {id: 42}) '
            'ON CREATE SET n.created = timestamp() '
            'ON MATCH SET n.lastSeen = timestamp() '
            'RETURN n;'
        )

    def test_create_relationship_with_props(self):
        assert_parses_clean(
            'MATCH (a:Person {name: "Alice"}), (b:Person {name: "Bob"}) '
            'CREATE (a)-[:KNOWS {since: 2020}]->(b);'
        )


class TestASTStructure:
    """Test that the AST structure is correct, not just that parsing succeeds."""

    def test_result_has_expected_keys(self):
        result = parse('MATCH (n) RETURN n;')
        assert 'result' in result
        assert 'errors' in result

    def test_no_errors(self):
        result = parse('MATCH (n) RETURN n;')
        assert result['errors'] == []

    def test_nodes_have_structure(self):
        result = parse('MATCH (n) RETURN n;')
        first_node = result['result'][0]
        assert 'node' in first_node
        assert 'children' in first_node
        assert 'parent' in first_node['node']
        assert 'text' in first_node['node']
        assert 'sourceInterval' in first_node['node']

    def test_top_level_is_script(self):
        result = parse('MATCH (n) RETURN n;')
        parents = [r['node']['parent'] for r in result['result'] if r['node']['text']]
        assert 'Script' in parents

    def test_eof_present(self):
        result = parse('MATCH (n) RETURN n;')
        texts = [r['node']['text'] for r in result['result']]
        assert '<EOF>' in texts

    def test_error_detection(self):
        """Verify that invalid syntax produces errors."""
        result = parse('NOT VALID CYPHER ??? !!!')
        errors = count_errors(result)
        assert errors > 0


class TestEdgeCases:
    def test_empty_string(self):
        result = parse('')
        # Should not crash
        assert 'result' in result

    def test_semicolon_only(self):
        result = parse(';')
        assert 'result' in result

    def test_whitespace_only(self):
        result = parse('   ')
        assert 'result' in result

    def test_comments(self):
        assert_parses_clean('/* comment */ MATCH (n) RETURN n;')

    def test_line_comment(self):
        assert_parses_clean('// line comment\nMATCH (n) RETURN n;')

    def test_case_insensitive_keywords(self):
        assert_parses_clean('match (n) return n;')

    def test_mixed_case_keywords(self):
        assert_parses_clean('Match (n) Where n.age > 10 Return n;')
