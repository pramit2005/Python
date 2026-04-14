import stat_mod
l=list(map(int,input('Enter the data:').split()))
print(f'Mean:{stat_mod.mean(l)}')
print(f'Median:{stat_mod.median(l)}')
print(f'Mode:{stat_mod.mode(l)}')