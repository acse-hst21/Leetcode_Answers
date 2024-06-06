class Solution:
    def minimumChairs(self, s: str) -> int:
        num_people_in_room = []
        current_num_people = 0
        
        for letter in s:
            if letter == 'E':
                current_num_people += 1
            else:
                current_num_people -= 1
            num_people_in_room.append(current_num_people)
        
        return max(num_people_in_room) 
