class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]

        for i in operations:
            if i not in ['+',"D","C"]:
                score.append(int(i))
            elif i=="+" :
                top1=score[-1] if score[-1] else 0
                top2=score[-2] if score[-2] else 0
                score.append(top1+top2)
            elif i=="D":
                top1=score[-1] if score[-1] else 0
                score.append(top1*2)
            elif i=="C":
                score.pop()

        return sum(score)