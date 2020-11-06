import bluetooth 
from send import send_image, send_music, send_text_file, send_video

names = []
address = [] 

try :
    print("Scanning devices......\n")
    nearby_devices = bluetooth.discover_devices(lookup_names = True)

    print("found ",len(nearby_devices), "devices\n")

    i = 0

    for name, addr in nearby_devices:
        print(i+1,name,addr)
        names.append(name)
        address.append(addr)
        i+=1


    print('\n')
    print("please select the device you want to send : ",end = " ")
    n = int(input())

    device_address = names[n-1]

    services = bluetooth.find_service(address=device_address)

    print('\n')
    print("finding services of the device ..........\n")

    for ser in services :
        print(ser["name"], ser["port"])

    print('\n')

    print("Enter the Port number you want to use : ",end=" ")
    port = int(input())


    print("1. Send Text File\n2. Send Video\n3. Send Image\n4. Send Music File")
    print("What type of file you need to send ?",end=" ")
    s = int(input())


    ## choose your filename.
    if s == 1 :
        filename = "test.txt"
        send_text_file(device_address, port, filename)
    elif s == 2 :
        filename = "medifit.mp4"
        send_video(device_address, port, filename)
    elif s == 3 :
        filename = "cars.jpg"
        send_image(device_address, port, filename)
    else :
        filename = "bgm.mp3"
        send_music(device_address, port, filename)


    print('DONE !!!!')

except :
    print("Please switch on the bluetooth of both the devices")
