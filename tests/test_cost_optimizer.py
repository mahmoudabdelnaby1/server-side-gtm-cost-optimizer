"""
Unit tests for sGTM Cost Optimizer
"""
import unittest
from scripts.estimate_sgtm_cost import calculate_sgtm_cost

class TestSGtmCost(unittest.TestCase):
    def test_cost_calculation_positive_savings(self):
        res = calculate_sgtm_cost(10_000_000, prune_rate=0.30)
        self.assertGreater(res["monthly_cost_unoptimized_usd"], res["monthly_cost_optimized_usd"])
        self.assertGreater(res["monthly_savings_usd"], 0)
        self.assertGreaterEqual(res["recommended_instances"], 2)

    def test_zero_prune_rate(self):
        res = calculate_sgtm_cost(5_000_000, prune_rate=0.0)
        self.assertEqual(res["monthly_savings_usd"], 0.0)

if __name__ == "__main__":
    unittest.main()
