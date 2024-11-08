import yaml


with open("./config.yaml", 'r') as f:
	cfg = yaml.load(f, Loader=yaml.Loader);

print(cfg)

control_bits = {}
for i in range(len(cfg['control_bits'])):
	control_bits[cfg['control_bits'][i]] = 1 << i
	print("{:016b}".format(control_bits[cfg['control_bits'][i]]))


rom = [0 for i in range(128)]

for key, inst in cfg['instructions'].items():
	for address, step in enumerate(inst['steps'], inst['addr'] << 3):
		command = 0
		for active_bit in step:
			print(active_bit, "{:016b}".format(control_bits[active_bit]))
			command = command | control_bits[active_bit]
		print(address)
		print("{:016b}".format(command), "{:06x}".format(command), command)

		rom[address+1] = command # th +1 is because my fetch instructions bleed into the ROM instructions

with open("f.bin", "w") as f:
	o = ""
	for i, a in enumerate(rom):
		o = o + " {:06x}".format(rom[i])
	f.write(o)

print("=========================================")
[print("{:016b} {:016b} {:016b}".format(rom[i], rom[i+1], rom[i+2])) for i in range(0, len(rom)-3, 3)]
print("=========================================")


