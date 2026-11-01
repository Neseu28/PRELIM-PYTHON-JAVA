import unittest

PURPOSES = ("Enrollment", "Records", "Payment")
SERVICE_TYPES = ("regular", "priority")
COUNTER_COUNT = 2


def validate_request(purpose, service_type="regular"):
    """Raise ValueError unless the ticket request is valid."""
    if not isinstance(purpose, str) or purpose not in PURPOSES:
        raise ValueError("Purpose must be Enrollment, Records, or Payment.")
    if not isinstance(service_type, str) or service_type.lower() not in SERVICE_TYPES:
        raise ValueError("Service type must be regular or priority.")
    return purpose, service_type.lower()


def issue_ticket(purpose, service_type="regular"):
    """Create and return a ticket number; the manager supplies ticket storage."""
    global next_ticket_number, tickets
    purpose, service_type = validate_request(purpose, service_type)
    number = next_ticket_number
    tickets.append({
        "number": number,
        "purpose": purpose,
        "service_type": service_type,
        "status": "waiting",
    })
    next_ticket_number += 1
    return number


def issue_many(*requests):
    """Issue several (purpose, service_type) requests atomically."""
    validated = []
    for request in requests:
        if not isinstance(request, (tuple, list)) or len(request) != 2:
            raise ValueError("Each request must be a (purpose, service_type) pair.")
        validated.append(validate_request(request[0], request[1]))
    return [issue_ticket(purpose, service_type) for purpose, service_type in validated]


def next_ticket(waiting, priority_streak):
    """Return the eligible waiting ticket (not an index), or None if none wait."""
    regular = None
    priority = None
    for ticket in waiting:
        if ticket["status"] != "waiting":
            continue
        if ticket["service_type"] == "regular" and regular is None:
            regular = ticket
        elif ticket["service_type"] == "priority" and priority is None:
            priority = ticket
    if priority is not None and (regular is None or priority_streak < 2):
        return priority
    if regular is not None:
        return regular
    return priority


def report(**kwargs):
    """Print supplied report counts; unrelated metadata is ignored."""
    labels = {
        "waiting": "Waiting", "served": "Served", "cancelled": "Cancelled",
        "free_counters": "Free counters",
    }
    for key in ("waiting", "served", "cancelled", "free_counters"):
        if key in kwargs:
            print("{}: {}".format(labels[key], kwargs[key]))


class WaitingTicketIterator:
    """Live iterator: each next() checks current ticket statuses in list order."""
    def __init__(self, ticket_list):
        self.ticket_list = ticket_list
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.position < len(self.ticket_list):
            ticket = self.ticket_list[self.position]
            self.position += 1
            if ticket["status"] == "waiting":
                return ticket
        raise StopIteration


def find_ticket(number):
    for ticket in tickets:
        if ticket["number"] == number:
            return ticket
    return None


def waiting_tickets():
    return [ticket for ticket in tickets if ticket["status"] == "waiting"]


def call_next():
    global priority_streak
    free_counter = None
    for counter in counters:
        if counter["ticket"] is None:
            free_counter = counter
            break
    if free_counter is None:
        return None, "Both counters are busy. Complete a service before calling another ticket."

    chosen = next_ticket(waiting_tickets(), priority_streak)
    if chosen is None:
        return None, "There are no waiting tickets."
    chosen["status"] = "in service"
    free_counter["ticket"] = chosen["number"]
    if chosen["service_type"] == "priority":
        priority_streak += 1
    else:
        priority_streak = 0
    return chosen, "Counter {} is serving ticket #{} ({}).".format(
        free_counter["number"], chosen["number"], chosen["purpose"])


def complete_service(number):
    ticket = find_ticket(number)
    if ticket is None:
        return False, "No ticket #{} exists.".format(number)
    if ticket["status"] != "in service":
        return False, "Ticket #{} is not currently in service (status: {}).".format(
            number, ticket["status"])
    for counter in counters:
        if counter["ticket"] == number:
            counter["ticket"] = None
            break
    ticket["status"] = "served"
    completed_history.append(number)
    return True, "Ticket #{} completed; its counter is free.".format(number)


def cancel_ticket(number):
    ticket = find_ticket(number)
    if ticket is None:
        return False, "No ticket #{} exists.".format(number)
    if ticket["status"] != "waiting":
        return False, "Only a waiting ticket can be cancelled. Ticket #{} is {}.".format(
            number, ticket["status"])
    ticket["status"] = "cancelled"
    return True, "Ticket #{} cancelled.".format(number)


def estimate_position(number):
    """Estimate call position by simulating all currently waiting tickets."""
    target = find_ticket(number)
    if target is None or target["status"] != "waiting":
        return None
    simulated = [dict(ticket) for ticket in tickets]
    streak = priority_streak
    position = 0
    while True:
        chosen = next_ticket(simulated, streak)
        if chosen is None:
            return None
        position += 1
        if chosen["number"] == number:
            return position
        chosen["status"] = "in service"
        if chosen["service_type"] == "priority":
            streak += 1
        else:
            streak = 0


