"""
File: VariableScope.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module demonstrates Python's variable scope rules using the LEGB 
    (Local, Enclosing, Global, Built-in) resolution order. Understanding 
    scope is fundamental to avoiding naming conflicts and writing maintainable code.

Complexity Analysis:
    - Time Complexity: O(1) for variable lookup in each scope level.
    - Space Complexity: O(n) where n is the number of variables in all scopes.

Logic:
    1. Python resolves variable names by searching scopes in LEGB order.
    2. Local scope: Variables defined within the current function.
    3. Enclosing scope: Variables in outer functions (for nested functions).
    4. Global scope: Variables defined at the module level.
    5. Built-in scope: Python's built-in names (print, len, etc.).
"""


class VariableScopeDemo:
    """
    A demonstration class for Python's LEGB scope rules.
    """

    def __init__(self):
        """Initializes the demo with a class-level variable."""
        self.instance_var = "Instance Variable"

    @staticmethod
    def demonstrate_local_scope():
        """Demonstrates local scope - variables defined within a function."""
        x = "Local x"
        y = "Local y"
        print(f"Inside function: x = '{x}', y = '{y}'")
        return x, y

    @staticmethod
    def demonstrate_global_scope():
        """Demonstrates global scope access and modification."""
        global global_var
        print(f"Accessing global_var: '{global_var}'")
        global_var = "Modified Global"
        print(f"After modification: '{global_var}'")

    @staticmethod
    def demonstrate_enclosing_scope():
        """Demonstrates enclosing (nonlocal) scope in nested functions."""
        enclosing_var = "Enclosing Value"

        def inner_function():
            nonlocal enclosing_var
            print(f"Inner accessing enclosing: '{enclosing_var}'")
            enclosing_var = "Modified by Inner"

        print(f"Before inner call: '{enclosing_var}'")
        inner_function()
        print(f"After inner call: '{enclosing_var}'")

    @staticmethod
    def demonstrate_builtin_scope():
        """Demonstrates built-in scope (Python's built-in functions)."""
        # 'len' is a built-in function
        sample_list = [1, 2, 3, 4, 5]
        print(f"Using built-in 'len': len({sample_list}) = {len(sample_list)}")

        # Shadowing a built-in (not recommended)
        # len = lambda x: "shadowed"  # This would shadow the built-in


# Global variable for demonstration
global_var = "Original Global"


def main():
    """
    Demonstrates the scholarly Variable Scope implementation.
    """
    print("--- Variable Scope Demo (LEGB Rule) ---\n")

    demo = VariableScopeDemo()

    # 1. Local Scope
    print("1. LOCAL SCOPE")
    print("-" * 40)
    demo.demonstrate_local_scope()
    print()

    # 2. Enclosing Scope
    print("2. ENCLOSING SCOPE (Nested Functions)")
    print("-" * 40)
    demo.demonstrate_enclosing_scope()
    print()

    # 3. Global Scope
    print("3. GLOBAL SCOPE")
    print("-" * 40)
    print(f"Initial global_var: '{global_var}'")
    demo.demonstrate_global_scope()
    print()

    # 4. Built-in Scope
    print("4. BUILT-IN SCOPE")
    print("-" * 40)
    demo.demonstrate_builtin_scope()
    print()

    # Instance variable demonstration
    print("5. INSTANCE (Class) SCOPE")
    print("-" * 40)
    print(f"Instance variable: '{demo.instance_var}'")

    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()
