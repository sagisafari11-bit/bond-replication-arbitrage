# Bond Pricing and Arbitrage Analysis

A Python-based fixed-income analysis project that calculates bond prices, generates future cash flows, compares theoretical prices with market prices, and identifies the cheapest combination of available bonds to replicate a target cash-flow profile.

## Features

### 1. Bond Pricing

Calculates the theoretical price of a fixed-rate bond using its face value, annual coupon rate, maturity, and yield to maturity.

The model assumes semi-annual coupon payments and discounts each payment using the semi-annual yield.

### 2. Bond Cash-Flow Generation

Generates the cash flows associated with a bond, including:
- Periodic coupon payments.
- Repayment of face value at maturity.
- A semi-annual payment schedule.

### 3. Present Value Analysis

Calculates the present value of each future cash flow using a specified discount rate. The individual present values can then be summed to obtain the theoretical bond price.

The theoretical price is compared with the market price to classify the bond as overpriced, underpriced, or fairly priced.

### 4. Bond Replication and Arbitrage Analysis

The project includes an optimisation function that searches for a combination of available bonds capable of reproducing a target cash-flow profile.

The algorithm:
- Represents the available bonds as a cash-flow matrix.
- Examines different combinations of bonds.
- Uses symbolic equations and Lagrangian stationarity conditions.
- Enforces non-negative bond quantities.
- Checks optimality conditions, including complementary slackness.
- Calculates the cost of the replicating portfolio.
- Compares the replication cost with the target bond's market price to estimate the potential arbitrage opportunity.
The optimisation algorithm is implemented using Python, NumPy, and SymPy. It evaluates candidate portfolios and retains the lowest-cost feasible portfolio found, subject to the conditions implemented in the model.
#### Inputs
1. Individual Bond Pricing
- face_value: The bond's face value.
- coupun_rate: The annual coupon rate.
- maturity: The yield or discount rate used to calculate present value.
- years: The bond's maturity in years.
2. Cash-Flow and Present-Value Calculations
- face_value, coupun_rate, years: Used by bond_cashflow() to generate the bond's semiannual coupon payments and final principal repayment.
- cash_flow, maturity: Used by present_values() to calculate the present value of each cash flow using the discount rate.
3. Bond Portfolio Optimisation
- bonds: Cash flows of the available bonds at each payment date.
- prices: Market prices of the available bonds.
- target: Cash flows to be replicated.
- target_price: Market price of the target bond, used to compare against the minimum replication cost.
## Technologies Used

- Python
- NumPy
- SymPy
- Fixed-income valuation
- Present value calculations
- Cash-flow replication
- Constrained optimisation
- Arbitrage analysis

## How It Works

1. Define a bond's face value, coupon rate, maturity, and discount rate.
2. Calculate its theoretical price and future cash flows.
3. Discount the cash flows to their present values.
4. Compare the theoretical value with the observed market price.
5. Define a target cash-flow profile and a set of available bonds.
6. Search for a feasible portfolio that replicates the target cash flows at the lowest cost.
7. Compare the target market price with the replication cost.

## Running the Project

1. Install Python.
2. Install the required libraries:

   ```bash
   pip install numpy sympy
   ```
3. Open bond_price.py and edit the example input values to test different bonds, market prices, and target cash-flow profiles.
4. Save the code in a Python file, such as `bond_price.py`.
5. Run it

The script runs the calculations using your specified inputs and prints the results.

## Limitations

- Bond coupon payments are assumed to occur semi-annually.
- The model does not account for transaction costs, taxes, bid–ask spreads, or liquidity constraints.
- The arbitrage function searches subsets of the supplied bonds, so the computation can become expensive as the number of available bonds increases.
- Results depend on the supplied cash flows and market prices. A theoretical price difference does not necessarily represent a risk-free, executable arbitrage opportunity.

## Purpose

This project demonstrates the application of mathematical modelling and Python programming to fixed-income valuation, portfolio replication, and quantitative finance.
