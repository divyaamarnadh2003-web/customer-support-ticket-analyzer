import unittest

from src.ticket import Ticket
from src.analyzer import (
    average_resolution_time_by_category,
    most_common_issues,
    agent_workload,
    tickets_by_customer_type
)


class TestTicketAnalytics(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            Ticket(
                "TKT001",
                "2026-09-01 09:00",
                "2026-09-01 13:00",
                "Resolved",
                "High",
                "Technical",
                "Login Issue",
                "Email",
                "Premium",
                "Agent_01",
                "Unable to login"
            ),
            Ticket(
                "TKT002",
                "2026-09-01 10:00",
                "2026-09-02 10:00",
                "Resolved",
                "Medium",
                "Billing",
                "Payment Failure",
                "Phone",
                "Standard",
                "Agent_02",
                "Payment failed"
            )
        ]

    def test_resolution_time(self):
        self.assertEqual(
            self.tickets[0].calculate_resolution_time(),
            4.0
        )

    def test_high_priority(self):
        self.assertTrue(
            self.tickets[0].is_high_priority()
        )

    def test_unresolved(self):
        self.assertFalse(
            self.tickets[0].is_unresolved()
        )

    def test_category_average(self):
        result = average_resolution_time_by_category(self.tickets)

        self.assertEqual(result["Technical"], 4.0)
        self.assertEqual(result["Billing"], 24.0)

    def test_common_issues(self):
        result = most_common_issues(self.tickets)

        self.assertEqual(result[0], ("Login Issue", 1))

    def test_agent_workload(self):
        result = agent_workload(self.tickets)

        self.assertEqual(len(result), 2)

    def test_customer_type(self):
        result = tickets_by_customer_type(self.tickets)

        self.assertEqual(result["Premium"], 1)
        self.assertEqual(result["Standard"], 1)


if __name__ == "__main__":
    unittest.main()