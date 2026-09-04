from prettytable import PrettyTable 

table = PrettyTable(["City Name", "Area(kmsq)", "Population"])

table.add_row(["Adelaide",1295,1158259])
print(table)