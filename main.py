# coding: utf-8
import os

print("USS module preparing to send a message")

#print("__name__ value : ", __name__)

hook = "https://hooks.slack.com/services/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"

def send(msg):
    #print("hello")
    cmd = "curl -X POST -H 'Content-type: application/json' --data '{\"text\":\"" + msg + "\"}' " + hook
    os.system(cmd)
    return

def make_begin():
    return "The program has begun ! If you didn t get this message, then well... saying that now would be pointless... but make sure your friends have the good URL in the hook variable :3"

def make_end():
    return "This is the end, my friend~~~~~~"

def make_ml_train(a):
    msg=""
    for line in a:
        msg += line[0]+" : "+line[1]+",\n"
    return msg

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
