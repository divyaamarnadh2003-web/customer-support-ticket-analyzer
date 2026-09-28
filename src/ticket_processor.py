from src.ticket import Ticket
from datetime import datetime
import csv


def validate_ticket(ticket):
    required_fields = [
        "ticket_id",
        "created_at",
        "status",
        "priority",
        "category",
        "issue_type"
    ]

    for field in required_fields:
        if not ticket.get(field):
            return False

    try:
        datetime.strptime(ticket["created_at"], "%Y-%m-%d %H:%M")

        if ticket["resolved_at"]:
            datetime.strptime(ticket["resolved_at"], "%Y-%m-%d %H:%M")

    except ValueError:
        return False

    return True

def clean_tickets(tickets):
    valid_tickets = []
    invalid_tickets = []

    for ticket in tickets:
        repaired_ticket = repair_ticket(ticket)

        if validate_ticket(repaired_ticket):
            valid_tickets.append(repaired_ticket)
        else:
            invalid_tickets.append(repaired_ticket)

    return valid_tickets, invalid_tickets
def create_ticket_objects(valid_tickets):
    ticket_objects = []

    for ticket in valid_tickets:
        ticket_object = Ticket(
            ticket["ticket_id"],
            ticket["created_at"],
            ticket["resolved_at"],
            ticket["status"],
            ticket["priority"],
            ticket["category"],
            ticket["issue_type"],
            ticket["channel"],
            ticket["customer_type"],
            ticket["assigned_agent"],
            ticket["description"]
        )

        ticket_objects.append(ticket_object)

    return ticket_objects



def repair_ticket(ticket):
    if not ticket.get("category") and ticket.get("issue_type"):
        issue_category_map = {
            "Login Issue": "Technical",
            "Password Reset": "Technical",
            "Server Error": "Technical",
            "Payment Failure": "Billing",
            "Refund Request": "Billing",
            "Profile Update": "Account",
            "Email Change": "Account",
            "Delayed Delivery": "Delivery"
        }

        category = issue_category_map.get(ticket["issue_type"])

        if category:
            ticket["category"] = category

    return ticket


def export_tickets(tickets, file_path):
    if not tickets:
        return

    fieldnames = [
        "ticket_id",
        "created_at",
        "resolved_at",
        "status",
        "priority",
        "category",
        "issue_type",
        "channel",
        "customer_type",
        "assigned_agent",
        "description"
    ]

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for ticket in tickets:
            writer.writerow({
                "ticket_id": ticket.ticket_id,
                "created_at": ticket.created_at.strftime("%Y-%m-%d %H:%M"),
                "resolved_at": (
                    ticket.resolved_at.strftime("%Y-%m-%d %H:%M")
                    if ticket.resolved_at
                    else ""
                ),
                "status": ticket.status,
                "priority": ticket.priority,
                "category": ticket.category,
                "issue_type": ticket.issue_type,
                "channel": ticket.channel,
                "customer_type": ticket.customer_type,
                "assigned_agent": ticket.assigned_agent,
                "description": ticket.description
            })