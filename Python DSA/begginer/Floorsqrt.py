def floorSqrt(n):
   guess = n//2
   epsilon=1e-30
   while True:
      new_guess = 0.5 * (guess + n / guess)
      if abs(new_guess - guess) < epsilon:
         print(new_guess)
         return round(new_guess)
      guess = new_guess
n = 77