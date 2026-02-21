import time
import psutil
import threading
from app.models.performance import PerformanceReport



#==========================================
# Performance Report Service
#==========================================

def generate_performance_report() -> PerformanceReport:
    """
    Service function to generate system performance metrics.
    Return metrics in required format.
    Metrics:
      - Response time (simulated here as elapsed time).
      - Memory usage (MB).
      - Threads used.
    """

    # Measure start time
    start_time = time.time()

    # Simulate some work (in real API, this would be request handling)
    time.sleep(0.01) # small delay to simulate processing

    # Measure elapsed time
    elapsed = time.time() - start_time
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed)) + f".{int((elapsed % 1) * 1000):03d}"

    # Memory usage in MB
    memory_usage = psutil.Process().memory_info().rss / (1024 * 1024)
    memory_str = f"{memory_usage:.2f} MB"

    # Thread count
    threads_count = threading.active_count()

    return PerformanceReport(
        time=formatted_time,
        memory=memory_str,
        threads=threads_count
    )