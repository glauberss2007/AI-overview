import orderedvector

vector = orderedvector.OrderedVector(10)
vector.vector_print()

vector.insert(6)
vector.vector_print()

vector.insert(4)
vector.vector_print()

vector.insert(3)
vector.vector_print()

vector.insert(5)
vector.vector_print()

vector.insert(1)
vector.vector_print()

vector.insert(8)
vector.vector_print()

vector.linear_search(3)
vector.linear_search(2)
vector.linear_search(9)

vector.vector_print()

vector.remove(5)
vector.vector_print()

vector.remove(1)
vector.vector_print()

vector.remove(8)
vector.vector_print()

vector.remove(9)

vector = orderedvector.OrderedVector(10)
vector.insert(8)
vector.insert(9)
vector.insert(4)
vector.insert(1)
vector.insert(5)
vector.insert(7)
vector.insert(11)
vector.insert(13)
vector.insert(2)
vector.vector_print()

vector.binary_search(7)

vector.binary_search(5)

vector.binary_search(13)

vector.binary_search(20)