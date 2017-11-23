



def main(test):
  stair = [0] * 20
  def stair_case(n):
    if n<0:
        return 0
    if n==0:
        return 1
    if stair[n] == 0:
      stair[n] = stair_case(n-1) + stair_case(n-2) + stair_case(n-3)
    return stair[n]
  print(stair_case(test))




if __name__ == "__main__":
    main(1)
    main(2)
    main(3)
    main(4)


