#Sum of squarea for 100 natural numbers
sum_sq = 0
summ = 0
for i in xrange(1, 101):
    sum_sq += i * i
    summ += i

square_sum = summ * summ
print square_sum - sum_sq
