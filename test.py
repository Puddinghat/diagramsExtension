from diagrams import Cluster, Diagram
from customdiagrams.clusters import ServiceCluster

with Diagram("Clustered Web Services", show=False):
    ServiceCluster()