def show_waiting():
    iterator = WaitingTicketIterator(tickets)
    found = False
    for position in range(len(tickets)):
        try:
            ticket = next(iterator)
        except StopIteration:
            break
        found = True
        estimate = estimate_position(ticket["number"])
        print("{}. #{} | {} | {} | estimated call position: {}".format(
            position + 1, ticket["number"], ticket["service_type"],
            ticket["purpose"], estimate))
    if not found:
        print("No waiting tickets.")


def show_counters_and_history():
    for counter in counters:
        if counter["ticket"] is None:
            print("Counter {}: free".format(counter["number"]))
        else:
            print("Counter {}: serving ticket #{}".format(
                counter["number"], counter["ticket"]))
    if completed_history:
        print("Completed history: {}".format(", ".join(
            "#{}".format(number) for number in completed_history)))
    else:
        print("Completed history: empty")


def show_summary():
    statuses = [ticket["status"] for ticket in tickets]
    report(
        waiting=statuses.count("waiting"),
        served=statuses.count("served"),
        cancelled=statuses.count("cancelled"),
        free_counters=sum(1 for counter in counters if counter["ticket"] is None),
        note="extra metadata does not affect queue decisions",
    )
    print("Total tickets issued: {}".format(len(tickets)))


def read_ticket_number(action):
    raw = input("Ticket number to {}: ".format(action)).strip()
    try:
        return int(raw)
    except ValueError:
        print("Please enter a numeric ticket number.")
        return None


def menu():
    while True:
        print("\nCampus Service Queue Manager")
        print("1. Issue a ticket")
        print("2. Call the next ticket")
        print("3. Complete a service")
        print("4. Cancel a waiting ticket")
        print("5. Show waiting tickets")
        print("6. Show counter status and completed history")
        print("7. Show a summary report")
        print("8. Exit")
        choice = input("Choose 1-8: ").strip()

        if choice == "1":
            purpose = input("Purpose (Enrollment, Records, Payment): ").strip()
            service_type = input("Service type (regular/priority): ").strip().lower()
            try:
                number = issue_ticket(purpose, service_type)
                print("Issued {} ticket #{} for {}.".format(
                    service_type, number, purpose))
                print("Estimated call position: {}".format(estimate_position(number)))
            except ValueError as error:
                print("Invalid ticket: {}".format(error))
        elif choice == "2":
            ticket, message = call_next()
            print(message)
        elif choice == "3":
            number = read_ticket_number("complete")
            if number is not None:
                success, message = complete_service(number)
                print(message)
        elif choice == "4":
            number = read_ticket_number("cancel")
            if number is not None:
                success, message = cancel_ticket(number)
                print(message)
        elif choice == "5":
            show_waiting()
        elif choice == "6":
            show_counters_and_history()
        elif choice == "7":
            show_summary()
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid menu choice. Enter a number from 1 to 8.")


tickets = []
completed_history = []
next_ticket_number = 1
priority_streak = 0
counters = [{"number": number, "ticket": None}
            for number in range(1, COUNTER_COUNT + 1)]

class QueueManagerTests(unittest.TestCase):
    """Small regression suite for the queue's core rules."""
    def setUp(self):
        global tickets, completed_history, next_ticket_number
        global priority_streak, counters
        tickets = []
        completed_history = []
        next_ticket_number = 1
        priority_streak = 0
        counters = [{"number": number, "ticket": None}
                    for number in range(1, COUNTER_COUNT + 1)]

    def test_ticket_numbers_increase(self):
        self.assertEqual(issue_ticket("Records"), 1)
        cancel_ticket(1)
        self.assertEqual(issue_ticket("Payment", "priority"), 2)

    def test_fairness_serves_regular_after_two_priorities(self):
        issue_ticket("Enrollment", "priority")
        issue_ticket("Records", "priority")
        issue_ticket("Payment", "regular")
        first, _ = call_next()
        second, _ = call_next()
        self.assertEqual([first["service_type"], second["service_type"]],
                         ["priority", "priority"])
        complete_service(first["number"])
        complete_service(second["number"])
        third, _ = call_next()
        self.assertEqual(third["service_type"], "regular")

    def test_both_counters_busy(self):
        issue_ticket("Enrollment")
        issue_ticket("Records")
        issue_ticket("Payment")
        call_next()
        call_next()
        ticket, message = call_next()
        self.assertIsNone(ticket)
        self.assertIn("Both counters are busy", message)

    def test_cancelled_ticket_is_skipped(self):
        cancelled = issue_ticket("Enrollment")
        waiting = issue_ticket("Records")
        cancel_ticket(cancelled)
        called, _ = call_next()
        self.assertEqual(called["number"], waiting)

    def test_iterator_exhaustion(self):
        issue_ticket("Enrollment")
        iterator = WaitingTicketIterator(tickets)
        self.assertEqual(next(iterator)["number"], 1)
        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    menu()
