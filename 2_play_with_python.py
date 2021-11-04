from win32com.client import Dispatch

sub1 = int(input("enter your marathi test mark : "))
sub2 = int(input("enter your englisg test mark : "))
sub3 = int(input("enter your hindi test mark : "))
sub4 = int(input("enter your science test mark : "))
sub5 = int(input("enter your math's test mark : "))
sub6 = int(input("enter your his and politcel-science test mark : "))
sub7 = int(input("enter your gio test mark : "))


if(sub1<33):
    t = sub1  
    s1 ="\nyou are fail in marathi"
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s1)
    print(s1)
else:
    t = sub1   
    st1="\nyour marathi test mark is : "+str(t)
    speakj = Dispatch("SAPI.SpVoice")
    speakj.Speak(st1)
    print(st1)

if (sub2<33):
    t2 = sub2
    ss2 ="you are fail in englisg"
    speaks = Dispatch("SAPI.SpVoice")
    speaks.Speak(ss2)
    print(ss2)

else:
    t2 = sub2
    stt2 = "your english test mark is : "+str(t2)
    peah = Dispatch("SAPI.SpVoice")
    peah.Speak(stt2)

    print(stt2)
  
if(sub3<33):
     t3= sub3
     ssy = "you are fail in hindi"
     spe = Dispatch("SAPI.SpVoice")
     spe.Speak(ssy)
     print(ssy)
    
    
    
else:
    t3= sub3
    fg="your hindi test mark is : "+str(t3)
    sp= Dispatch("SAPI.SpVoice")
    sp.Speak(fg)
    print(fg)
 

if(sub4<33):
    t4 = sub4  
    s13 ="you are fail in science"
    speakh = Dispatch("SAPI.SpVoice")
    speakh.Speak(s13)
    print(s13)
else:
    t4 = sub4  
    sts1="you science test mark is : "+str(t4)
    speakjf = Dispatch("SAPI.SpVoice")
    speakjf.Speak(sts1)
    print(sts1)


if(sub5<33):
    t5 = sub5 
    s134 ="you are fail in math's"
    speakh = Dispatch("SAPI.SpVoice")
    speakh.Speak(s134)
    print(s134)
else:
    t5 = sub5  
    sts14="you math's test mark is : "+str(t5)
    speakjfj = Dispatch("SAPI.SpVoice")
    speakjfj.Speak(sts14)
    print(sts14)

if(sub6<33):
    t6 = sub6  
    s134j ="you are fail in his and politcel-science"
    speajkh = Dispatch("SAPI.SpVoice")
    speajkh.Speak(s134j)
    print(s134j)
else:
    t6 = sub6  
    sts141="you his and politcel-science test mark is : "+str(t6)
    speakjfj1 = Dispatch("SAPI.SpVoice")
    speakjfj1.Speak(sts141)
    print(sts141)

if(sub7<33):
    t7 = sub7  
    s134jhl ="you are fail in gio"
    speajkhl = Dispatch("SAPI.SpVoice")
    speajkhl.Speak(s134jhl)
    print(s134jhl)
else:
    t7 = sub7  
    sts141j="you gio test mark is : "+str(t7)
    speakjfj1k = Dispatch("SAPI.SpVoice")
    speakjfj1k.Speak(sts141j)
    print(sts141j)



total = (t+t2+t3+t4+t5+t6+t7)/2





if(total<40):
    k = "your fail because your total percentage less than 40"
    sat= Dispatch("SAPI.SpVoice")
    sat.Speak(k)
    print(k)

else:
    o="\n \tcongatulations ! you passed the exam\n"+"your total marks is : "+str(total)
    sn= Dispatch("SAPI.SpVoice")
    sn.Speak(o)
    print(o)




