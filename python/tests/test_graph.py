import pytest

from code_challenges.graph.graph import Graph, Vertex, Edge


def test_can_instantiate_Graph():
    graph = Graph()
    assert graph
    assert graph._adjacency_list == {}


def test_can_instantiate_Vertex():
    vertex = Vertex()
    assert vertex
    assert vertex.value == None


def test_can_instantiate_Edge():
    vertex1 = Vertex("selam")
    edge = Edge(vertex1, weight=50)
    assert edge.vertex == vertex1
    assert edge.weight == 50


def test_vertex_can_be_added_to_graph():
    graph = Graph()
    vertex1 = Vertex("selam")
    graph.add_node(vertex1)
    result = graph.size()
    assert result == 1


def test_an_edge_can_be_added_to_graph():
    graph = Graph()
    vertex1 = Vertex(1)
    vertex2 = Vertex(2)
    graph.add_node(vertex1)
    graph.add_node(vertex2)
    graph.add_edge(vertex1, vertex2, 20)
    vertex1_list = graph._adjacency_list[vertex1]
    first_edge = vertex1_list[0]
    assert first_edge.vertex == vertex2
    assert first_edge.weight == 20


def test_a_collection_of_all_nodes_can_be_retrieved_from_graph():
    graph = Graph()
    vertex1 = Vertex(1)
    vertex2 = Vertex(2)
    vertex3 = Vertex(3)
    graph.add_node(vertex1)
    graph.add_node(vertex2)
    graph.add_node(vertex3)
    list = graph.get_nodes()
    expected = [1, 2, 3]
    actual = []
    for x in list:
        actual.append(x.value)
    assert actual == expected


def test_neighbors_are_returned_with_weights_between_nodes_included():
    graph = Graph()
    vertex1 = Vertex(1)
    vertex2 = Vertex(2)
    vertex3 = Vertex(3)
    graph.add_node(vertex1)
    graph.add_node(vertex2)
    graph.add_node(vertex3)
    graph.add_edge(vertex1, vertex2, 20)
    graph.add_edge(vertex1, vertex3, 30)
    actual = graph.get_neighbors(vertex1)

    # actual is a list of edges
    # edges have vertex and weight properties
    # we want to check correct vertex and weight

    edge1 = actual[0]
    edge2 = actual[1]
    assert edge1.vertex == vertex2
    assert edge1.weight == 20
    assert edge2.vertex == vertex3
    assert edge2.weight == 30


def test_size_returns_correct_size():
    graph = Graph()
    vertex1 = Vertex(1)
    vertex2 = Vertex(2)
    vertex3 = Vertex(3)
    graph.add_node(vertex1)
    graph.add_node(vertex2)
    graph.add_node(vertex3)
    actual = graph.size()
    assert actual == 3

