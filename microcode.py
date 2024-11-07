
import yaml

with open("./config.yaml", 'r') as f:
	cfg = yaml.load(f, Loader=yaml.Loader);

print(cfg)
def load_control_bits():
	control_bits = {}
	one = 1
	for i in range(len(cfg['control_bits'])):
		control_bits[cfg['control_bits'][i]] = one << i
	

load_control_bits()