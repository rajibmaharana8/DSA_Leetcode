class Solution(object):
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        seats = corridor.count('S')

        if seats == 0 or seats % 2 == 1:
            return 0
        
        ways = 1
        seat_count = 0
        plants_between_pairs = 0
        counting_plants = False
        
        for ch in corridor:
            if ch == 'S':
                seat_count += 1
                if seat_count % 2 == 0:
                    counting_plants = True
                else:
                    if counting_plants:
                        ways = (ways * (plants_between_pairs + 1)) % MOD
                        plants_between_pairs = 0
                        counting_plants = True
            else:
                if counting_plants and seat_count % 2 == 0:
                    plants_between_pairs += 1
        
        return ways