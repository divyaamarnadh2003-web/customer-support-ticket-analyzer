from datetime import datetime


class Ticket:
    def __init__(
        self,
        ticket_id,
        created_at,
        resolved_at,
        status,
        priority,
        category,
        issue_type,
        channel,
        customer_type,
        assigned_agent,
        description
    ):
        self.ticket_id = ticket_id
        self.created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M")
        self.resolved_at = (
            datetime.strptime(resolved_at, "%Y-%m-%d %H:%M")
            if resolved_at
            else None
        )
        self.status = status
        self.priority = priority
        self.category = category
        self.issue_type = issue_type
        self.channel = channel
        self.customer_type = customer_type
        self.assigned_agent = assigned_agent
        self.description = description

    def is_high_priority(self):
        return self.priority == "High"

    def is_unresolved(self):
        return self.resolved_at is None

    def calculate_resolution_time(self):
        if self.resolved_at is None:
            return None

        resolution_time = self.resolved_at - self.created_at

        return resolution_time.total_seconds() / 3600


    def get_sla_hours(self):
        sla_rules = {
            "High": 24,
            "Medium": 48,
            "Low": 72
        }

        return sla_rules.get(self.priority)

    
    def is_sla_breached(self):
        resolution_time = self.calculate_resolution_time()

        if resolution_time is None:
            return False

        sla_hours = self.get_sla_hours()

        return resolution_time > sla_hours


    def is_overdue(self, reference_time):
        if self.resolved_at is not None:
            return False

        ticket_age = reference_time - self.created_at
        age_in_hours = ticket_age.total_seconds() / 3600

        sla_hours = self.get_sla_hours()

        return age_in_hours > sla_hours    