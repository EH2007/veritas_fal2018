{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n",
      "25\n"
     ]
    }
   ],
   "source": [
    "alist = [1,3,5,7,9]\n",
    "\n",
    "def listsum(a):\n",
    "  theSum = 0\n",
    "  for i in a:\n",
    "    theSum += i\n",
    "  return theSum\n",
    "\n",
    "print(listsum(alist))\n",
    "\n",
    "# 1 + [3,5,7,9]\n",
    "#     3 + [ 5, 7, 9]\n",
    "#         5 + [7, 9]\n",
    "#              7 + [9]\n",
    "# --------------------\n",
    "# 1 + 3 + 5 + 7 + 9\n",
    "             \n",
    "def listSum(a):\n",
    "  if len(a) == 1:\n",
    "    return a[0]\n",
    "  else:\n",
    "    return a[0] + listSum(a[1:])\n",
    "\n",
    "print(listSum(alist))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# For Problem 3 of USACO 2018 December Contest, Bronze: Back and Forth - Eugene Hwang 2/28/2019\n",
    "# http://usaco.org/index.php?page=viewproblem2&cpid=857"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
