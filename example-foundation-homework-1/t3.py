"""Task 3"""

# This task doesn't have any sub questions so we can just call it t2 or t2q1!

class WorldGreeter():
    """An more complicated hello world example"""
    def __init__(self, world="world"):
        self.greeting = f"hello, {world}!"

    def greet(self):
        """Prints a greeting to the world"""
        print(self.greeting)

    def aggressively_greet(self, times):
        """Prints a lot of greetings to the world"""
        for i in range(times):
            print(self.greeting)

if __name__ == "__main__":
    earthGreater = WorldGreeter("earth")
    earthGreater.greet()
    marsGreater = WorldGreeter("mars")
    marsGreater.aggressively_greet(100)