"""
Tests for the main module of the HelloWorld package.
"""

import pytest
from io import StringIO
import sys
from helloworld.main import hello_world, greet, main


class TestHelloWorld:
    """Test cases for the hello_world function."""
    
    def test_hello_world_returns_correct_message(self):
        """Test that hello_world returns the correct message."""
        result = hello_world()
        assert result == "Hello, World!"
    
    def test_hello_world_is_string(self):
        """Test that hello_world returns a string."""
        result = hello_world()
        assert isinstance(result, str)
    
    def test_hello_world_prints_message(self, capsys):
        """Test that hello_world prints to stdout."""
        hello_world()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello, World!"


class TestGreet:
    """Test cases for the greet function."""
    
    def test_greet_with_valid_name(self):
        """Test greeting with a valid name."""
        result = greet("Alice")
        assert result == "Hello, Alice!"
    
    def test_greet_with_name_with_spaces(self):
        """Test greeting with a name that has leading/trailing spaces."""
        result = greet("  Bob  ")
        assert result == "Hello, Bob!"
    
    def test_greet_prints_message(self, capsys):
        """Test that greet prints to stdout."""
        greet("Charlie")
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello, Charlie!"
    
    def test_greet_with_empty_string_raises_error(self):
        """Test that greeting with empty string raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")
    
    def test_greet_with_whitespace_only_raises_error(self):
        """Test that greeting with whitespace-only string raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("   ")
    
    def test_greet_with_non_string_raises_error(self):
        """Test that greeting with non-string input raises TypeError."""
        with pytest.raises(TypeError, match="Name must be a string"):
            greet(123)
        
        with pytest.raises(TypeError, match="Name must be a string"):
            greet(None)
        
        with pytest.raises(TypeError, match="Name must be a string"):
            greet(["Alice"])
    
    def test_greet_with_unicode_name(self):
        """Test greeting with unicode characters."""
        result = greet("José")
        assert result == "Hello, José!"
    
    def test_greet_with_long_name(self):
        """Test greeting with a very long name."""
        long_name = "A" * 100
        result = greet(long_name)
        assert result == f"Hello, {long_name}!"


class TestMain:
    """Test cases for the main function."""
    
    def test_main_calls_hello_world(self, capsys):
        """Test that main function calls hello_world."""
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == "Hello, World!" 