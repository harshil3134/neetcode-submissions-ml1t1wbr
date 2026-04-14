class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s=[]

        for num in asteroids:
            
                while(s and num<0<s[-1]):
                    # print("num",num,"arr",s)
                    # print('num',num,"s top",s[-1])
                    if abs(num)>abs(s[-1]):
                        # print('if tur')
                        s.pop()
                        continue
                    elif abs(num)==abs(s[-1]):
                        # print('elif tur')
                        s.pop()
                        break
                    else:
                       
                        break
                else:
                    s.append(num)
    
        return s