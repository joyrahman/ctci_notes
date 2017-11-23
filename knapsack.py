def knapsack_01(values, weights, total_weight):
  total_items = len(weights)
  rows = total_items + 1
  cols = total_weight  + 1 

  T  = [[ 0 for _ in xrange(cols)] for _ in xrange(rows)]

  for i in range(1, rows):
    for j in range(1,cols):
      if j < weights[i-1] :
        T[i][j] = T[i-1][j]
      else:
        #pick the item: value of item + T[prev_row][total - value of item]
        # or don't pick: T[prev_row] [total]
        T[i][j] = max( values[i-1] + T[i-1][j-weights[i-1]] , T[i-1][j] )
  return T[rows -1][cols-1]


if __name__ == "__main__":
  total_weight = 7 
  weights = [1, 3, 4, 5]
  values = [1, 4, 5, 7]
  expected = 9
  print(knapsack_01(values, weights, total_weight))
