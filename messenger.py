# coding: utf-8
import os
import time

class messenger:    
    def __init__(self, hook = None):
        self.hook = hook
        self.start = 0
        self.c_time = 0
        
        if self.hook == None:
            print("No hook defined, using default hook")
            self.hook = "https://hooks.slack.com/services/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"
            return
        
        assert(hook != None)
        print("USS module ready to send a message")
    
    def set_hook(self, hook):
        self.hook = hook
    
    def send(self, msg):
        #print("hello")
        cmd = "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"" + msg + "\"}' " + self.hook
        os.system(cmd)
        return

    def make_begin(self):
        self.start = time.time()
        return "The program has begun ! If you didn t get this message, then well... saying that now would be pointless... but make sure your friends have the good URL in the hook variable :3"

    def make_end(self):
        return "This is the end, my friend~~~~~~"

    def make_ml_train(self, a):
        msg=""
        for line in a:
            msg += line[0]+" : "+line[1]+",\n"
        return msg

    def make_ETA(self, current_epoch, total_epochs):
        import time
        self.c_time = time.time() - self.start
        msg= "Program has been running for : " + str(int(self.c_time)) + " seconds,\n"
        completion = float(current_epoch / total_epochs)
        msg+= "and has completed :" + str(round(completion*100, 2)) + "% of the training (epoch count : "+ str(current_epoch) + "/" + str(total_epochs) + ".\n"
        eta = self.c_time * (1/completion - 1)
        msg+= "Program will end in : " + str(int(eta)) + " seconds at : " + time.ctime(time.time() + eta)
        return msg

    def make_pix_graph(self, shape):
        l = len(shape)
        m = max(shape)
        shape = [int((i/m)*20) for i in shape]
        m = max(shape)
        a = [[] for i in range(m)]
        for k in range(m):
            #print(int((m - k - 1)/2))
            #print(int((m + k + 1)/2))
            for i in range(l):
                if k > m/2 - shape[i]/2 - 1 and k < m/2 + shape[i]/2:
                    a[k].append("0")
                else:
                    a[k].append(".")
                if i == l - 1:
                    a[k].append("\n")
        print(a)
        mess = "     "
        for line in a:
            for charac in line:
                mess += charac + "     "
        print(mess)
        return mess

    def ETA(self, current_epoch, total_epochs):
        return self.send(self.make_ETA(current_epoch, total_epochs))

    def begin(self):
        return self.send(self.make_begin())

    def end(self):
        return self.send(self.make_end())

    def ml_train(self, a):
        return self.send(self.make_ml_train(a))

    def main(self):    
        msg = "What do you want ?! è.é"
        print("Sending...")
        self.send(msg)
        print("Done.")
        self.begin()
        self.ml_train([["Messaging power",">9000"], ["My brain",">your brain"]])
        self.ETA(100, 333)
        self.end()
