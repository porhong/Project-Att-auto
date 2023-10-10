from datetime import datetime
import time as time2
from datetime import time
import subprocess
import schedule
import random
import requests





ran = str(random.randrange(10,30))
ran2 = str(random.randrange(1,5))
mor_ran = "08:"+ran
lunch_ran_out = "12:"+ran
lunch_ran_in = "13:0"+ran2
leave_ran = "17:3"+ran2
check = 0
check_time = 1
run = True
morning_1 = time(8,00,0).strftime("%H:%M")
morning_2 = time(8,59,0).strftime("%H:%M")
lunch_1 = time(9,00,0).strftime("%H:%M")
lunch_2 = time(12,30,0).strftime("%H:%M")
after_lunch_1 = time(12,31,0).strftime("%H:%M")
after_lunch_2 = time(13,30,0).strftime("%H:%M")
leave_work_1 = time(13,31,0).strftime("%H:%M")
leave_work_2 = time(18,59,0).strftime("%H:%M")

def start() :
    now = datetime.now()
    current_time = now.strftime("%H:%M") 
    global check   
    global run
    run = True
    if current_time >= morning_1 and current_time <= morning_2 :
        check = 1
    elif current_time >= lunch_1 and current_time <= lunch_2  :
        check = 2
    elif current_time >= after_lunch_1 and current_time <= after_lunch_2 :
        check = 3
    elif current_time >= leave_work_1 and current_time <= leave_work_2 :
        check = 4
    else :
        check = 0


def wait2run():

    now = datetime.now()
    current = now.strftime("%H:%M:%S")
    # start time
    start_time = current
    end_time = "07:00:00"
    # convert time string to datetime
    t1 = datetime.strptime(start_time, "%H:%M:%S")
    t2 = datetime.strptime(end_time, "%H:%M:%S")
    # get difference
    delta = t1 - t2

    runtime = delta.total_seconds()
    return runtime




def send_to_telegram(message):

    apiToken = '6628897049:AAGzSfvTc8xSMpX9wMFiU7OF-PLBx0VMPDU'
    chatID = '673968568'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        #print(response.text)
    except Exception as e:
        print(e)

def check_time_passed(time_run_check):
    now = datetime.now()
    current = now.strftime("%H:%M")
    if time_run_check < current :
        start()


    
    # reactive_time = time(7,00,0).strftime("%H:%M")
    # delta = datetime.strftime(current) - datetime.strftime(reactive_time)
    # second = delta.total_seconds()
    # print("Sleeping time !!" + second)




# morning_1 = time(8,00,0).strftime("%H:%M")
# morning_2 = time(9,00,0).strftime("%H:%M")
# lunch_1 = time(11,55,0).strftime("%H:%M")
# lunch_2 = time(12,30,0).strftime("%H:%M")
# after_lunch_1 = time(13,0,0).strftime("%H:%M")
# after_lunch_2 = time(13,30,0).strftime("%H:%M")
# leave_work_1 = time(17,0,0).strftime("%H:%M")
# leave_work_2 = time(18,30,0).strftime("%H:%M")



# def start() :
#     now = datetime.now()
#     current_time = now.strftime("%H:%M")

#     if current_time >= morning_1 and current_time <= morning_2 :
#         print("Morning Script"+ " Current time is : " +  current_time)
#         subprocess.call([r'In1.bat'])
#     elif current_time >= lunch_1 and current_time <= lunch_2  :
#         print("Lunch script"+ " Current time is : " +  current_time)
#         subprocess.call([r'leave.bat'])
#     elif current_time >= after_lunch_1 and current_time <= after_lunch_2 :
#         print("After lunch script"+ " Current time is : " +  current_time)
#         subprocess.call([r'In2.bat'])
#     elif current_time >= leave_work_1 and current_time <= leave_work_2 :
#         print("Leave work script"+ " Current time is : " +  current_time)
#         subprocess.call([r'leave.bat'])
#     else :
#         print("Not Action time." + " Current time is : " +  current_time)

def in1() :
    subprocess.call([r'In1.bat'])
    ran = str(random.randrange(10,30,2)) 
    ran2 = str(random.randrange(-1,5))
    global mor_ran 
    global lunch_ran_out
    global lunch_ran_in
    global leave_ran
    global check_time
    global run
    run = False
    mor_ran = "08:"+ran
    lunch_ran_out = "12:"+ran
    lunch_ran_in = "13:0"+ran2
    leave_ran = "17:3"+ran2
    check_time = 2
    send_to_telegram("""
Check in morning success 🟢 
Time start : """ + current_time) 
    print("Sleeping time !!")
    time2.sleep(3600)



def lunch():
    subprocess.call([r'leave.bat'])
    ran = str(random.randrange(10,30,2)) 
    ran2 = str(random.randrange(-1,5))
    global mor_ran 
    global lunch_ran_out
    global lunch_ran_in
    global leave_ran
    global check_time
    global run
    run = False
    mor_ran = "08:"+ran
    lunch_ran_out = "12:"+ran
    lunch_ran_in = "13:0"+ran2
    leave_ran = "17:3"+ran2
    check_time = 3
    send_to_telegram("""
Check Out for lunch success 🟢 
Time start : """ + current_time) 
    print("Sleeping time !!")
    time2.sleep(1200)

