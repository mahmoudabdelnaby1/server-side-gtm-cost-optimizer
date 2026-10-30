"""
Server-Side GTM Cost Optimizer & Infrastructure Sizing Tool
Estimates Google Cloud Run / App Engine monthly costs for sGTM based on:
- Inbound monthly request volume
- Noise event pruning percentage (scroll, timer, engagement heartbeats)
- Peak throughput (requests per second)
- Minimum instance baseline (min 2 instances for high availability)
"""
import math
import json
import argparse
from typing import Dict, Any

# Cloud Run pricing baselines (approximate us-central1 / europe-west3)
CPU_HOUR_COST = 0.00002400 * 3600  # ~$0.0864 / vCPU hour
MEM_GB_HOUR_COST = 0.00000250 * 3600  # ~$0.009 / GB hour
EGRESS_PER_GB = 0.08  # Egress network cost
REQUESTS_PER_MILLION = 0.40

def calculate_sgtm_cost(monthly_requests: int, prune_rate: float = 0.35, min_instances: int = 2) -> Dict[str, Any]:
    # Pruned requests that never hit Cloud Run
    retained_requests = int(monthly_requests * (1.0 - prune_rate))
    pruned_requests = monthly_requests - retained_requests
    
    # Estimate Peak RPS (monthly requests / (30 days * 12 peak hours * 3600s) * burst factor 2.0)
    avg_rps = retained_requests / (30 * 24 * 3600)
    peak_rps = avg_rps * 3.5
    
    # 1 Cloud Run instance (1 vCPU, 0.5 GB) comfortably handles ~80-100 sGTM rps
    required_instances = max(min_instances, math.ceil(peak_rps / 80.0))
    
    # Active CPU/memory computation (assume instance active during peak hours, min instances 24/7)
    hours_in_month = 720
    instance_hours = required_instances * hours_in_month
    
    compute_cost = instance_hours * (CPU_HOUR_COST + (0.5 * MEM_GB_HOUR_COST))
    
    # Egress: average sGTM response payload ~1.5 KB
    total_egress_gb = (retained_requests * 1500) / (1024 ** 3)
    network_cost = total_egress_gb * EGRESS_PER_GB
    
    total_cost_optimized = round(compute_cost + network_cost, 2)
    
    # Unoptimized cost comparison (0% prune rate)
    unopt_instances = max(min_instances, math.ceil((avg_rps / (1.0 - prune_rate) * 3.5) / 80.0))
    unopt_compute = unopt_instances * hours_in_month * (CPU_HOUR_COST + (0.5 * MEM_GB_HOUR_COST))
    unopt_network = ((monthly_requests * 1500) / (1024 ** 3)) * EGRESS_PER_GB
    unopt_total = round(unopt_compute + unopt_network, 2)
    
    savings = round(unopt_total - total_cost_optimized, 2)
    
    return {
        "monthly_inbound_requests": monthly_requests,
        "prune_rate_pct": prune_rate * 100.0,
        "pruned_events_saved": pruned_requests,
        "retained_requests": retained_requests,
        "peak_rps": round(peak_rps, 1),
        "recommended_instances": required_instances,
        "monthly_cost_optimized_usd": total_cost_optimized,
        "monthly_cost_unoptimized_usd": unopt_total,
        "monthly_savings_usd": savings,
        "savings_percentage": round((savings / unopt_total) * 100.0 if unopt_total > 0 else 0, 1)
    }

def main():
    res = calculate_sgtm_cost(50_000_000, prune_rate=0.40)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
