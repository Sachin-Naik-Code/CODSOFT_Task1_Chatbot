file_path = r"C:\Users\sachin\Downloads\archive (7)\dialogs.txt"

queries_responses = []

# Read the dataset file
with open(file_path, 'r') as file:
    for line in file:
        if "::" in line:
            query, response = line.strip().split("::")
            queries_responses.append((query, response))

# Print the queries and responses in a tabular format
print(f"{'Query':<50} {'Response':<50}")
print("="*100)
for query, response in queries_responses:
    print(f"{query:<50} {response:<50}")
