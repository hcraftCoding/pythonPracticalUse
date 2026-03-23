"""
Practice 3: finally in an API context


api_keys_remaining = 10

def make_api_call(query):
    # write a try/except/finally that:
    # - tries to print f"Calling API with query: {query}"
    # - raises a ValueError if query is an empty string
    # - catches the ValueError with a clean message
    # - always subtracts 1 from api_keys_remaining in finally
    #   and prints f"API calls remaining: {api_keys_remaining}"
    pass
apiKeysRemaining is defined outside of the function
"""
api_keys_remaining = 10

def make_api_call(query):
    global api_keys_remaining   #= 10 cant assign/modify var on same like as sglobal just declare it
    try:
        if query == "":
            raise ValueError
        print(f"Calling API with query: {query}") #had it at top/ but print display even if Error
    except ValueError:
        print("query is empty")
    finally:
        api_keys_remaining -= 1
        print(f"API keys remaining: {api_keys_remaining}")

make_api_call("weather in Jackson")
make_api_call("")
make_api_call("stock price AAPL")