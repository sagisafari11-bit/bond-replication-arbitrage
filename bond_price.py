import sympy as sp
import numpy as np
def bond_price(face_value,coupun_rate,maturity,years):
    coupon = face_value * coupun_rate / 2
    n=int(years)*2
    price=0
    for k in range(1,n+1):
        price+=coupon/((1+maturity/2)**k)
    price+=face_value/((1+maturity/2)**n)
    
    return price
def bond_cashflow(face_value,coupun_rate,years):
    coupun = face_value * coupun_rate / 2
    n=int(years)*2
    cash_flow=[]
    for k in range(1,n+1):
        cashflow=coupun
        if k==n:
            cashflow+=face_value
        cash_flow.append(cashflow)
    return cash_flow
def present_values(cash_flow, maturity):

    present_values = []

    for k in range(len(cash_flow)):

        pv = cash_flow[k] / (1 + maturity / 2) ** (k+1)

        present_values.append(pv)

    return present_values
#test
cash_flows = bond_cashflow(
    1000,0.05,2
)

pvs = present_values(
    cash_flows,
    0.06
)
#add your own value
market_price=1020
replication_price = sum(pvs)
difference = market_price - replication_price
if market_price > replication_price:
    print("Bond is overpriced")
    
elif market_price < replication_price:
    print("Bond is underpriced")
    
else:
    print("Bond is fairly priced")
#############################################################################################################################################################################################
#phase II What is the cheapest combination of available bonds that gives me the same cash flows as my target?
def bond_arbitrage(bonds, prices, target, target_price):

    A = np.array(bonds, dtype=float).T
    p = np.array(prices, dtype=float)
    T = np.array(target, dtype=float)

    n_bonds = len(prices)
    n_dates = len(target)

    best_cost = float("inf")
    best_x = None

    # We want to know which bonds are active
    # e.g. we have 3 bonds, so there are 8 possible combinations
    for mask in range(1, 2 ** n_bonds):

        # Decide which bonds are active
        # e.g. 001, 010, 011, 100, ...
        active = [
            i for i in range(n_bonds)
            if mask & (1 << i)
        ]

        # We need enough active bonds to reproduce all cash flows
        if len(active) < n_dates:
            continue

        A_active = A[:, active]
        p_active = p[active]

        # Lagrangian condition:
        #
        # p - A^T lambda = 0
        #
        # therefore:
        #
        # A^T lambda = p

        r = len(active)

        x = sp.symbols(f"x0:{r}")
        lam = sp.symbols(f"lam0:{n_dates}")

        objective = sum(
            p_active[i] * x[i]
            for i in range(r)
        )

        constraints = []

        for j in range(n_dates):

            cash_flow = sum(
                A_active[j, i] * x[i]
                for i in range(r)
            )

            constraints.append(
                T[j] - cash_flow
            )

        # Build Lagrangian
        L = objective

        for j in range(n_dates):
            L += lam[j] * constraints[j]

        # Take derivatives with respect to x
        derivative_equations = [
            sp.diff(L, x[i])
            for i in range(r)
        ]

        # Stationarity equations + cash-flow constraints
        equations = derivative_equations + constraints

        # Solve for x and lambda
        solution = sp.solve(
            equations,
            list(x) + list(lam),
            dict=True
        )

        if not solution:
            continue

        solution = solution[0]

        # Get the quantities of the active bonds
        x_active = np.array(
            [float(solution[xi]) for xi in x]
        )

        # x >= 0
        if np.any(x_active < -1e-10):
            continue

        # Get lambda values
        lambda_values = np.array(
            [float(solution[li]) for li in lam]
        )

        # Calculate mu
        mu = p - A.T @ lambda_values

        # mu >= 0
        if np.any(mu < -1e-10):
            continue

        # Put the active quantities into the full x vector
        x_full = np.zeros(n_bonds)

        for i, bond_index in enumerate(active):
            x_full[bond_index] = x_active[i]

        # Complementarity: mu_i * x_i = 0
        if np.any(np.abs(mu * x_full) > 1e-8):
            continue

        # Calculate investment cost
        cost = p @ x_full

        # Keep the cheapest feasible portfolio
        if cost < best_cost:
            best_cost = cost
            best_x = x_full

    if best_x is None:
        return None

    arbitrage = target_price - best_cost

    return best_x, best_cost, arbitrage
########################################################################################################################################################################################################
#TEST CASE
bonds = [
    [50, 1050, 0],     # Bond 0
    [20, 1020, 0],     # Bond 1
    [0, 40, 1040]      # Bond 2
]

prices = [
    980,    # Bond 0 price
    1000,   # Bond 1 price
    1010    # Bond 2 price
]

target = [
    70,     # Cash flow at date 1
    2110,   # Cash flow at date 2
    1040    # Cash flow at date 3
]

target_price = 3200
result = bond_arbitrage(
    bonds,
    prices,
    target,
    target_price
)

print(result)
