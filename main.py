# coding: utf-8
import os
import time

print("USS module preparing to send a message")

#print("__name__ value : ", __name__)

hook = "https://hooks.slack.com/services/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"
start = 0
c_time = 0

def send(msg):
    #print("hello")
    cmd = "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"" + msg + "\"}' " + hook
    os.system(cmd)
    return

def make_begin():
    global start
    start = time.time()
    return "The program has begun ! If you didn t get this message, then well... saying that now would be pointless... but make sure your friends have the good URL in the hook variable :3"

def make_end():
    return "This is the end, my friend~~~~~~"

def make_ml_train(a):
    msg=""
    for line in a:
        msg += line[0]+" : "+line[1]+",\n"
    return msg

def make_ETA(current_epoch, total_epochs):
    import time
    global start
    global c_time
    c_time = time.time()
    c_time -= start
    msg= "Program has been running for : " + str(c_time) + ",\n"
    completion = float(current_epoch / total_epochs)
    msg+= "and has completed :" + str(completion*100) + "% of the training.\n"
    eta = c_time * (1/completion - 1)
    msg+= "Program will end in : " + str(eta) + " at : " + time.ctime(time.time() + eta)
    return msg

def ETA(current_epoch, total_epochs):
    return send(make_ETA(current_epoch, total_epochs))

def begin():
    return send(make_begin())

def end():
    return send(make_end())

def ml_train(a):
    return send(make_ml_train(a))

def main():    
    msg = "What do you want ?! è.é"
    print("Sending...")
    send(msg)
    print("Done.")
    if testing == True:
        begin()
        ml_train([["Your power",">9000"], ["My brain",">your brain"]])
        end()

if __name__ == "__main__":
    testing=True
    main()
