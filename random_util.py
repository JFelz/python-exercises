user_data = {
    "name": {
        "first_name": "Jovanni",
        "last_name": "Feliz"
    },
    "password": {
        "current": "LoROr788$!",
        "previous": ["sqVOwzOb8267#!", "XEeuFxo10350$!", ["n6K1234", "442356"]]
    },
    "email": "feliz.j@gmail.com",
}

print(user_data["name"]["last_name"])
print(user_data["password"]["previous"][1])
new_input = user_data["name"]["middle_name"] = "Dangerous"
print(user_data)
print(user_data["password"]["previous"][2][0])
