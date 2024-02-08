if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up = sorted(set(arr),reverse=True)
    print(runner_up[1])
    