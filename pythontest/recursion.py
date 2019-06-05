# 一条语句使用递归实现，找到列表的最大值
# 比如： l = [12,2,4,7,3,32]
def max(l):
    return l[0] if len(l)<=1 else (l[0]>max(l[1:]) and l[0] or max(l[1:]))
