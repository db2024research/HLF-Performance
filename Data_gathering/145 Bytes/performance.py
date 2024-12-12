class ModelParameters:
    def __init__(self):
        self.parameters = {
            "TR": "The set of transactions",
            "n": "The number of transactions",
            "TRi": "ith transaction",
            "Si": "Size of TRi in Byte",
            "CN": "Committing nodes set",
            "m": "The number of committing nodes",
            "CNk": "kth committing node",
            "T-VSk": "Time of ... CNk, the number of transactions that can store in a second",
            "T-MVk": "Time of ... CNk, the number of transactions that can store in a second",
            "T-DBk": "Time of ... CNk, the number of transactions that can store in a second",
            "BWk": "The bandwidth of CNk",
            "LS": "The maximum limit size of the block in byte",
            "LN": "The maximum limited number of transaction number existing in the block",
            "PCN": "The percentage of committing nodes that should store the block"
        }
        self.decision_variables = {
            "BSB": "The block size in byte",
            "BST": "The block size in the number of transactions",
            "xi": "1 iff TRi exists in the block, otherwise 0",
            "yk": "1 iff CNk can store the block in a second, otherwise 0",
            "STk": "The storing time of block by CNk"
        }
        self.constraints = {
            "(1)": "Throughput (Transaction per second) = max BST",
            "(2)": "BSB = Σ(xi * Si) for i = 1 to n",
            "(3)": "BST = Σxi for i = 1 to n",
            "(4)": "BSB <= LS",
            "(5)": "BST <= LN",
            "(6)": "1 <= Σxi <= n for i = 1 to n",
            "(7)": "STk = BST / Perfk + BSB / BWk for k = 1 to m",
            "(8)": "M(1 - yk) >= (STk - 1) for k = 1 to m",
            "(9)": "Σyk = m for k = 1 to m",
            "(10)": "xi ∈ {0, 1} for i = 1 to n",
            "(11)": "yk ∈ {0, 1} for k = 1 to m",
            "(12)": "STk ∈ R+ for k = 1 to m",
            "(13)": "STk - max{BST/Perfk, BSB/BWk} * yk ≤ 0 for k = 1 to m",
            "(14)": "Σyk ≥ PCN * m for k = 1 to m",
            "(15)": "Σxi ≥ 1 for i = 1 to n",
            "(16)": "BSB - max(Si) * xi ≤ LS",
            "(17)": "BST - xi ≤ LN"
        }

    def display_parameters(self):
        print("Table 1: Models Parameters/Variables and Their Description\n")
        print("Parameters:")
        for param, description in self.parameters.items():
            print(f"{param}: {description}")
    
    def display_decision_variables(self):
        print("\nDecision Variables:")
        for var, description in self.decision_variables.items():
            print(f"{var}: {description}")

    def display_constraints(self):
        print("\nConstraints and Equations (1 to 17)")
        for eq, description in self.constraints.items():
            print(f"{eq}: {description}")

# Example values for the variables
n = 5  # Number of transactions
m = 2  # Number of committing nodes

# Transaction sizes in bytes
Si = [115, 111, 111, 110, 111]

# Inclusion of transactions in the block (1 if included, 0 if not) shuld remove
xi = [1, 1, 1, 1, 1]

# Bandwidth of committing nodes Kbps
BWk = [400, 400]

# Performance of committing nodes(milliseconds) remove
Perfk = [19, 17]

# Storing time of block by CNk (milliseconds) remove
STk = [22, 22]  # To be calculated

# Limits
LS = 51000000   # Maximum limit size of the block in byte
LN = 10    # Maximum limited number of transactions in the block

# Inclusion of committing nodes (1 if can store, 0 if not)
yk = [1, 1, 1]

# Large number for M 
M = 1000000

# Percentage of committing nodes that should store the block
PCN = 0.75

# (1) Throughput (Transaction per second) = max BST (max written)
BST = sum(xi[:n])
throughput = BST  # Simplified assumption for max BST
print(f"Condition 1: Throughput (Transaction per second) = {throughput}")

# (2) BSB = Σ(xi * Si) for i = 1 to n
BSB = sum(xi[i] * Si[i] for i in range(n))
print(f"Condition 2: BSB = {BSB}")

# (3) BST = Σxi for i = 1 to n
BST = sum(xi[:n])
print(f"Condition 3: BST = {BST}")

# (4) BSB <= LS
condition_4 = BSB <= LS
print(f"Condition 4: (BSB <= LS): {condition_4}")

# (5) BST <= LN
condition_5 = BST <= LN
print(f"Condition 5: (BST <= LN): {condition_5}")

# (6) 1 <= Σxi <= n for i = 1 to n
condition_6 = 1 <= sum(xi[:n]) <= n
print(f"Condition 6: (1 <= Σxi <= n): {condition_6}")

# (7) STk = BST / Perfk + BSB / BWk for k = 1 to m
condition_7 = [(BST / Perfk[k]) + (BSB / BWk[k]) for k in range(m)]
print(f"Condition 7: STk = {condition_7}")

# (8) M(1 - yk) >= (STk - 1) for k = 1 to m
condition_8 = [M * (1 - yk[k]) >= (STk[k] - 1) for k in range(m)]
print(f"Condition 8: (M(1 - yk) >= (STk - 1)): {condition_8}")

# (9) Σyk = m for k = 1 to m
condition_9 = sum(yk[:m]) == m
print(f"Condition 9: (Σyk = m): {condition_9}")

# (10) xi ∈ {0, 1} for i = 1 to n
condition_10 = all(x in {0, 1} for x in xi)
print(f"Condition 10: (xi ∈ {{0, 1}}): {condition_10}")

# (11) yk ∈ {0, 1} for k = 1 to m
condition_11 = all(y in {0, 1} for y in yk)
print(f"Condition 11: (yk ∈ {{0, 1}}): {condition_11}")

# (12) STk ∈ R+ for k = 1 to m (non-negative real numbers)
condition_12 = all(st >= 0 for st in STk)
print(f"Condition 12: (STk ∈ R+): {condition_12}")

# (13) STk - max{BST/Perfk, BSB/BWk} * yk ≤ 0 for k = 1 to m
condition_13 = [STk[k] - max(BST / Perfk[k], BSB / BWk[k]) * yk[k] <= 0 for k in range(m)]
print(f"Condition 13: (STk - max{{BST/Perfk, BSB/BWk}} * yk ≤ 0): {condition_13}")

# (14) Σyk ≥ PCN * m for k = 1 to m
condition_14 = sum(yk[:m]) >= PCN * m
print(f"Condition 14: (Σyk ≥ PCN * m): {condition_14}")