def in2():
    subprocess.call([r'In2.bat'])
    ran = str(random.randrange(10,30,2)) 
    ran2 = str(random.randrange(-1,5))
    global mor_ran 
    global lunch_ran_out
    global lunch_ran_in
    global leave_ran
    global check_time
    global run
    run = False
    mor_ran = "08:"+ran
    lunch_ran_out = "12:"+ran
    lunch_ran_in = "13:0"+ran2
    leave_ran = "17:3"+ran2
    check_time = 4
    send_to_telegram("""
Check in after lunch success 🟢 
Time start : """ + current_time) 
    print("Sleeping time !!")
    time2.sleep(1800)

def leave():
    subprocess.call([r'leave.bat'])
    ran = str(random.randrange(10,30,2)) 
    ran2 = str(random.randrange(-1,5))
    global mor_ran 
    global lunch_ran_out
    global lunch_ran_in
    global leave_ran
    global check_time
    global run
    run = False
    mor_ran = "08:"+ran
    lunch_ran_out = "12:"+ran
    lunch_ran_in = "13:0"+ran2
    leave_ran = "17:3"+ran2
    check_time = 0
    send_to_telegram("""
Check out of day success 🟢 
Time start : """ + current_time) 
    runAt = 2*wait2run()
    send_to_telegram("""
Watting to Start at Tmr 😴
Time start : """ + runAt) 
    print("Sleeping time !! and will start at ;" + runAt)
    time2.sleep(runAt)

def dayoff():
    relax = "It's not working day 😀"
    print (relax)
    send_to_telegram(relax)
    time2.sleep(82800)
    start()


while True:
    
    print ("******* Welcome *******")
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    send_to_telegram("""
Service Started
Time start : """ + current_time) 
    print("Started time is : " + current_time)
    print("Status : Active")
    start()
    if check == 1 :
        print ( "Current Check is : " + str(check))

        schedule.every().monday.at(mor_ran).do(in1)
        schedule.every().tuesday.at(mor_ran).do(in1)
        schedule.every().wednesday.at(mor_ran).do(in1)
        schedule.every().thursday.at(mor_ran).do(in1)
        schedule.every().friday.at(mor_ran).do(in1)
        schedule.every().saturday.at(mor_ran).do(dayoff)
        schedule.every().sunday.at(mor_ran).do(dayoff)
        print("Will run at : " + str(mor_ran))
        send_to_telegram("""
Waiting Check in morning 🟠  
Will start : """ + mor_ran) 
        while run == True:
            schedule.run_pending()
            time2.sleep(1)
            check_time_passed(mor_ran)

    elif check ==2 :
        print ( "Current Check is : " + str(check))

        schedule.every().monday.at(lunch_ran_out).do(lunch)
        schedule.every().tuesday.at(lunch_ran_out).do(lunch)
        schedule.every().wednesday.at(lunch_ran_out).do(lunch)
        schedule.every().thursday.at(lunch_ran_out).do(lunch)
        schedule.every().friday.at(lunch_ran_out).do(lunch)
        print("Will run at : " + str(lunch_ran_out))
        send_to_telegram("""
Waiting Check out lunch 🟠  
Will start : """ + lunch_ran_out) 
        while run == True:
            schedule.run_pending()
            time2.sleep(1)
            check_time_passed(lunch_ran_out)

    elif check == 3 :
        print ( "Current Check is : " + str(check))
        schedule.every().monday.at(lunch_ran_in).do(in2)
        schedule.every().tuesday.at(lunch_ran_in).do(in2)
        schedule.every().wednesday.at(lunch_ran_in).do(in2)
        schedule.every().thursday.at(lunch_ran_in).do(in2)
        schedule.every().friday.at(lunch_ran_in).do(in2)
        print("Will run at : " + str(lunch_ran_in))
        send_to_telegram("""
Waiting Check in after lunch 🟠  
Will start : """ + lunch_ran_in)
        while run == True:
            schedule.run_pending()
            time2.sleep(1)
            check_time_passed(lunch_ran_in)

    elif check == 4:
        print ( "Current Check is : " + str(check))
        schedule.every().monday.at(leave_ran).do(leave)
        schedule.every().tuesday.at(leave_ran).do(leave)
        schedule.every().wednesday.at(leave_ran).do(leave)
        schedule.every().thursday.at(leave_ran).do(leave)
        schedule.every().friday.at(leave_ran).do(leave)
        print("Will run at : " + str(leave_ran))
        send_to_telegram("""
Waiting Check out of the day 🟠  
Will start : """ + leave_ran)
        while run == True:
            schedule.run_pending()
            time2.sleep(1)
            check_time_passed(leave_ran)
            
    else :
        print("Not Active time!!")
        time2.sleep(60)
    
    


    
    


