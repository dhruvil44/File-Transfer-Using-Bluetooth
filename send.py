from PyOBEX.client import Client

def send_text_file(bd_addr, port, filename) :
    res = bytes("my name is Safwan Mansuri", 'utf-8') 

    client = Client(bd_addr, port) 
    client.connect()
    print('\n')
    print("Waiting for acceptance......")
    client.put(filename,res)
    client.disconnect()

def send_image(bd_addr, port, filename) :
    Image = open(filename, "rb")
    data = Image.read()

    client = Client(bd_addr, port) 
    client.connect()
    print('\n')
    print("Waiting for acceptance......")
    client.put(filename, data)
    client.disconnect()

def send_video(bd_addr, port, filename) :
    Image = open(filename, "rb")
    data = Image.read()

    client = Client(bd_addr, port) 
    client.connect()
    print('\n')
    print("Waiting for acceptance......")
    client.put(filename, data)
    client.disconnect()

def send_music(bd_addr, port, filename) :
    Image = open(filename, "rb")
    data = Image.read()

    client = Client(bd_addr, port) 
    client.connect()
    print('\n')
    print("Waiting for acceptance......")
    client.put(filename, data)
    client.disconnect()