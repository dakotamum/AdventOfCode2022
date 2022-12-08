GLOBAL_SUM = 0
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
    def getMemorySum(self):
        print(self.m_entityName)
        dur_sizes = 0
        file_sizes = 0
        for child in self.m_children:
            if child.m_fileSize == 0:
                dur_sizes += child.getMemorySum()
            else:
                file_sizes += child.m_fileSize
        if dur_sizes + file_sizes < 100001:
            print (dur_sizes + file_sizes)
            print ('---------')
            return dur_sizes + file_sizes
        else:
            print (dur_sizes)
            print ('---------')
            return dur_sizes

    # def getMemorySum(self):
    #     # print(self.m_entityName)
    #     curr_dur_size = 0
    #     for child in self.m_children:
    #         if child.m_fileSize == 0:
    #             curr_dur_size += child.getMemorySum()
    #         else:
    #             curr_dur_size += child.m_fileSize
    #     return curr_dur_size

file = open('input.txt','r')
raw_data = file.read().strip().split("\n")

rootDur = FileEntity("root")
currDur = rootDur
currDur.AddChild("/")

# print(currDur.m_entityName)

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
rootDur.PrintTree()
print(rootDur.getMemorySum())