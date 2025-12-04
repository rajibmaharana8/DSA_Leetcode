class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        # Step 1: Remove cars that will never collide
        # Leading 'L' cars escape left, trailing 'R' cars escape right
        trimmed = directions.lstrip('L').rstrip('R')
        
        # Step 2: Count all moving cars in the middle
        # Every 'L' or 'R' in the middle will eventually collide
        collisions = sum(1 for c in trimmed if c != 'S')
        
        return collisions