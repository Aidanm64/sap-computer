import yaml

prog = [0 for i in range(16)]

with open("./config.yaml", 'r') as f:
	cfg = yaml.load(f, Loader=yaml.Loader);


with open("sample.sap", 'r') as f:
	lines = f.readlines()

lines = [l.strip('\n') for l in lines]
i = 0
for line in lines:
	items = line.split(' ')
	if items[0] == '':
		continue
	elif items[0] == "set":
		prog[int(items[1])] = int(items[2])
	elif items[0] == "OUT":
		prog[i] = (int(cfg['instructions'][items[0]]['addr'])) << 4
		i += 1
	else:
		prog[i] = (int(cfg['instructions'][items[0]]['addr'])) << 4 | int(items[1])
		i += 1

print(prog)
[print("{:02x}".format(i)) for i in prog]