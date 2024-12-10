import requests
import json
import networkx as nx
from itertools import permutations
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from datetime import datetime
import os
import csv

# API keys for Alpaca
api_key = 'PKLE7Y1G8TGII7728VVB'  # Replace with your actual API key
api_secret = 'EPK95ECziHn5Zhz7ld0rPV3bb21B13By5ve3QA9s'  # Replace with your actual API secret
client = TradingClient(api_key, api_secret, paper=True)  # Initialize Alpaca trading client

# Dictionary of cryptocurrency names and their respective ticker symbols
coins = {
    'us dollar coin': 'usdc',
    'bitcoin-cash': 'bch',
    'eos': 'eos',
    'litecoin': 'ltc',
    'ethereum': 'eth',
    'bitcoin': 'btc',
    'polkadot': 'dot',
    'chainlink': 'link',
    'stellar': 'xlm',
    'avalanche': 'avax',
    'basic attention token': 'bat',
    'sushiswap': 'sushi'
}

def place_order(symbols, qty, side):
    # Function to place market orders for given symbols
    for symbol in symbols:
        # Create a market order request
        order = MarketOrderRequest(
            symbol=(symbol.strip() + 'USD').upper(),  # Ensure the symbol is formatted correctly
            notional=qty,  # Amount to trade
            side=side,  # Buy or Sell
            time_in_force=TimeInForce.GTC  # Order is good 'til canceled
        )
        try:
            market_order = client.submit_order(order_data=order)  # Submit the order
            print(f"Order submitted: {market_order}")  # Print order confirmation
        except Exception as e:
            print("Error submitting order:", str(e))  # Print error if order fails

def get_exchange_rates():
    # Fetch current exchange rates from CoinGecko API
    names_url = ','.join(coins.keys())  # Create a comma-separated string of coin names
    ticker_url = ','.join(coins.values())  # Create a comma-separated string of ticker symbols
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={names_url}&vs_currencies={ticker_url}'  # Construct API URL
    
    # Make the GET request and return the parsed JSON data
    response = requests.get(url)  # Fetch data from CoinGecko API
    return response.json()  # Return the JSON response

def build_graph(data):
    # Build a directed graph with exchange rates as edge weights
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
                continue  # Skip if there's a missing rate
    
    return g  # Return the constructed graph

def dfs(graph, node, visited):
    # Depth-first search to explore graph connectivity
    visited.add(node)  # Mark the current node as visited
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Recursively visit unvisited neighbors

def check_reachability(graph, start_node):
    # Check if all nodes are reachable from the start node
    visited = set()  # Set to keep track of visited nodes
    dfs(graph, start_node, visited)  # Perform DFS
    
    # Compare the visited nodes with all nodes in the graph to find unreachable nodes
    all_nodes = set(graph.nodes)  # Get all nodes in the graph
    missing_nodes = all_nodes - visited  # Identify missing nodes
    return missing_nodes  # Return unreachable nodes

def check_arbitrage(g):
    arbitrage_opportunities = []  # List to store arbitrage opportunities

    # First, check if all nodes are reachable from a given start node ('btc')
    missing_nodes = check_reachability(g, 'btc')
    
    if missing_nodes:
        print(f"Not all nodes are reachable from 'btc'. Missing nodes: {missing_nodes}")
        return []  # Return an empty list if there are missing nodes
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

                # Store the arbitrage opportunity with its path and factor
                arbitrage_opportunities.append({
                    "arbitrage_factor": arbitrage_factor,
                    "forward_path": path,
                    "reverse_path": path_reverse
                })

            except KeyError:
                print(f"Missing edge for path: {path}")  # Print warning for missing edges
                continue

    # Sort the opportunities by arbitrage factor in descending order
    arbitrage_opportunities.sort(key=lambda x: x["arbitrage_factor"], reverse=True)

    # Get the top 10 arbitrage opportunities
    top_10_opportunities = arbitrage_opportunities[:10]

    # Print the top 10 arbitrage opportunities
    print("=" * 50)
    if top_10_opportunities:
        print("Top 10 Arbitrage Opportunities:")
        for i, opportunity in enumerate(top_10_opportunities):
            print(f"{i + 1}. Arbitrage Factor: {opportunity['arbitrage_factor']}")
            print(f"   Forward Path: {opportunity['forward_path']} -> Reverse Path: {opportunity['reverse_path']}")
        
        # Ensure the directory exists
        os.makedirs('final_Project', exist_ok=True)

        # Save the top 10 opportunities to a JSON file in the specified directory
        with open('final_Project/results.json', 'w') as json_file:
            json.dump(top_10_opportunities, json_file, indent=4)
        
        return top_10_opportunities  # Return the top 10 opportunities
    else:
        print("No arbitrage opportunities found.")
        return []  # Return an empty list if no opportunities found

