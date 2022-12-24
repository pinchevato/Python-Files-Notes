# Return 1st 3 characters of str repeated n times
# (if it's <3 char, just repeat those)
print("\n  front_times()")
def front_times(str, n):
  if len(str) < 3:
    out = n * str
  out = n * str[0:3]
  print(out)
front_times('bLergh',5)


# Return every other character from a string
print("\n  every_other()")
def every_other(str):
    out = ''
    for i in range(len(str)):
        if i % 2 == 0:
            out += str[i]
    print(out)
every_other('F1u2c3k4 5y4o_u*!')


# Return 1st char of str, then 1st n 2nd, then 1st 2nd 3rd etc
print("\n  str_derp()")
def str_derp(str):
  out = ''
  for i in range(len(str)):
    out += str[:i+1]
  print(out)
str_derp('Hey hey!')


# Return a count of how many times the last two char's of a
# str are repeated within the entire str
print("\n  last2()")
def last2(str):
  if len(str) < 2:
    return 0
  
  end = str[-2:]
  out = 0
  for i in range(len(str)-2):
    if str[i:i+2] == end:
      out += 1
  print(out)
last2('nz3aaanz4nz23231nz')


# Given an array of ints, return True if one of the
# first 4 elements in the array is a 9 (array length may be <4)
print("\n  front9()")
def front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  c = 0
  for i in range(end):
    if nums[i] == 9:
      c += 1
  print(c>0)
front9([2,1,3,9,3,4])


# Does [1,2,3] appears within the array? T or F?
print("\n  array123()")
def array123(nums):
  c = 0
  for i in range(len(nums)):
    if nums[i:i+3] == [1,2,3]:
      c += 1
  print(c>0)
array123([4,3,1,2,3,29384])


# How many positions do 2 str's contain the same length 2 substring
print("\n  string_match()")
def string_match(a, b):
  c=0
  shorty = min(len(a), len(b))
  for i in range(shorty - 1):
    if a[i:i+2] == b[i:i+2]:
      c += 1
  print(c)
string_match('awkward22','aw3wa4422')


# Return the number of times co*e appears in a string
print("\n  cound_co*e()")
def count_code(str):
  c = 0
  for i in range(len(str)-3):
    if str[i:i+2] == "co" and str[i+3] == "e":
      c += 1
  print(c)
count_code('co3ejfcode29')


# If one string appears at the end the other string,
# return True, not case sensitive
print("\n  end_other()")
def end_other(a, b):
  al = a.lower()
  bl = b.lower()
  if len(a) < len(b):
    short = al
    longg = bl
  else:
    short = bl
    longg = al
  if longg[-len(short):] == short:
    print(True)
  else:
    print(False)
end_other('tURd','298fkturD')


# Return True if string contains 'xyz' only if not preceded by '.'
# 'abxyzf' -> True; '32.xyzjj' -> False
print("\n  xyz_there()")
def xyz_there(str):
  if len(str) < 4 and str == 'xyz':
    print(True)
  elif str[0:3] == 'xyz':
    print(True)
  else:
    c = 0
# ***IMPORTANT NOTE: we range to only 3 under len(str)
# (cuz range excludes last #) but we can index to i+4
    for i in range(len(str)-3):
      if str[i] != '.' and str[i+1:i+4] == 'xyz':
        c += 1
    if c > 0:
      print(True)
    else:
      print(False)
xyz_there('333xyz22')


# Rotate elements left in an len3 array: [1,2,3] -> [2,3,1]
print("\n  rotate_left3()")
def rotate_left3(nums):
# ***IMPORTANT NOTE: we must use nums[0:1] instead of just
# nums[0] bc the 2nd one returns an int which cannot be
# concatenated whereas the 1st returns a list w one element
  print(nums[1:] + nums[0:1])
rotate_left3([6,7,8])


# "Centered Average" - ignoring highest and lowest values,
# return the average of the other values; if there are
# multiple copies of the highest or lowest number, ignore
# ONLY ONE of them
print("\n  centered_avg()")
def centered_average(nums):
  min = 1000
  max = -1000
  for i in range(len(nums)):
    if nums[i] > max:
      max = nums[i]
    if nums[i] < min:
      min = nums[i]
  print((sum(nums) - min - max) / (len(nums)-2))
centered_average([1,2,5,70,800,800,-2])


# Return the sum of an array of int's, excluding 13
# AND any # that may come after 13 in the array
print("\n  sum13()")
def sum13(nums):
  if nums == []:
    print(0)
  summ = 0
  for i in range(len(nums)):
    if nums[i] != 13:
      summ += nums[i]
    if i < len(nums)-1 and nums[i] == 13 and nums[i+1] != 13:
      summ -= nums[i+1]
  print(summ)
sum13([5,5,13,13,4,1])


# Return sum of all numbers in a list, excluding
# anything that's [6,... 7] (6 will always eventually
# be followed by a 7 for these inputs)
print("\n  sum67()")
def sum67(nums):
  summ = 0
  found6 = False
  for i in range(len(nums)):
    if nums[i] != 6 and found6 == False:
      summ += nums[i]
    if nums[i] == 6:
      found6 = True
    if nums[i] == 7:
      found6 = False
  print(summ)
sum67([1,6,398,7,3,6,1,1,7,5])


# Return true if array contains a 2 next to a 2
print("\n  has22()")
def has22(nums):
  a = False
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] ==2:
      a = True
  print(a)
has22([1,2,5,9])


# Do we have enough bricks to build the goal?
# Big bricks are 5 long and smalls are 1 long
print('\n  make_bricks()')
def make_bricks(small, big, goal):
  quo = goal // 5
  rem = goal % 5
  # if we don't have enough
  if big*5 + small < goal:
    print(False)
  # have enough bigs for quotient
  elif big >= quo:
    # have enough smalls for remainder
    if small >= rem:
      print(True)
  # don't have enough bigs for quotient
  elif big < quo:
    # have enough smalls for ALL the rest
    if small >= (goal - big*5):
      print(True)
make_bricks(2,1,8)


# Kinda like last one (but we're using chocolate)
# and we'r returning how many smalls we need if it's
# possible, and -1 if it isn't possible
print('\n  make_chocolate()')
def make_chocolate(small, big, goal):
  quo = goal // 5
  rem = goal % 5
  # if we don't have enough total bigs before OR AFTER division
  if (goal - quo*5 - small > 0) or (goal - big*5 - small > 0):
    print(-1)
  # have enough bigs for quotient
  elif big >= quo:
    # have enough smalls for remainder
    if small >= rem:
      print(rem)
  # don't have enough bigs for quotient
  elif big < quo:
    # have enough smalls for ALL the rest
    if small >= (goal - big*5):
      print(goal - (big*5))
make_chocolate(6,13,42)
