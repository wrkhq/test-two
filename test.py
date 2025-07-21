from main import main


def test_main_returns_hello():
    """Test that main function returns 'Hello'"""
    result = main()
    assert result == "Hello John"
    print(f"✓ main() returned: '{result}'")
