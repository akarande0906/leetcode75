'''
LC 489. Robot Room Cleaner: 
You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.
The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.
You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.
When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.
Design an algorithm to clean the entire room using the following APIs:
'''
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Four directions where the robot can go from one cell
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        visited = set()

        def go_back():
            # Go back one cell and face the same way
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        def backtrack(cell = (0,0), d = 0):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                # Calculate the next direction - always start with the same direction as the previous one - i.e. move in the same path
                new_d = (d + i) % 4 
                next_position = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])
                if next_position not in visited and robot.move():
                    # Move only if it has not been visited before and the robot can move - not edge and no obstacle
                    backtrack(next_position, new_d)
                    # Once visited go back to previous cell - backtrack
                    go_back()
                # Finally move right 
                robot.turnRight()

        backtrack() # First cell is considered to be (0,0) since we dont know the exact position. Everything else is relative
        '''
        TC: O(N-M) where N is number of cells and M is number of obstacles -> Totally 4(N-M) operations
        SC: O(N-M) 
        '''
                
