"""
Main module for the HelloWorld package.
Contains functions for greeting the world and specific people.
"""


def hello_world():
    """
    Print a simple 'Hello, World!' message.
    
    Returns:
        str: The greeting message
    """
    message = "Hello, World!"
    print(message)
    return message


def greet(name):
    """
    Print a personalized greeting message.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: The personalized greeting message
        
    Raises:
        TypeError: If name is not a string
        ValueError: If name is empty or whitespace only
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    if not name.strip():
        raise ValueError("Name cannot be empty")
    
    message = f"Hello, {name.strip()}!"
    print(message)
    return message


def main():
    """Main entry point for the application."""
    hello_world()


if __name__ == "__main__":
    main() 