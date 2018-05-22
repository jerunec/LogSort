import re
from datetime import timedelta, datetime


pattern = '(\d{2}):(\d{2}):(\d{2,3})(\'\d{2,3})(\"\d{2,3})'

def sortTimestamp(curr_line,logFile,timelist):
    curr_match = re.search(pattern, curr_line)
    # prev_match = re.search(pattern, prev_line)

    class timeValue():
        def __init__(self, matchedPattern,wholeLine,fileLog):
            self.time = matchedPattern.group(0)
            self.fileName=fileLog
            self.wholeLine=wholeLine
           
    log1 = timeValue(curr_match,curr_line,logFile)
    
    return tuple([log1.fileName,log1.wholeLine,log1.time])

    # print(totalHours,totalMins,totalSecs,totalMills,totalMicro)
    # curr_match2 = re.search(pattern2, curr_line)
    # prev_match2 = re.search(pattern2, prev_line)

filename1 = "roselyn.txt"
filename2 = "jerune.txt"
file1 = open(filename1, "r")
file2 = open(filename2, "r")

# for item in sortTimestamp(ts1,ts2,file1,file2):
#     file.write("%s\n" % item)
# file.close()

with open(filename1) as f:
    content_1 = f.readlines()
content_1 = [x.strip() for x in content_1] 

with open(filename2) as f:
    content_2 = f.readlines()
content_2 = [x.strip() for x in content_2] 

timelist = []
for c1, c2 in zip(content_1, content_2):
    timelist.append(sortTimestamp(c1,'log1',timelist))
    timelist.append(sortTimestamp(c2,'log2',timelist))

def takeSecond(elem):
    return elem[2]


timelist.sort(key=takeSecond)


file = open("sorted.txt",'w')
for x in range(len(timelist)):
    tuplex = tuple(timelist[x])
    file.write(''+str(tuplex[0])+' '+str(tuplex[1])+'\n')
file.close()
# ===================f i l e 1============
# 08:00:56'699"491|f734eb70 Enter virtual void att::AttLink::OnRecv(ILink*, std::size_t, const unsigned char*, RAddr*) \
# # d 08:00:56'699"494|f734eb70 Enter virtual int IPC_TCP::LinkImpl::SetOpt(int, const void*, socklen_t) \
# # d 08:00:56'699"525|f734eb70 Leave virtual int IPC_TCP::LinkImpl::SetOpt(int, const void*, socklen_t) /

# ===================f i l e 2============
# 08:00:56'699"321|f734eb70 Enter virtual void att::AttLink::OnRecv(ILink*, std::size_t, const unsigned char*, RAddr*) \
# d 08:00:56'699"493|f734eb70 Enter virtual int IPC_TCP::LinkImpl::SetOpt(int, const void*, socklen_t) \
# d 08:00:56'699"517|f734eb70 Leave virtual int IPC_TCP::LinkImpl::SetOpt(int, const void*, socklen_t) /