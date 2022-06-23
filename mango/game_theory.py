def risk_load_multiplier(
        return_on_marginal_surplus: float,
        standard_normal_multiplier: float
) -> float:

    y = return_on_marginal_surplus
    z = standard_normal_multiplier

    res = y * z / (1 + y)

    return res