import math

class Vector:
    def __init__(self, *components):
        if len(components) == 0:
            raise ValueError("A vector must have at least one component.")
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of components.")
        result = tuple(a + b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same number of components.")
        result = tuple(a - b for a, b in zip(self.components, other.components))
        return Vector(*result)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same number of components.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            result = tuple(a * other for a in self.components)
            return Vector(*result)
        else:
            raise ValueError("Multiplication with type not supported.")

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize the zero vector.")
        result = tuple(a / magnitude for a in self.components)
        return