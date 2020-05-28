# write your code here
for i in range(10):
    name = "file{}.txt".format(str(i + 1))
    with open(name, "w") as f:
        f.write(str(i + 1))