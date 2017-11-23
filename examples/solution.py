import multiprocessing as mp
from netmiko import ConnectHandler()
from time import sleep


devs = [
        cisco_7200_R1 = { 'device_type': 'generic_termserver_telnet',
                  'ip': '127.0.0.1',
                  'port': 2015
        },

        cisco_7200_R2 = { 'device_type': 'generic_termserver_telnet',
                  'ip': '127.0.0.1',
                  'port': 2015
        }
]


def talk_to_router(dev_dict,rname,q):
    net_connect = ConnectHandler(**dev_dict)
    net_connect.read_channel()
    net_connect.write_channel('show ip interface brief\r\n')
    sleep(2)
    output1 = net_connect.read_channel()
    net_connect.write_channel('show ip interface brief\r\n')
    net_connect.read_channel()
    net_connect.write_channel('show arp\r\n')
    output2 = net_connect.read_channel()
    q.put((rname,output1,output2))



if __name__ == '__main__':
    
    jobs = []
    results = []
    q = mp.Queue()
    for i in range(0,1):
        p = mp.Process(target = talk_to_router, args = (devs[i],'R ' + str(i+1),q)    
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()

    while not q.empty():
        results.append(q.get())

    print (results)
