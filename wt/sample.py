# test_project/sample.py
import asyncio
from collections import deque

GLOBAL_VAR = 100
GLOBAL_ANNOTATED: str = "hello"

class MyBaseClass:
    """A base class."""
    pass

# @classmethod # Example decorator
# def some_class_method(cls):
#     pass # Body ignored for now

class MyClass(MyBaseClass):
    """
    This is a sample class.
    It has attributes and methods.
    """
    CLASS_ATTRIBUTE: int = 10 # Class attribute with annotation

    instance_var = None # Class attribute without annotation (detected by Assign)

    def __init__(self, name: str, value: int = 0):
        """Constructor"""
        self.name = name # Instance attribute assignment
        self._value = value # Private convention attribute assignment
        self.items = deque() # Using imported name

    @property # Decorator
    def value(self) -> int:
        """Getter for value."""
        return self._value

    def add_item(self, item: any): # Method
        """Adds an item."""
        self.items.append(item)
        # Calls helper_function - Call detection is basic/optional
        #_local_var = helper_function(item)
        print(f"Added {item}")

    async def async_method(self): # Async method
        """An asynchronous method."""
        await asyncio.sleep(0.1) # Requires import asyncio usually
        return True

    class InnerClass: # Inner class
         """An inner class."""
         INNER_CONST = "nested"

# def helper_function(data) -> bool: # Top-level function
#     """A standalone helper function."""
#     print(f"Helper received: {data}")
#     if data:
#         return True
#     return False
#
# async def async_global_function(): # Async top-level function
#     """An async global function."""
#     pass

# Example of assignment that isn't a simple variable
# result = helper_function(GLOBAL_VAR) # Parser currently ignores this type

if __name__ == "__main__":
    instance = MyClass("wt", 5)
    instance.add_item("apple")
    print(instance.value)