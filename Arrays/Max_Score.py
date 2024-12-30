class Solution:
    def max_score(self, points: list[int], power: int) -> int:

        points.sort()
        score = 0

        while points:
            print(f"point: {points[0]} , score: {score}")
            if points[0] <= power:
                power -= points[0]
                points.pop(0)
                score += 1

            elif(score >0 and len(points) > 1):
                power += points[len(points)-1]
                points.pop()
                score -= 1
            else:
                break
            
        return score


points=[1000,2000,300,400,500,]
power = 300

print(Solution().max_score(points,power))
