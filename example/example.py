from pyketama import Ketama

def test(k):
        data = {}
        for i in xrange(REQUESTS):
            tower = k.get_node('a'+str(i))
            data.setdefault(tower,0)
            data[tower] += 1
        print 'Number of caches on each node: '
        print data
        print ''
        
        print k.get_node('Aplple');
        print k.get_node('Hello');
        print k.get_node('Data');
        print k.get_node('Computer');
        
NODES = ['192.168.0.1:6000','192.168.0.1:6001','192.168.0.1:6002',
        '192.168.0.1:6003','192.168.0.1:6004','192.168.0.1:6005',
        '192.168.0.1:6006','192.168.0.1:6008','192.168.0.1:6007'
       ]
REQUESTS = 1000

k = Ketama(NODES)  
    
test(k)

k.remove_node('192.168.0.1:6007')

test(k)

k.add_node('192.168.0.1:6007')

test(k)
