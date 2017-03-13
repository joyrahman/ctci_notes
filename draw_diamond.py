def drawDiamond(n):
    for i in xrange(1,n+1):
        #draw the diamond line
        print " " * (n-i),
        print "+" * (2*i-1)
    for i in xrange(n-1,0,-1):
        #draw the diamond line
        print " " * (n-i),
        print "+" * (2*i-1)




drawDiamond(6)
