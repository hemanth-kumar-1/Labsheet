from googleapiclient.discovery import build

def search_cse(api_key, search_engine_id, search_term):
  try:
    service = build("customsearch", "v1", developerKey=api_key)

    request = service.cse().list(
        q=search_term, cx=search_engine_id
    )

    response = request.execute()

    if 'items' in response:
      return response['items']
    else:
      print("No results found.")
      return None

  except Exception as e:
    print(f"An error occurred: {e}")
    return None

API_KEY = "YOUR_API_KEY"
SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"
SEARCH_TERM = "memory leaks"

results = search_cse(API_KEY, SEARCH_ENGINE_ID, SEARCH_TERM)

if results:
  print(f"Search results for '{SEARCH_TERM}':")
  for item in results:
    print(f"- Title: {item['title']}")
    print(f"  Snippet: {item['snippet']}")
    print(f"  Link: {item['link']}")
    print("---")
