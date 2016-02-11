import OSC

def handler(addr, tags, data, client_address):
    txt = "Mensaje OSC '%s' DE %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

if __name__ == "__main__":
    s = OSC.OSCServer(('127.0.0.1', 5720))  # listen on localhost, port 5720
    s.addMsgHandler('/micity_checkout', handler)     # call handler() for OSC messages received with the /checkout address
s.addMsgHandler('/micity_checkin', handler)     # call handler() for OSC messages received with the /checkin address
s.addMsgHandler('/bici_checkout',handler)
s.addMsgHandler('/bici_checkin', handler)  
s.serve_forever()
