import math

def normal_cdf(x, mean, std_dev):
	return 0.5 * (1 + math.erf((x - mean)/(math.sqrt(2) * std_dev)))

max_weight = float(raw_input())
boxes = float(raw_input())
single_mean = float(raw_input())
std_dev = float(raw_input())

print round(normal_cdf(max_weight, single_mean*boxes, std_dev*math.sqrt(boxes)),4)
