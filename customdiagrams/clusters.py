from diagrams import Cluster, Diagram
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Prometheus
from customicons.tools import Opensearch

def ServiceCluster():
    with Cluster("ServiceCluster") as ret:
        with Cluster("Observability"):
            with Cluster("Metrics"):
                prometheus = Prometheus("Prometheus")
            with Cluster("Logging"):
                fluentbit = Fluentd("Fluentbit")
                fluentd = Fluentd("Central fluentd")
                elastic = Opensearch("Opensearch")
                fluentbit >> fluentd >> elastic
    return ret