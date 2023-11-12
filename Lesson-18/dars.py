import os

if not os.path.exists('ketmonbek.txt'):
    with open('ketmonbek.txt', 'x'):
        pass

with open('ketmonbek.txt', 'w') as writer:
    writer.write("Bir narsalsar")

with open('ketmonbek.txt', 'a') as appender:
    appender.write("Bir narsalsar\n")
    appender.write("Bir narsalsar\n")
    appender.write("Bir narsalsar\n")
    appender.write("Bir narsalsar\n")
    appender.write("Bir narsalsar\n")

with open('ketmonbek.txt', 'r') as reader:
    data = reader.readlines()
    print(data)

