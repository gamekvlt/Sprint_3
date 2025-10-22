types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}

tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}


def delete_duplicates(ticket_dict):
    for key in ticket_dict:
        ticket_dict[key] = list(set(ticket_dict[key]))  # убираем повторы внутри списка
    return ticket_dict


def get_tickets_by_type(types, tickets):
    tickets = delete_duplicates(tickets)
    used_tickets = []
    result = {}

    for key in types:
        unique_tickets = []
        for ticket in tickets[key]:
            if ticket not in used_tickets:
                unique_tickets.append(ticket)
                used_tickets.append(ticket)
        result[types[key]] = unique_tickets

    return result


tickets_by_type = get_tickets_by_type(types, tickets)
print(tickets_by_type)
