{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 사과나무 (BFS)\n",
    "\n",
    "![apple](./problem.png)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: ''",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 5\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[39m# 직접 풀어보기 \u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[39m# BFS는 시작점에서 쫙 퍼지는 느낌이다 -> 시작점을 잘 선정하는게 중요하다\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[39mfrom\u001b[39;00m \u001b[39mcollections\u001b[39;00m \u001b[39mimport\u001b[39;00m deque\n\u001b[1;32m----> 5\u001b[0m N \u001b[39m=\u001b[39m \u001b[39mint\u001b[39;49m(\u001b[39minput\u001b[39;49m())\n\u001b[0;32m      7\u001b[0m dQ \u001b[39m=\u001b[39m deque()\n\u001b[0;32m      8\u001b[0m dQ\u001b[39m.\u001b[39mappend\n",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: ''"
     ]
    }
   ],
   "source": [
    "# 직접 풀어보기 \n",
    "# BFS는 시작점에서 쫙 퍼지는 느낌이다 -> 시작점을 잘 선정하는게 중요하다\n",
    "\n",
    "from collections import deque\n",
    "N = int(input())\n",
    "dx = [-1,0,1,0]\n",
    "dy = [0,1,0,-1]\n",
    "\n",
    "a = [list(map(int, input().split())) for _ in range(N)]\n",
    "ch = [[0] * N for _ in range(N)]\n",
    "ch[N//2][N//2] = 1\n",
    "sum = sum + a[N//2][N//2]\n",
    "sum = 0\n",
    "\n",
    "dQ = deque()\n",
    "dQ.append((N//2, N//2))\n",
    "L = 0 # Level\n",
    "\n",
    "while True:\n",
    "    if L == N//2:\n",
    "        break\n",
    "    size = len(dQ) # 1이겠지\n",
    "    for i in range(size): # Level 탐색\n",
    "        tmp = dQ.popleft() # 여기서 하나가 나오면 무조건 4개를 돌아야함\n",
    "        for j in range(4):\n",
    "            x = tmp[0] + dx[j]\n",
    "            y = tmp[1] + dy[j]\n",
    "            if ch[x][y] != 1:\n",
    "                sum = sum + a[x][y]\n",
    "                ch[x][y] = 1\n",
    "                dQ.append((x,y))\n",
    "    L = L + 1\n",
    "print(sum)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0, 0, 0], [0, 0, 0], [0, 0, 0]]\n",
      "0 0 0 \n",
      "0 0 0 \n",
      "0 0 0 \n"
     ]
    }
   ],
   "source": [
    "# 그 전에 2차원 리스트 생성과 접근\n",
    "\n",
    "a = [[0] *3 for _ in range(3)]\n",
    "print(a) # 이렇게 하면 3행 3열 행렬이 만들어짐\n",
    "a[0][1]\n",
    "\n",
    "for x in a:\n",
    "    for y in x:\n",
    "        print(y, end = ' ')\n",
    "    print() # 이거면 충분함"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.0"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
