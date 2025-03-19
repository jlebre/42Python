ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# List
ft_list[1] = "World!"

# Tuple
del ft_tuple
ft_tuple = ("Hello", "Portugal!")

# Set
ft_set.remove("tutu!")
ft_set.add("Lisboa!")

# Dict
ft_dict["Hello"] = "42Lisboa!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)