
# name: Meytar Gil-Ron
# id:322876046
class Agent:
    def __init__(self,vals:list[int]):
        self.vals=vals

    def value(self,option:int):
        return self.vals[option]

def isParetoImprovement(agents:list[Agent],option1:int, option2:int)->bool:
    for i in range(len(agents)):
        if agents[i].value(option1)<agents[i].value(option2):
            return False
    return True

def isParetoOptimal(agents:list[Agent], option:int, allOptions:list[int])->bool:
    for i in range(len(allOptions)):
        if allOptions[i]!=option:
           if isParetoImprovement(agents,allOptions[i],option):
               return False
    return True

if __name__ == '__main__':
    ami= Agent([1,2,3,4,5])
    tami= Agent([3,1,2,5,4])
    rami= Agent([3,5,5,1,1])
    agents=[ami,tami,rami]
    allOptions=[0,1,2,3,4]

    print(isParetoOptimal(agents,2,allOptions))
    print(isParetoOptimal(agents, 1, allOptions))
