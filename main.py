# This file is for strategy


from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):


        if self.intent is not None:
            return
       
        if self.kickoff_flag:
            self.set_intent(kickoff())
            print("kickoff")
            return
       
        d1 = abs(self.ball.location.y - self.foe_goal.location.y)
        d2 = abs(self.me.location.y - self.foe_goal.location.y)
        is_front_of_ball = d1 > d2


        available_boost = [boost for boost in self.boosts if boost.large and boost.active]


        closest_boost = None
        closest_distance = 1000
        for boost in available_boost:
            distance = (self.me.location - boost.location).magnitude()
            if closest_boost is None or distance < closest_distance:
                closest_boost = boost
                closest_distance = distance
                go = True


        if self.me.boost > 80:
            go = False


        if go == False:
            if is_front_of_ball == True:
                print("True")
                if d1 > 7000:
                    self.set_intent(short_shot(self.foe_goal.location))
                    print("atball")
                    return
                else:
                    self.set_intent(goto(self.friend_goal.location))
                    print("retreat")
                    return
           
        if is_front_of_ball == False:
            print("False")
            self.set_intent(short_shot(self.foe_goal.location))
            print("attack")
            return
   
        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            print("going for boost")
            return
       
        self.me.boost = boost
        print(boost)
