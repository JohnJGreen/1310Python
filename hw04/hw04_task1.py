# John Green
# 1001011958
# 9/30/13
# In the table header, all column names are be centered.
# The data in the left column of the table are left alligned.
# The data in the center column of the table are centered.
# The data in the right column of the table are right alligned.
# Printed numbers in the table are floats.

print("Melting and Boiling Points of Alkanes:")

print("-"*60)

print("|{:^9s}|{:^24s}|{:^23s}|".format("Name","Melting Point (deg C)","Boiling Point (deg C)"))

print("-"*60)

print("|{:<9s}|{:^24.2f}|{:>23.2f}|".format("Methane",-162,-183))
print("|{:<9s}|{:^24.2f}|{:>23.2f}|".format("Ethane",-89,-172))
print("|{:<9s}|{:^24.2f}|{:>23.2f}|".format("Propane",-42,-188))
print("|{:<9s}|{:^24.2f}|{:>23.2f}|".format("Butane",-.5,-135))

print("-"*60)
