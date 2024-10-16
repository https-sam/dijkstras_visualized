# Boulder Pathfinding Visualizer

This project visualizes the shortest path from South Boulder to North Boulder using real-world map data from OpenStreetMap (OSM). The Dijkstra's algorithm is used to compute the shortest path, and the path is visualized on an interactive map.

## Features

- Download real-world map data using OpenStreetMap (via `osmnx`).
- Find the shortest path between two locations (South Boulder and North Boulder) using Dijkstra's algorithm.
- Visualize the shortest path on a map using `matplotlib`.

## Prerequisites

Before running the project, ensure that you have the following installed:

- Python 3.8+

## Installation
```bash
pip install -r requirements.txt
```


## How to run the project
```bash
python visualize.py
```
This script will:
- Download map data for Boulder, Colorado.
- Find the shortest path from South Boulder to North Boulder using Dijkstra's algorithm.
- Visualize the shortest path on a map.