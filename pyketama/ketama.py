"""
    Ketama algorithm



"""

class Ketama(object):

    def __init__(self,hash_digest=hash,repeat_times=5,bucket=1000):
        self.repeat_times   = repeat_times
        self.bucket         = bucket
        self.hash_digest    = hash_digest
        self.towers         = [None]*bucket
        
    def addTower(self,string):
        # Could be collision when two servers has same towers
        th = self.hash_digest(string)
        a = self.bucket/self.repeat_times
        for i in xrange(1,self.repeat_times+1):
            self.towers[( ((th % self.bucket)+i*a) % self.bucket )] = string 
            
        
    def getTower(self,string):
        h = self.hash_digest(string) % self.bucket
        for i in xrange(h+1,h+self.bucket+1):
            t = self.towers[i%1000]
            if t: return t
        
if __name__ == '__main__':
    import pyketama.hashes as h
    k = Ketama(hash_digest=h.hashPJW)    
    k.addTower('agon')
    k.addTower('dinamo')
    k.addTower('data')
    k.addTower('hash')
    k.addTower('type')
    
    print 'test:',k.getTower('test')
    print 'hello:',k.getTower('hello')
    print 'guest:',k.getTower('guest')
    print 'alert:',k.getTower('alert')
    
    import time
    st = time.time()
    for i in xrange(100000):
        k.getTower('test4')
        
    print time.time()-st
