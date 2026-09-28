def generate_summary_report(
    total_tickets,
    valid_tickets,
    invalid_tickets,
    high_priority_tickets,
    unresolved_tickets,
    overdue_tickets,
    category_averages,
    common_issues,
    sla_breaches,
    agent_counts,
    customer_counts,
    file_path
):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("CUSTOMER SUPPORT TICKET ANALYTICS REPORT\n")
        file.write("=" * 45 + "\n\n")

        file.write("TICKET SUMMARY\n")
        file.write("-" * 45 + "\n")
        file.write(f"Total tickets: {total_tickets}\n")
        file.write(f"Valid tickets: {valid_tickets}\n")
        file.write(f"Invalid tickets: {invalid_tickets}\n")
        file.write(f"High-priority tickets: {high_priority_tickets}\n")
        file.write(f"Unresolved tickets: {unresolved_tickets}\n")
        file.write(f"Overdue unresolved tickets: {overdue_tickets}\n\n")

        file.write("AVERAGE RESOLUTION TIME BY CATEGORY\n")
        file.write("-" * 45 + "\n")

        for category, average_time in category_averages.items():
            file.write(f"{category}: {average_time:.2f} hours\n")

        file.write("\nMOST COMMON CUSTOMER ISSUES\n")
        file.write("-" * 45 + "\n")

        for issue, count in common_issues:
            file.write(f"{issue}: {count}\n")

        file.write("\nSLA-BREACHED TICKETS\n")
        file.write("-" * 45 + "\n")

        for ticket in sla_breaches:
            resolution_time = ticket.calculate_resolution_time()

            file.write(
                f"{ticket.ticket_id} - "
                f"{ticket.priority} priority - "
                f"{resolution_time:.2f} hours\n"
            )

        file.write("\nAGENT WORKLOAD\n")
        file.write("-" * 45 + "\n")

        for agent, count in agent_counts:
            file.write(f"{agent}: {count} tickets\n")

        file.write("\nTICKETS BY CUSTOMER TYPE\n")
        file.write("-" * 45 + "\n")

        for customer_type, count in customer_counts.items():
            file.write(f"{customer_type}: {count} tickets\n")