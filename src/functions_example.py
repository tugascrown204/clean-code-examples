def fetch_data(data_source):
    """Fetch data from the specified data source."""
    # Simulated data fetching; replace with actual implementation
    return [1, 2, 3, 4, 5]


def process_data(data):
    """Process the fetched data by summing it."""
    return sum(data)

# Example usage:
data = fetch_data('data_source')
processed_result = process_data(data)
print(f'Processed result: {processed_result}')