def save_arbitrage_pairs_to_csv(opportunities):
    # Save arbitrage pairs to a CSV file
    current_directory = os.getcwd()  # Get the current working directory
    print(f"Current Directory: {current_directory}")

    # Define the path for the data directory inside the Final_project folder
    data_directory = os.path.join(current_directory, 'Final_project', 'data')
    os.makedirs(data_directory, exist_ok=True)  # Create directory if it doesn't exist
    # Get the current date and time for the filename
    now = datetime.now()
    
    # Create a unique filename based on the first opportunity's paths
    
    filename = f"currency_pair_{now.strftime('%Y.%m.%d_%H.%M')}.txt"

    filepath = os.path.join(data_directory, filename)  # Full path for the file

    # Write the currency pairs to a CSV file
    try:
        with open(filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['currency_from', 'currency_to', 'exchange_rate'])  # Write header

            # Iterate through the opportunities and write each currency pair and its exchange rate
            for opportunity in opportunities:
                forward_path = opportunity['forward_path']
                # Assuming you want to write the exchange rates for the first and last currency in the path
                currency_from = forward_path[0]
                currency_to = forward_path[-1]
                exchange_rate = opportunity['arbitrage_factor']  # Use the arbitrage factor as a placeholder for the exchange rate

                writer.writerow([currency_from, currency_to, exchange_rate])  # Write currency pair and exchange rate

        print(f"Arbitrage pairs saved to {filepath}")  # Confirm successful save
    except Exception as e:
        print("Error saving arbitrage pairs to CSV:", str(e))  # Print error if saving fails

def main():
    data = get_exchange_rates()  # Fetch exchange rates from CoinGecko API
    print("Fetched Exchange Rates:", data)  # Optional: print the fetched exchange rates for debugging

    g = build_graph(data)  # Build a directed graph from the exchange rate data

    # Print the nodes and edges for debugging
    print("Graph Nodes:", g.nodes)
    print("Graph Edges:", g.edges)

    top_10_opportunities = check_arbitrage(g)  # Get the top 10 arbitrage opportunities

    # Save the arbitrage pairs to a CSV file
    save_arbitrage_pairs_to_csv(top_10_opportunities)

    # If there are top 10 opportunities, place orders
    if top_10_opportunities:
        for opportunity in top_10_opportunities:
            forward_path = opportunity['forward_path']
            # Assuming you want to buy the first coin in the forward path and sell the last coin
            buy_symbol = forward_path[0]
            sell_symbol = forward_path[-1]
            qty = 1000  # Define the quantity you want to trade

            # Place buy order
            print(f"Placing buy order for {buy_symbol}...")
            place_order([buy_symbol], qty, OrderSide.BUY)

            # Place sell order
            print(f"Placing sell order for {sell_symbol}...")
            place_order([sell_symbol], qty, OrderSide.SELL)
    else:
        print("No arbitrage opportunities found. No orders will be placed.")

if __name__ == "__main__":
    main()  # Execute the main function