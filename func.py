class dict():
    def __init__(self):
        self.key = []
        self.value = []
    
    def __setitem__(self,key,value):
        self.key.append(key)
        self.value.append(value)
    
    def __getitem__(self,name):
        return self.value[self.key.index(name)]
                
    def __delitem__(self,name):
        del self.value[self.key.index(name)]
        del self.key[self.key.index(name)]
        
    def clear(self):
        del self.key
        del self.value
        self.key = []
        self.value = []
    
    def values(self):
        return self.value
    
    def keys(self):
        return self.key
        
if __name__ == "__main__":
    dic = dict()
    dic['he'] = 3
    dic[2]    = 4
    print(dic.values())
    print(dic.keys())