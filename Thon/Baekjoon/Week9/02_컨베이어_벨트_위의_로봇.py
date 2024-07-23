### 20055 - 컨베이어 벨트 위의 로봇
# 고민: 30분
# 코딩: 35분

import sys
# input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))

robot = [0] * N * 2 # robot 위치 인덱스

# 초기값 설정
stage = 1 # 최종 출력
robot_num = 1 # 올라가는 로봇 번호
robot_list = [] # 올라가 있는 로봇 리스트
robot_set = set()


# 반복
while True:
    
    # 1. 벨트 회전 (내구도 감소 X)
    s, r = belt.pop(), robot.pop()
    belt = [s] + belt
    robot = [r] + robot

    if robot[N - 1] != 0: # 내리는 위치
        robot_set -= {robot[N - 1]}
        robot[N - 1] = 0    
        
    robot_list = sorted(list(robot_set))

    # 2. 로봇 이동
    for n in robot_list:
        ind = robot.index(n)

        if ind != 2 * N - 1: # 맨 끝 인덱스가 아니면
            if belt[ind + 1] != 0 and robot[ind + 1] == 0: # 내구도가 0이 아니고, 로봇이 없으면
                robot[ind], robot[ind + 1] = robot[ind + 1], robot[ind]
                belt[ind + 1] -= 1 # 내구도 감소
                
        else: # 맨 끝 인덱스이면
            if belt[0] != 0 and robot[0] == 0:
                robot[0], robot[ind] = robot[ind], robot[0]
                belt[0] -= 1 # 내구도 감소

        if ind + 1 == N - 1: # 내리는 위치면
            robot[ind + 1] = 0
            robot_set -= {n}
            
    robot_list = sorted(list(robot_set))

    # 3. 로봇 올리기
    if robot[0] == 0 and belt[0] != 0:
        robot[0] = robot_num
        robot_list.append(robot_num)
        robot_set.add(robot_num)
        robot_num += 1
        belt[0] -= 1

    # 4. 종료 조건
    cnt = 0
    for n in belt:
        if n == 0:
            cnt += 1
    if cnt >= K:
        break

    stage += 1

print(stage)
        
### 답안 참고
# 인덱싱을 현명하게 쓰신 것 같은데, 제대로 읽어보지는 않음
# 

N, K = map(int, input().split())
arr = list(map(int, input().split()))
robots = [0] * len(arr)
start = 0
restart = len(arr)-1
end = N-1
cnt = 0
repetition = 0
# process 4
while cnt < K:
    repetition += 1

    # process 1: moving conveyor belt
    robots[end] = 0
    start -= 1
    end -= 1
    if start < 0:
        start = restart
    elif end < 0:
        end = restart
    # get off robot on the end
    # if robot[end]:
    robots[end] = 0

    # process 2: robot moving
    idx = end - 1
    if idx < 0:
        idx = restart
    while idx != start:
        if robots[idx] == 1:
            moved_robot = idx + 1
            if moved_robot > restart:
                moved_robot = 0

            if robots[moved_robot] == 0 and arr[moved_robot]:
                arr[moved_robot] -= 1
                if arr[moved_robot] == 0:
                    cnt += 1
                robots[idx] = 0
                robots[moved_robot] = 1
        idx -= 1
        if idx < 0:
            idx = restart

    # process 3: input robot
    if arr[start] != 0:
        arr[start] -= 1
        robots[start] = 1
        if arr[start] == 0:
            cnt += 1

print(repetition)
