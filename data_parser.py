lines = []

with open("master_output.txt", 'r') as f:
    lines = f.readlines()

x = 0
while x < len(lines):
    print(lines[x+1].replace('\n','')+', '+lines[x].replace('\n','')+', '+lines[x+2].replace('\n',''))
    x += 4
