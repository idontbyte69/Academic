import tkinter as tk
from tkinter import messagebox, ttk
import networkx as nx
import random
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple

# Constants
NODE_TYPES = {
    "Building": ["A Building", "B Building", "E Building", "F Building", "I Building", "J Building"],
    "Junction": ["C Junction", "G Junction", "K Junction"],
    "Enemy Camp": ["D Enemy Camp", "H Enemy Camp"],
    "Home": ["Home Node"]
}

ROLES = ["Army", "Volunteer", "Rescuer"]
WINDOW_TITLE = "Perfect Pathway"
WINDOW_SIZE = "800x600"
FONT_FAMILY = "Helvetica"
TITLE_FONT = (FONT_FAMILY, 16)
NORMAL_FONT = (FONT_FAMILY, 12)

# Graph generation parameters
MIN_CONNECTIONS = 2  # Minimum number of connections per node
MAX_CONNECTIONS = 3  # Maximum number of connections per node
MIN_COST = 1
MAX_COST = 10

class PerfectPathway:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(WINDOW_TITLE)
        self.root.geometry(WINDOW_SIZE)
        
        self.G: Optional[nx.Graph] = None
        self.home_node = "Home Node"
        self.destination_node: Optional[str] = None
        self.selected_role: Optional[str] = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome section
        welcome_label = ttk.Label(main_frame, text="Welcome to the game", font=TITLE_FONT)
        welcome_label.pack(pady=10)
        
        # Role selection section
        role_frame = ttk.LabelFrame(main_frame, text="Choose a Role", padding="10")
        role_frame.pack(fill=tk.X, pady=10)
        
        for role in ROLES:
            role_button = ttk.Button(role_frame, text=role, 
                                   command=lambda r=role: self.choose_role(r))
            role_button.pack(side=tk.LEFT, padx=5)
        
        self.role_label = ttk.Label(main_frame, text="Role selected: None", font=NORMAL_FONT)
        self.role_label.pack(pady=10)
        
        # Destination selection section
        dest_frame = ttk.LabelFrame(main_frame, text="Select Destination", padding="10")
        dest_frame.pack(fill=tk.X, pady=10)
        
        self.destination_label = ttk.Label(dest_frame, text="Destination selected: None", 
                                         font=NORMAL_FONT)
        self.destination_label.pack(pady=5)
        
        # Create buttons for each node type
        for node_type, nodes in NODE_TYPES.items():
            if node_type != "Home":  # Skip home node as it's not a destination
                type_frame = ttk.Frame(dest_frame)
                type_frame.pack(fill=tk.X, pady=5)
                ttk.Label(type_frame, text=f"{node_type}s:").pack(side=tk.LEFT)
                for node in nodes:
                    btn = ttk.Button(type_frame, text=node,
                                   command=lambda n=node: self.select_destination(n))
                    btn.pack(side=tk.LEFT, padx=5)
        
        # Simulation button
        self.sim_button = ttk.Button(main_frame, text="Start Simulation",
                                   command=self.start_simulation)
        self.sim_button.pack(pady=10)
        
        # Exit button
        exit_button = ttk.Button(main_frame, text="Exit", command=self.root.destroy)
        exit_button.pack(pady=10)

    def choose_role(self, role: str):
        self.selected_role = role
        self.role_label.config(text=f"Role selected: {role}")
        self.initialize_army_graph()

    def get_node_connections(self, node: str, edges: List[Tuple[str, str]]) -> int:
        """Get the number of connections for a given node."""
        return sum(1 for edge in edges if node in edge)

    def generate_random_connections(self) -> List[Tuple[str, str]]:
        """Generate random connections between nodes ensuring the graph is connected."""
        all_nodes = [node for nodes in NODE_TYPES.values() for node in nodes]
        edges = []
        connected_nodes = {self.home_node}  # Start with home node
        
        # First, ensure all nodes are connected to the graph
        unconnected_nodes = set(all_nodes) - connected_nodes
        while unconnected_nodes:
            node = random.choice(list(unconnected_nodes))
            # Find a connected node that hasn't reached its maximum connections
            available_connected = [n for n in connected_nodes 
                                if self.get_node_connections(n, edges) < MAX_CONNECTIONS]
            if not available_connected:
                # If no available nodes, start over
                return self.generate_random_connections()
            connected_to = random.choice(available_connected)
            edges.append((connected_to, node))
            connected_nodes.add(node)
            unconnected_nodes.remove(node)
        
        # Add additional random connections
        for node in all_nodes:
            current_connections = self.get_node_connections(node, edges)
            if current_connections < MIN_CONNECTIONS:
                # Need to add more connections
                attempts = 0
                while current_connections < MIN_CONNECTIONS and attempts < 100:
                    other_node = random.choice(all_nodes)
                    if (other_node != node and 
                        self.get_node_connections(other_node, edges) < MAX_CONNECTIONS and
                        (node, other_node) not in edges and 
                        (other_node, node) not in edges):
                        edges.append((node, other_node))
                        current_connections += 1
                    attempts += 1
                
                # If we couldn't add enough connections, start over
                if current_connections < MIN_CONNECTIONS:
                    return self.generate_random_connections()
        
        return edges

    def initialize_army_graph(self):
        try:
            self.G = nx.Graph()
            all_nodes = [node for nodes in NODE_TYPES.values() for node in nodes]
            self.G.add_nodes_from(all_nodes)
            
            # Generate random connections
            edges = self.generate_random_connections()
            
            # Add edges with random costs
            for edge in edges:
                self.G.add_edge(edge[0], edge[1], cost=random.randint(MIN_COST, MAX_COST))
                
            # Verify the graph is connected
            if not nx.is_connected(self.G):
                messagebox.showwarning("Warning", "Generated graph is not fully connected. Regenerating...")
                self.initialize_army_graph()
                return
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to initialize graph: {str(e)}")

    def select_destination(self, node: str):
        self.destination_node = node
        self.destination_label.config(text=f"Destination selected: {node}")

    def start_simulation(self):
        if not self.G:
            messagebox.showwarning("Error", "Please select a role first.")
            return

        if not self.destination_node:
            messagebox.showwarning("Error", "Please select a destination node.")
            return

        try:
            path = nx.shortest_path(self.G, source=self.home_node,
                                  target=self.destination_node, weight='cost')
            
            result_message = f"{self.selected_role} is going to {self.destination_node} "
            result_message += f"through the following path: {' -> '.join(path)}\n"
            
            total_cost = sum(self.G[path[i]][path[i+1]]['cost'] 
                           for i in range(len(path)-1))
            result_message += f"Total Cost/Injuries: {total_cost}"

            # Create visualization
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(self.G, k=1, iterations=50)
            
            # Draw all nodes
            nx.draw_networkx_nodes(self.G, pos, node_color='lightgray',
                                 node_size=700)
            
            # Draw all edges in gray with their costs
            nx.draw_networkx_edges(self.G, pos, edge_color='gray', width=1)
            
            # Draw the selected path in blue with thicker lines
            path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges,
                                 edge_color='blue', width=3)
            
            # Draw all node labels
            nx.draw_networkx_labels(self.G, pos, font_weight='bold')
            
            # Draw edge labels for all edges
            edge_labels = {(u, v): d['cost'] for u, v, d in self.G.edges(data=True)}
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels,
                                       font_color='red', font_size=8)
            
            plt.title(f"Perfect Pathway - {self.selected_role}'s Route\n"
                     f"Selected path shown in blue, costs shown in red")
            plt.axis('off')
            plt.show()

            messagebox.showinfo("Simulation Result", result_message)
            
        except nx.NetworkXNoPath:
            messagebox.showerror("Error", "No valid path found to the destination!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PerfectPathway()
    app.run()
