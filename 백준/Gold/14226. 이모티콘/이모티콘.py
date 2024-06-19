from collections import deque

S = int(input())
queue = deque([[1, 0, 0]])

visited = [[False] * 1001 for _ in range(1001)]
visited[1][0]=True

while queue:
    screen, clipboard,cnt=queue.popleft()

    if screen==S:
        print(cnt)
        break
    for i in range(3):
        if i==0:
            new_clipboard,new_screen=screen,screen

        elif i==1:
            new_screen,new_clipboard=screen+clipboard,clipboard

        else:
            new_screen,new_clipboard=screen-1,clipboard

        if new_screen >= 1001 or new_screen < 0 or new_clipboard >= 1001 or new_clipboard < 0 or visited[new_screen][
            new_clipboard]:
            continue
        visited[new_screen][new_clipboard]=True
        queue.append([new_screen,new_clipboard,cnt+1])


