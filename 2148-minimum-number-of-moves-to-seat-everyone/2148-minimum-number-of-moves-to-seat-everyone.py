class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        print(seats)
        moves=0
        for i in range(len(seats)):
            moves+=max(seats[i],students[i])-min(seats[i],students[i])
        return moves

        