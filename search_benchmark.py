from pymilvus import connections, Collection
import numpy as np
import time

# Connect to Milvus
connections.connect("default", host="localhost", port="19530", max_receive_message_length=514983574, max_send_message_length=514983574)
collection_name = "diskann_benchmark"
collection = Collection(name=collection_name)

# Search Benchmark Function
def search_benchmark(num_queries, dim=128, ef=50):
    query_vectors = [np.random.random(dim).tolist() for _ in range(num_queries)]
    search_params = {"metric_type": "L2", "params": {"ef": ef}}
    start_time = time.time()
    results = collection.search(query_vectors, "vector", search_params, limit=10)
    end_time = time.time()
    print(f"Search completed in {end_time - start_time:.2f} seconds.")
    return results

# Run Search Benchmarks
for queries in [10, 100, 1000]:  # Vary the number of queries
    print(f"Running benchmark with {queries} queries...")
    search_benchmark(num_queries=queries)
