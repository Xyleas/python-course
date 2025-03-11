from llama_index import VectorStoreIndex, SimpleDirectoryReader #, SummaryIndex

# Load documents
docs = SimpleDirectoryReader('input_files=['./docs1/example.csv').load_data()
docs[0].metadata['category'] = 'customer support'

# Create index
index = VectorStoreIndex.from_documents(docs)

# Save index
index.storage_context.persist()

# Query
query_engine = index.as_query_engine(verbose = True, similarity_top_k = 6, response_mode = 'tree_summarize')
response = query_engine.query('summarize our customer support content')
print(response)

print(response.get_formatted_sources())
#testing print(response.source_nodes)