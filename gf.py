import random

num_of_node = 100000

gf = open("go_100000_visualizater.txt", 'w')
gf.write('t # GO \n')

for i in range(num_of_node):
    gf.write('an ' + '"' + str(i) + '" label: "' + str(i) + '"' + '\n')

a = range(num_of_node)
random.shuffle(a)

previuous_root = -1

while len(a) != 0:
    root = a.pop()
    if previuous_root != -1:
        gf.write('ae "' + str(root) + ' ' + str(previuous_root) +
                 '" > "' + str(random.randint(0, num_of_node)) + '"' + '\n')
    for i in range(random.randint(2, 10)):
        if len(a) == 0:
            break
        gf.write('ae "' + str(root) + ' ' + str(a.pop()) +
                 '" > "' + str(random.randint(0, num_of_node)) + '"' + '\n')
    previuous_root = root
