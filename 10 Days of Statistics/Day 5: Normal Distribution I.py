import math

def erf(x, terms=70):
	sum = x
	neg = True
	fac_accum = 1;
	for term in xrange(1, terms):
		odd = term * 2 + 1
		fac_accum = term * fac_accum
		cur_term = math.pow(x, odd) / (odd * fac_accum)
		if neg:
			sum = sum - cur_term
		else:
			sum = sum + cur_term
		neg = not neg

	return sum * (2/math.sqrt(math.pi))

def normal_cdf(x, mean, std_dev):
	return 0.5 * (1 + erf((x - mean)/(math.sqrt(2) * std_dev)))

mean, std_dev = map(float, raw_input().split())
q1 = float(raw_input())
q2_lower, q2_upper = map(float, raw_input().split())
print round(normal_cdf(q1, mean, std_dev),3)
print round(normal_cdf(q2_upper, mean, std_dev) - normal_cdf(q2_lower, mean, std_dev), 3)
