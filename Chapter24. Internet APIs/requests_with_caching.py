import requests_with_caching
# it's not found in the permanent cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
print(res.text[:100])
# this time it will be found in the temporary cache
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
# This one is in the permanent cache.
res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
