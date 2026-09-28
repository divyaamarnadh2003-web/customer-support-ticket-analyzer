# Customer Support Ticket Analytics System

A Python-based customer support ticket analytics system that processes support ticket data, validates and repairs records, calculates resolution metrics, identifies SLA breaches and overdue tickets, and generates operational reports.

## Features

- Load customer support tickets from CSV
- Validate ticket data
- Repair safely recoverable records
- Process tickets using Object-Oriented Programming
- Calculate ticket resolution time
- Identify high-priority tickets
- Identify unresolved tickets
- Identify overdue unresolved tickets
- Calculate average resolution time by category
- Find the most common customer issues
- Detect SLA-breached tickets
- Analyze support-agent workload
- Analyze tickets by customer type
- Export processed ticket data to CSV
- Generate an automated management summary report
- Includes automated unit tests

## Technologies

- Python 3
- CSV
- Object-Oriented Programming
- File Handling
- Exception Handling
- datetime
- collections
- unittest

## Project Structure

```text
customer-support-ticket-analyzer/
│
├── data/
│   └── support_tickets.csv
│
├── reports/
│
├── src/
│   ├── analyzer.py
│   ├── data_loader.py
│   ├── report_generator.py
│   ├── ticket.py
│   └── ticket_processor.py
│
├── tests/
│   └── test_analyzer.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md