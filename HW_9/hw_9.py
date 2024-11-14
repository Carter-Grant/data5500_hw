import requests  # For making API requests
import json  # For parsing JSON data
import networkx as nx  # For graph manipulation and traversal
from itertools import permutations  # For generating all pairs of currency nodes

# Dictionary of cryptocurrency names and their respective ticker symbols
coins = {
    'ripple': 'xrp',
    'cardano': 'ada',
    'bitcoin-cash': 'bch',
    'eos': 'eos',
    'litecoin': 'ltc',
    'ethereum': 'eth',
    'bitcoin': 'btc'
}

# Fetch exchange rates from the CoinGecko API
def get_exchange_rates():
    # Build the API URL using the coin names and tickers
    names_url = ','.join(coins.keys())
    ticker_url = ','.join(coins.values())
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={names_url}&vs_currencies={ticker_url}'
    
    # Make the GET request and return the parsed JSON data
    response = requests.get(url)
    return response.json()

# Build a directed graph with exchange rates as edge weights
def build_graph(data):
    g = nx.DiGraph()  # Initialize a directed graph
    
    # Add edges to the graph based on the fetched exchange rates
    for coin, coin_data in data.items():
        for tkr, rate in coin_data.items():
            node_from = coins[coin]  # Source node (cryptocurrency)
            node_to = tkr  # Target node (cryptocurrency)
            try:
                g.add_edge(node_from, node_to, weight=rate)  # Add edge with exchange rate as weight
            except KeyError:
                print(f"Warning: Missing exchange rate from {node_from} to {node_to}. Skipping...")
                continue
    
    return g  # Return the constructed graph

# Depth-first search to explore graph connectivity
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Check if all nodes are reachable from the starting node
def check_reachability(graph, start_node):
    visited = set()
    dfs(graph, start_node, visited)
    
    # Compare the visited nodes with all nodes in the graph to find unreachable nodes
    all_nodes = set(graph.nodes)
    missing_nodes = all_nodes - visited
    return missing_nodes

# Check for arbitrage opportunities in the graph
def check_arbitrage(g):
    max_opportunity = 0  # Track the maximum arbitrage opportunity
    min_opportunity = float('inf')  # Track the minimum arbitrage opportunity
    max_path = min_path = None  # Store the paths for maximum and minimum arbitrage

    # First, check if all nodes are reachable from a given start node ('btc')
    missing_nodes = check_reachability(g, 'btc')
    
    if missing_nodes:
        print(f"Not all nodes are reachable from 'btc'. Missing nodes: {missing_nodes}")
        # Skip unreachable nodes, but continue with the arbitrage check
    else:
        print("All nodes are reachable from 'btc'. Proceeding with arbitrage check...")

    # Check arbitrage for all pairs of nodes (currencies)
    for n1, n2 in permutations(g.nodes, 2):  # Generate all pairs of nodes
        if n1 in missing_nodes or n2 in missing_nodes:
            continue  # Skip pairs where either node is unreachable
        
        print(f"\nChecking paths from {n1} to {n2}...")

        # Check all simple paths between n1 and n2
        for path in nx.all_simple_paths(g, source=n1, target=n2):
            try:
                # Calculate forward path weight (product of exchange rates along the path)
                path_weight_to = 1.0
                for i in range(len(path) - 1):
                    path_weight_to *= g[path[i]][path[i + 1]]['weight']
                
                # Calculate reverse path weight
                path_reverse = list(reversed(path))  # Reverse the path
                path_weight_from = 1.0
                for i in range(len(path_reverse) - 1):
                    path_weight_from *= g[path_reverse[i]][path_reverse[i + 1]]['weight']
                
                # Calculate the arbitrage factor (product of forward and reverse path weights)
                arbitrage_factor = path_weight_to * path_weight_from

                # Print the details of the path and the arbitrage factor
                print(f"Path: {path}")
                print(f"Forward path weight: {path_weight_to}")
                print(f"Reverse path weight: {path_weight_from}")
                print(f"Arbitrage factor: {arbitrage_factor}")

                # Track the maximum and minimum arbitrage opportunities
                if arbitrage_factor > max_opportunity:
                    max_opportunity = arbitrage_factor
                    max_path = (path, path_reverse)
                
                if arbitrage_factor < min_opportunity:
                    min_opportunity = arbitrage_factor
                    min_path = (path, path_reverse)

            except KeyError:
                print(f"Missing edge for path: {path}")
                continue

    # Print the results for the arbitrage opportunities
    print("=" * 50)
    if max_path and min_path:
        print(f"Max Arbitrage Opportunity: {max_opportunity}")
        print(f"Path: {max_path[0]} -> {max_path[1]}")
        print(f"Min Arbitrage Opportunity: {min_opportunity}")
        print(f"Path: {min_path[0]} -> {min_path[1]}")
    else:
        print("No arbitrage opportunities found.")

# Main function to run the entire program
def main():
    data = get_exchange_rates()  # Fetch exchange rates from CoinGecko API
    print("Fetched Exchange Rates:", data)  # Optional: print the fetched exchange rates for debugging
    g = build_graph(data)  # Build a directed graph from the exchange rate data
    check_arbitrage(g)  # Check for arbitrage opportunities in the graph

# Program entry point
if __name__ == "__main__":
    main()
