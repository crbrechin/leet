class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourHand = (hour % 12 + minutes / 60) * 30
        minuteHand = minutes * 6

        angle = min(abs(minuteHand - hourHand), abs(hourHand - minuteHand)) 

        # print(f'{hourHand}deg, {minuteHand}deg, {angle}')
        
        return min(angle, 360 - angle)
