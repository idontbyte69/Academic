# Perfect Pathway

A Python-based pathfinding simulation game that visualizes optimal routes between different locations in a network. The application uses graph theory concepts to find the shortest path while considering various roles and destinations.

## Features

- Interactive GUI built with Tkinter
- Multiple role selection (Army, Volunteer, Rescuer)
- Dynamic graph generation with random connections and costs
- Visual representation of the network using NetworkX and Matplotlib
- Shortest path calculation with cost optimization
- Real-time path visualization with color-coded routes

## Prerequisites

- Python 3.x
- Required Python packages:
  - tkinter
  - networkx
  - matplotlib
  - typing

## Installation



Install the required packages:
```bash
pip install networkx matplotlib
```

## Usage

1. Run the application:
```bash
python Perfect_pathway.py
```

2. Follow the on-screen instructions:
   - Select a role (Army, Volunteer, or Rescuer)
   - Choose a destination from the available nodes
   - Click "Start Simulation" to visualize the optimal path

## Node Types

The network consists of several types of nodes:
- Buildings (A, B, E, F, I, J)
- Junctions (C, G, K)
- Enemy Camps (D, H)
- Home Node (Starting point)

## Visualization

The application provides a visual representation of the network where:
- Gray lines represent possible connections
- Blue lines show the selected optimal path
- Red numbers indicate the cost/injury value of each connection
- Nodes are labeled with their respective names

## Technical Details

- The graph is randomly generated with 2-3 connections per node
- Connection costs range from 1 to 10
- The application ensures the graph remains fully connected
- Shortest path is calculated using NetworkX's built-in algorithms

## Error Handling

The application includes error handling for:
- Unconnected graphs
- Invalid paths
- Missing role selection
- Missing destination selection

## License

[Your chosen license]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 