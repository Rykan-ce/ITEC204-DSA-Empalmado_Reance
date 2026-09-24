tickets = []

tickets.append({
    "id": "INC1392939",
    "bot": "BOT-Inventory",
    "description": "Failed to generate the daily report"
})

tickets.append({
    "id": "INC1392940",
    "bot": "BOT-Email",
    "description": "Failed to send the scheduled notification"
})

tickets.append({
    "id": "INC1392941",
    "bot": "BOT-DataSync",
    "description": "Encountered an error during data transfer"
})

tickets.append({
    "id": "INC1392942",
    "bot": "BOT-Invoice",
    "description": "Failed to process an invoice"
})

tickets.append({
    "id": "INC1392943",
    "bot": "BOT-Report",
    "description": "Failed to generate the weekly report"
})

tickets.append({
    "id": "INC1392944",
    "bot": "BOT-FileTransfer",
    "description": "Failed to upload the required file"
})

tickets.append({
    "id": "INC1392945",
    "bot": "BOT-DataEntry",
    "description": "Encountered an error while entering records"
})

tickets.append({
    "id": "INC1392946",
    "bot": "BOT-Backup",
    "description": "Failed to complete the scheduled backup"
})

tickets.append({
    "id": "INC1392947",
    "bot": "BOT-Validation",
    "description": "Failed to validate the submitted records"
})

tickets.append({
    "id": "INC1392948",
    "bot": "BOT-Notification",
    "description": "Failed to send the system alert"
})

def display_tickets():
    print("\n--- Active Incident Tickets ---")

    for ticket in tickets:
        print(f"ID: {ticket['id']}")
        print(f"Bot: {ticket['bot']}")
        print(f"Description: {ticket['description']}")
        print()

def add_ticket():
    incident_id = input("Enter Incident ID: ")
    bot = input("Enter Bot: ")
    description = input("Enter Short Description: ")

    new_ticket = {
        "id": incident_id,
        "bot": bot,
        "description": description
    }

    tickets.append(new_ticket)

    print("Incident ticket added successfully!")


def search_ticket():
    search_id = input("Enter Incident ID to search: ")

    for ticket in tickets:
        if ticket["id"] == search_id:
            print("\nTicket Found!")
            print(f"ID: {ticket['id']}")
            print(f"Bot: {ticket['bot']}")
            print(f"Description: {ticket['description']}")
            return

    print("Ticket not found.")

def remove_ticket():
    remove_id = input("Enter Incident ID to remove: ")

    for ticket in tickets:
        if ticket["id"] == remove_id:
            tickets.remove(ticket)
            print("Incident ticket removed successfully!")
            return

    print("Ticket not found.")

def count_tickets():
    print(f"Total active incident tickets: {len(tickets)}")


while True:
    print("\n=== IT Automation Incident Ticket Manager ===")
    print("1. Add New Incident Ticket")
    print("2. Display All Active Incident Tickets")
    print("3. Search Incident Ticket")
    print("4. Remove Resolved Incident Ticket")
    print("5. Display Total Active Incident Tickets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_ticket()

    elif choice == "2":
        display_tickets()

    elif choice == "3":
        search_ticket()

    elif choice == "4":
        remove_ticket()

    elif choice == "5":
        count_tickets()

    elif choice == "6":
        print("Thank you for using the Incident Ticket Manager!")
        break

    else:
        print("Invalid choice. Please try again.")
