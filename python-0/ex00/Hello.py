ft_list: list[str] = ["Hello", "tata!"]
ft_tuple: tuple[str] = ("Hello", "toto!")
ft_set: set[str] = {"Hello", "tutu!"}
ft_dict: dict[str:str] = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "Italy!")
ft_set = {"Hello", "Rome!"}
ft_dict["Hello"] = "42Rome!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)