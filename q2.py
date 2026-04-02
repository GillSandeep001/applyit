
# Assignment #2 - Flyweight Pattern Implementation
# This example demonstrates memory optimization by sharing objects.

# Flyweight interface
class Flyweight:
    def operation(self, extrinsic_state):
        # Method to be implemented by concrete flyweights
        pass


# ConcreteFlyweight stores intrinsic (shared) state
class ConcreteFlyweight(Flyweight):
    def __init__(self, intrinsic_state):
        # intrinsic_state represents shared data
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        # extrinsic_state is context-specific data passed at runtime
        print(f"Character: {self.intrinsic_state}, Position: {extrinsic_state}")


# FlyweightFactory ensures objects are reused instead of recreated
class FlyweightFactory:
    def __init__(self):
        # Dictionary to store existing flyweight objects
        self._flyweights = {}

    def get_flyweight(self, key):
        # Check if flyweight already exists
        if key not in self._flyweights:
            print("Creating new flyweight object...")
            self._flyweights[key] = ConcreteFlyweight(key)
        else:
            print("Reusing existing flyweight object...")
        return self._flyweights[key]

    def list_flyweights(self):
        # Display currently stored flyweights
        print(f"Current flyweights: {list(self._flyweights.keys())}")


# Client code
if __name__ == "__main__":
    factory = FlyweightFactory()

    # Request flyweights
    letter1 = factory.get_flyweight("A")
    letter2 = factory.get_flyweight("A")
    letter3 = factory.get_flyweight("B")

    # Display stored flyweights
    factory.list_flyweights()

    # Use flyweights with different extrinsic states
    letter1.operation("Position 1")
    letter2.operation("Position 2")
    letter3.operation("Position 3")

    # Verify object reuse
    print("Are letter1 and letter2 the same object?")
    print(letter1 is letter2)
