from pydantic import BaseModel


#==========================================
# Performance Report Models
#==========================================
class PerformanceReport(BaseModel):
    time: str   # "HH:mm:ss.SSS"
    memory: str # "XXX.XX MB"
    threads: int