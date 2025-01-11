
capitals= {
    "France": "Paris",
    "Germany": "Berlin",
}

#nested list in dictionary
# trave_log={
#     "France": ["Paris","Lille","Dijon"],
#     "Germany": ["Stutgart","Berlin"],
# }

# print(trave_log["France"][1])

nested_list = ["A","B",["C","D"]]

print(nested_list[2][1])


trave_log={
    "France": {
               "cities_visited":["Paris","Lille","Dijon"],
               "total_visits":12
               },
    "Germany": {
               "cities_visited":["Stuttgart","Berlin"],
               "total_visits":5
               },
}

print(trave_log["France"]["cities_visited"][1])