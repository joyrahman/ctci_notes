#!/bin/python

import sys

def calculate_longest_palindrome(s):
    T = [[0 for _ in xrange(len(s))] for _ in xrange(len(s))]

    for i in xrange(len(s)):
        T[i][i] = 1
    for l in xrange(2,len(s)+1):
        for i in xrange(0,len(s)-l+1):
            j = i+l - 1
            if (l ==2 and s[i]==s[j]):
                T[i][j] = 2
            elif s[i]==s[j]:
                T[i][j] =  2 + T[i+1][j-1]
            else:
                T[i][j] = max(T[i+1][j], T[i][j-1])

    return T[0][len(s)-1]



def find_parent(parent, item):
    if parent[item]==-1 or parent[item]==item:
        parent[item] = item
        return item
    else:
        return find_parent(parent, parent[item])

def print_parent(parent):
    for i in xrange(1,len(parent)):
        print "\t(",i,"->",parent[i],")"
def union(parent, x, y):
    x_set = find_parent(parent,x)
    y_set = find_parent(parent,y)
    if rank[x_set] >= rank[y_set]:
       parent[y_set]= x_set
       rank[x_set] += 1
    else:
       parent[x_set] = y_set
       rank[y_set] += 1

    

n,k,m = raw_input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
parent = (n+1) *[-1]
rank = (n+1) * [1]
for a0 in xrange(k):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    union(parent,x,y)

a = map(int, raw_input().strip().split(' '))

for i in xrange(len(a)):
    a[i] = find_parent(parent,a[i])

print calculate_longest_palindrome(a) 

