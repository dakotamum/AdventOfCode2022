global SUM_OF_THINGS_UNDER_LIMIT
SUM_OF_THINGS_UNDER_LIMIT = 0
global MIN_DUR_TO_DELETE
MIN_DUR_TO_DELETE = 70000000
global SPACE_NEEDED

class FileEntity:
    def __init__(self, entityName, fileSize = 0, parent=None):
        self.m_entityName = entityName
        self.m_fileSize = fileSize
        self.m_parent = parent
        self.m_children = []
    def AddChild(self, entityName, fileSize = 0):
        self.m_children.append(FileEntity(entityName, fileSize, self))
    def PrintTree(self, indentation = 0):
        numspace = (indentation) * 2
        space = ""
        for i in range(numspace):
            space += " "
        print(space + self.m_entityName)
        for child in self.m_children:
            if child.m_fileSize == 0:
                child.PrintTree(indentation + 1)
            else:
                numspaces = (indentation + 1) * 2
                spaces = ""
                for i in range(numspaces):
                    spaces += " "
                print(spaces + child.m_entityName)
    def getMemorySum(self, modGlob = False):
        global SUM_OF_THINGS_UNDER_LIMIT
        curr_sum = 0
        for child in self.m_children:
            if child.m_fileSize == 0:
                curr_sum += child.getMemorySum(modGlob)
            else:
                curr_sum += child.m_fileSize
        if curr_sum < 100000 and modGlob:
            SUM_OF_THINGS_UNDER_LIMIT += curr_sum
        return curr_sum
    def findMinMemory(self):
        global MIN_DUR_TO_DELETE
        curr_sum = 0
        for child in self.m_children:
            if child.m_fileSize == 0:
                curr_sum += child.findMinMemory()
            else:
                curr_sum += child.m_fileSize
        if curr_sum > SPACE_NEEDED and curr_sum < MIN_DUR_TO_DELETE:
            MIN_DUR_TO_DELETE = curr_sum
        return curr_sum
    def getDurToDelete(self):
        global MIN_DUR_TO_DELETE
        MIN_DUR_TO_DELETE = 70000000
        global SPACE_NEEDED
        SPACE_NEEDED = 30000000 - (70000000 - self.getMemorySum())
        self.findMinMemory()
        toDelete = MIN_DUR_TO_DELETE
        return toDelete

file = open('input.txt','r')
raw_data = file.read().strip().split("\n")
rootDur = FileEntity("root")
currDur = rootDur
currDur.AddChild("/")

for line in raw_data:
    broken_up_line = line.split()
    if(broken_up_line[0] == '$'):
        if broken_up_line[1] == "cd":
            if broken_up_line[2] == "..":
                currDur = currDur.m_parent
            for child in currDur.m_children:
                if child.m_entityName == broken_up_line[2] and child.m_fileSize == 0:
                    currDur = child
                    break
    else:
        if broken_up_line[0] == "dir":
            currDur.AddChild(broken_up_line[1], 0)
        else:
            currDur.AddChild(broken_up_line[1], int(broken_up_line[0]))

# part a
totalSum = rootDur.m_children[0].getMemorySum(True)
print(SUM_OF_THINGS_UNDER_LIMIT)

# part b
print(rootDur.m_children[0].getDurToDelete())
