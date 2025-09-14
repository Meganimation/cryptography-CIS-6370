import requests
import json

# Base URL for the API
BASE_URL = 'http://localhost:5000'

def test_get_hello():
    """Test the GET /hello endpoint"""
    print("Testing GET /hello...")
    try:
        response = requests.get(f'{BASE_URL}/hello')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_post_hello():
    """Test the POST /hello endpoint"""
    print("\nTesting POST /hello...")
    try:
        # Test data
        test_data = {'greetingMsg': 'Hello from the test!'}
        
        response = requests.post(
            f'{BASE_URL}/hello',
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

def test_updated_greeting():
    """Test that the greeting was actually updated"""
    print("\nTesting updated greeting...")
    try:
        response = requests.get(f'{BASE_URL}/hello')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            data = response.json()
            return data.get('greetingMsg') == 'Hello from the test!'
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    print("Starting backend tests...")
    print("Make sure the backend is running on http://localhost:5000")
    print("-" * 50)
    
    # Run tests
    test1 = test_get_hello()
    test2 = test_post_hello()
    test3 = test_updated_greeting()
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print(f"GET /hello: {'PASS' if test1 else 'FAIL'}")
    print(f"POST /hello: {'PASS' if test2 else 'FAIL'}")
    print(f"Updated greeting: {'PASS' if test3 else 'FAIL'}")
    
    if all([test1, test2, test3]):
        print("\nAll tests passed! ✅")
    else:
        print("\nSome tests failed! ❌")
