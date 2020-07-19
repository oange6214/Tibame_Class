import prettytable

t = prettytable.PrettyTable(["Id", "Title"], encoding="utf8")

# t.add_row(["1", "AAA"])
# t.add_row(["2", "BBB"])
# t.add_row(["3", "CCC"])

# 利用 for-in 建立 row 資料
for i in range(1, 10, 1):
	t.add_row([i, f"CCC{i}"])

t.align["ID"] = "r"
t.align["Title"] = "r"

print(t)