def calculate_cost(history):
    CPU_UNITS = 2
    RUNTIME_MIN = 5
    COST_PER_CPU = 0.0008

    cost = CPU_UNITS * RUNTIME_MIN * COST_PER_CPU

    if history:
        avg_cost = sum(h["cost"] for h in history) / len(history)
    else:
        avg_cost = cost

    cost_score = cost / (avg_cost + 1e-5)

    return cost, cost_score
