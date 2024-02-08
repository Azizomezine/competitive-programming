if __name__ == '__main__':
    sheet=[]
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        
        sheet.append([name,grade])

second_highest = sorted(list(set([grade for name, grade in sheet])))[1]
print('\n'.join([a for a,b in sorted(sheet) if b == second_highest]))