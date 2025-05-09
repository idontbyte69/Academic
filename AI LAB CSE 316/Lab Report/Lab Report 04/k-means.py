import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import random
import math

class ClusterPoint:
    def __init__(self, x: float, y: float):
        self.coordinates = np.array([x, y])
        self.cluster_id = None
        self.distance_to_centroid = float('inf')

class Cluster:
    def __init__(self, centroid: np.ndarray, cluster_id: int):
        self.centroid = centroid
        self.id = cluster_id
        self.points: List[ClusterPoint] = []
        self.old_centroid = None
        self.silhouette_score = 0.0

class KMeansClusterer:
    def __init__(self, n_points: int = 100, n_clusters: int = 10, max_iterations: int = 100):
        self.n_points = n_points
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations
        self.points: List[ClusterPoint] = []
        self.clusters: List[Cluster] = []
        self.iteration_count = 0
        self.convergence_threshold = 0.001
        self.generate_data()
        
    def generate_data(self):
        centers = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(4)]
        points_per_center = self.n_points // 4
        
        for center in centers:
            for _ in range(points_per_center):
                x = random.gauss(center[0], 15)
                y = random.gauss(center[1], 15)
                x = max(0, min(100, x))
                y = max(0, min(100, y))
                self.points.append(ClusterPoint(x, y))
        
        for i in range(self.n_clusters):
            centroid = np.array([random.uniform(0, 100), random.uniform(0, 100)])
            self.clusters.append(Cluster(centroid, i))
            
        with open('data.txt', 'w') as f:
            f.write("Points:\n")
            for p in self.points:
                f.write(f"{p.coordinates[0]:.2f},{p.coordinates[1]:.2f}\n")
            f.write("Centroids:\n")
            for c in self.clusters:
                f.write(f"{c.centroid[0]:.2f},{c.centroid[1]:.2f}\n")

    def euclidean_distance(self, p1: np.ndarray, p2: np.ndarray) -> float:
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def assign_points_to_clusters(self):
        for point in self.points:
            min_distance = float('inf')
            for cluster in self.clusters:
                distance = self.euclidean_distance(point.coordinates, cluster.centroid)
                if distance < min_distance:
                    min_distance = distance
                    point.cluster_id = cluster.id
                    point.distance_to_centroid = distance

    def update_centroids(self) -> float:
        total_movement = 0.0
        for cluster in self.clusters:
            cluster.old_centroid = cluster.centroid.copy()
            cluster_points = [p for p in self.points if p.cluster_id == cluster.id]
            
            if cluster_points:
                new_centroid = np.mean([p.coordinates for p in cluster_points], axis=0)
                cluster.centroid = new_centroid
                total_movement += self.euclidean_distance(cluster.old_centroid, new_centroid)
        
        return total_movement / self.n_clusters

    def calculate_silhouette_score(self):
        for cluster in self.clusters:
            cluster_points = [p for p in self.points if p.cluster_id == cluster.id]
            if len(cluster_points) <= 1:
                continue
                
            for point in cluster_points:
                a = np.mean([self.euclidean_distance(point.coordinates, p.coordinates) 
                           for p in cluster_points if p != point])
                
                other_clusters = [c for c in self.clusters if c.id != cluster.id]
                b = min([np.mean([self.euclidean_distance(point.coordinates, p.coordinates) 
                                for p in self.points if p.cluster_id == c.id])
                        for c in other_clusters])
                
                point_silhouette = (b - a) / max(a, b)
                cluster.silhouette_score += point_silhouette
            
            cluster.silhouette_score /= len(cluster_points)

    def run(self):
        while self.iteration_count < self.max_iterations:
            self.iteration_count += 1
            self.assign_points_to_clusters()
            movement = self.update_centroids()
            
            if movement < self.convergence_threshold:
                break
        
        self.calculate_silhouette_score()
        self.visualize_results()

    def visualize_results(self):
        plt.figure(figsize=(12, 8))
        
        colors = plt.cm.rainbow(np.linspace(0, 1, self.n_clusters))
        for i, cluster in enumerate(self.clusters):
            cluster_points = [p for p in self.points if p.cluster_id == cluster.id]
            if cluster_points:
                x = [p.coordinates[0] for p in cluster_points]
                y = [p.coordinates[1] for p in cluster_points]
                plt.scatter(x, y, c=[colors[i]], label=f'Cluster {i+1}', alpha=0.6)
        
        for i, cluster in enumerate(self.clusters):
            plt.scatter(cluster.centroid[0], cluster.centroid[1], 
                       c=[colors[i]], marker='*', s=200, edgecolor='black')
        
        plt.title('K-Means Clustering Results')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        
        plt.savefig('output/clustering_result.png')
        plt.show()
        plt.close()

        print(f"\nClustering completed in {self.iteration_count} iterations")
        print("\nCluster Statistics:")
        for i, cluster in enumerate(self.clusters):
            cluster_points = [p for p in self.points if p.cluster_id == cluster.id]
            print(f"\nCluster {i+1}:")
            print(f"Centroid: ({cluster.centroid[0]:.2f}, {cluster.centroid[1]:.2f})")
            print(f"Number of points: {len(cluster_points)}")
            print(f"Silhouette score: {cluster.silhouette_score:.3f}")

def main():
    clusterer = KMeansClusterer(n_points=100, n_clusters=10)
    clusterer.run()

if __name__ == "__main__":
    main()