title1 = "Exercise 1: Cost to operate one server"
print(title1)
print('-'*len(title1))

# Cost to operate one server per hour
cost_per_server_per_hour = 0.51

# Hours in a day and month
hours_in_day = 24
hours_in_month = 24 * 30

# Cost to operate one server per day
cost_per_server_per_day = cost_per_server_per_hour * hours_in_day
print("Cost to operate one server per day:", cost_per_server_per_day)

# Cost to operate one server per month
cost_per_server_per_month = cost_per_server_per_hour * hours_in_month
print("Cost to operate one server per month:", cost_per_server_per_month)

title2 = "Exercise 2: Cost to operate one server"
print(title2)
print('-'*len(title2))
# Cost to operate one server per day
cost_per_server_per_day = 10
print("Cost to operate one server per day:", cost_per_server_per_day)

# Cost to operate one server per month
days_in_month = 30
cost_per_server_per_month = cost_per_server_per_day * days_in_month
print("Cost to operate one server per month:", cost_per_server_per_month)

# Cost to operate twenty servers per day
num_servers = 20
cost_twenty_servers_per_day = cost_per_server_per_day * num_servers
print("Cost to operate twenty servers per day:", cost_twenty_servers_per_day)

# Cost to operate twenty servers per month
cost_twenty_servers_per_month = cost_per_server_per_month * num_servers
print("Cost to operate twenty servers per month:", cost_twenty_servers_per_month)

# Days to operate one server with $918
days_to_operate_one_server = 918 / cost_per_server_per_day
print("Days to operate one server with $918:", days_to_operate_one_server)