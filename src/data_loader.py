import csv


def load_tickets(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            tickets = list(reader)

        return tickets

    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []

    except PermissionError:
        print(f"Error: Permission denied - {file_path}")
        return []

    except Exception as error:
        print(f"Error while reading file: {error}")
        return []