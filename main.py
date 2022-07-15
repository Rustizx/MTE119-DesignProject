# Tension will be +ve and Compression -ve
MAX_TENSION = 12000
MAX_COMPRESSION = -8000


class Member:
    def __init__(self, joints, magnitude):
        self.joints = joints
        self.magnitude = magnitude
        self.force = 0
        pass


class Joint:
    def __init__(self, x, y, numMembers, firstMember, secondMember, thirdMember):
        self.x = x
        self.y = y
        self.numMembers = numMembers
        self.firstMember = firstMember
        self.secondMember = secondMember
        self.thirdMember = thirdMember
        pass


class Bridge:
    def __init__(self):
        pass
