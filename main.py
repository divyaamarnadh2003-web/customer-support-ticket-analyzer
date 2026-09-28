from src.data_loader import load_tickets
from src.ticket_processor import (
    clean_tickets,
    create_ticket_objects,
    export_tickets
)
from src.analyzer import (
    average_resolution_time_by_category,
    most_common_issues,
    find_sla_breaches,
    find_overdue_tickets,
    agent_workload,
    tickets_by_customer_type
)
from src.report_generator import generate_summary_report


def main():
    file_path = "data/support_tickets.csv"

    # Load tickets from CSV
    tickets = load_tickets(file_path)

    # Validate and clean tickets
    valid_tickets, invalid_tickets = clean_tickets(tickets)

    # Convert valid dictionaries into Ticket objects
    ticket_objects = create_ticket_objects(valid_tickets)

    # Export processed tickets
    processed_file_path = "data/processed_tickets.csv"

    export_tickets(ticket_objects, processed_file_path)

    print("Processed tickets exported to:", processed_file_path)

    # Basic ticket statistics
    print("Total tickets:", len(tickets))
    print("Valid tickets:", len(valid_tickets))
    print("Invalid tickets:", len(invalid_tickets))

    # High-priority tickets
    high_priority_tickets = []

    for ticket in ticket_objects:
        if ticket.is_high_priority():
            high_priority_tickets.append(ticket)

    print("High-priority tickets:", len(high_priority_tickets))

    # Unresolved tickets
    unresolved_tickets = []

    for ticket in ticket_objects:
        if ticket.is_unresolved():
            unresolved_tickets.append(ticket)

    print("Unresolved tickets:", len(unresolved_tickets))

    # Average resolution time by category
    category_averages = average_resolution_time_by_category(ticket_objects)

    print("\nAverage resolution time by category:")

    for category, average_time in category_averages.items():
        print(f"{category}: {average_time:.2f} hours")

    # Most common customer issues
    common_issues = most_common_issues(ticket_objects)

    print("\nMost common customer issues:")

    for issue, count in common_issues:
        print(f"{issue}: {count}")

    # SLA-breached tickets
    sla_breaches = find_sla_breaches(ticket_objects)

    print("\nSLA-breached tickets:")

    for ticket in sla_breaches:
        print(
            f"{ticket.ticket_id} - "
            f"{ticket.priority} priority - "
            f"{ticket.calculate_resolution_time():.2f} hours"
        )



    # Overdue unresolved tickets
    overdue_tickets = find_overdue_tickets(ticket_objects)

    print("\nOverdue unresolved tickets:")

    for ticket in overdue_tickets:
        print(
            f"{ticket.ticket_id} - "
            f"{ticket.priority} priority"
        )

    print("Overdue unresolved tickets:", len(overdue_tickets))


    # Agent workload
    agent_counts = agent_workload(ticket_objects)

    print("\nAgent workload:")

    for agent, count in agent_counts:
        print(f"{agent}: {count} tickets")

    # Customer type analysis
    customer_counts = tickets_by_customer_type(ticket_objects)

    print("\nTickets by customer type:")

    for customer_type, count in customer_counts.items():
        print(f"{customer_type}: {count} tickets")

    # Generate management report
    report_file_path = "reports/summary_report.txt"

    generate_summary_report(
        total_tickets=len(tickets),
        valid_tickets=len(valid_tickets),
        invalid_tickets=len(invalid_tickets),
        high_priority_tickets=len(high_priority_tickets),
        unresolved_tickets=len(unresolved_tickets),
        overdue_tickets=len(overdue_tickets),
        category_averages=category_averages,
        common_issues=common_issues,
        sla_breaches=sla_breaches,
        agent_counts=agent_counts,
        customer_counts=customer_counts,
        file_path=report_file_path
    )

    print("Summary report generated at:", report_file_path)


if __name__ == "__main__":
    main()