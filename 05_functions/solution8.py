def print_kwags(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_kwags(Power="lazer",Name="Shaktiman")
print_kwags(name="Shaktiman")
print_kwags(name="Shaktiman",Power="lazer",enemy = "Dr. Jackaal")