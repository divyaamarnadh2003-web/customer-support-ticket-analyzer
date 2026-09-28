from collections import defaultdict
from datetime import datetime


def average_resolution_time_by_category(tickets):
    category_times = defaultdict(list)

    for ticket in tickets:
        resolution_time = ticket.calculate_resolution_time()

        if resolution_time is not None:
            category_times[ticket.category].append(resolution_time)

    averages = {}

    for category, times in category_times.items():
        averages[category] = sum(times) / len(times)

    return averages


def most_common_issues(tickets):
    issue_counts = defaultdict(int)

    for ticket in tickets:
        issue_counts[ticket.issue_type] += 1

    return sorted(
        issue_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )


def find_sla_breaches(tickets):
    breached_tickets = []

    for ticket in tickets:
        if ticket.is_sla_breached():
            breached_tickets.append(ticket)

    return breached_tickets


def agent_workload(tickets):
    agent_counts = defaultdict(int)

    for ticket in tickets:
        agent_counts[ticket.assigned_agent] += 1

    return sorted(
        agent_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )


def tickets_by_customer_type(tickets):
    customer_counts = defaultdict(int)

    for ticket in tickets:
        customer_counts[ticket.customer_type] += 1

    return dict(customer_counts)


def find_overdue_tickets(tickets):
    overdue_tickets = []

    reference_time = datetime.now()

    for ticket in tickets:
        if ticket.is_overdue(reference_time):
            overdue_tickets.append(ticket)

    return overdue_tickets