class Item:
    def __init__(self,name=None,price=0,category=0):
        if(price<=0):
            raise ValueError("Invalid value for price, got {}".format(price))
        self._name=name
        self._price=price
        self._category=category
        
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def category(self):
        return self._category
        
    def __str__(self):
        return f"{self.name}@{self.price}-{self.category}"
        
class Query:
    operations=["IN","EQ","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
    def __init__(self,field=None,value=None,operation=None):
        if(operation not in self.operations):
            raise ValueError("Invalid value for operation, got {}".format(operation))
        self._field=field
        self._value=value
        self._operation=operation
    
    @property
    def field(self):
        return self._field
    @property
    def value(self):
        return self._value
    @property
    def operation(self):
        return self._operation
        
    def __str__(self):
        return f"{self.field} {self.operation} {self.value}"
        
class Store:
    def __init__(self):
        self.items=[]
        
    def add_item(self,item):
        self.items.append(item)
        
    def __str__(self):
        if(len(self.items)>0):
            return "\n".join(map(str,self.items))
        else:
            return "No items"
            
    def count(self):
        return (len(self.items))
        
    @staticmethod
    def operations(operand1,operand2,operation):
        dic={"GT":True if operand1>operand2 else False,
            "LT":True if operand1<operand2 else False,
            "LTE":True if operand1<=operand2 else False,
            "GTE":True if operand1>=operand2 else False
        }
        return dic[operation]
        
    def intersection(self,args,category):
        multiple_query_values=[]
        for query in args:
            updated_result=Store()
            multiple_query=[]
            if(category=="filter"):
                multiple_query="\n".join(map(str,self.filter(query).items)).split("\n")
            else:
                multiple_query="\n".join(map(str,self.exclude(query).items)).split("\n")
            multiple_query_values.append(set(multiple_query))
            updated_items=multiple_query_values[0]
            for item in multiple_query_values:
                updated_items=updated_items&item
            for item in updated_items:
                updated_result.add_item(item)
        return updated_result
        
    def filter(self,*args):
        result=Store()
        multiple_query_values=[]
        if(len(args)==1):
            for query in args:
                if(query.operation=="EQ" or query.operation=="IN" or query.operation=="CONTAINS"):
                    if(type(query.value))!=list:
                        query._value=[query.value]
                    for qu in query.value:
                        if(query.field=="name"):
                            for item in self.items:
                                if (qu in item.name):
                                    result.add_item(item)
                        elif(query.field=="category"):
                            for item in self.items:
                                if (qu in item.category):
                                    result.add_item(item)
                        else:
                            for item in self.items:
                                if(qu==item.price):
                                    result.add_item(item)
                            
                elif(query.operation=="STARTS_WITH" or query.operation=="ENDS_WITH"):
                    for item in self.items:
                        if(query.value in item.name or query.value in item.category):
                            result.add_item(item)
                else:
                    for item in self.items:
                        operand1=getattr(item,query.field)
                        operand2=query.value
                        if(self.operations(operand1,operand2,query.operation)):
                            result.add_item(item)
            return result
        return self.intersection(args,"filter")
        
    def exclude(self,*args):
        result=Store()
        if(len(args)==1):
            for query in args:
                filter_store=self.filter(query)
                for item in self.items:
                    if item not in filter_store.items:
                        result.add_item(item)
            return result
        return self.intersection(args,"exclude")
        
    def __add__(self,other):
        result=Store()
        self_items={"\n".join(map(str,self.items))}
        other_items={"\n".join(map(str,other.items))}
        union=self_items|other_items
        union=sorted(union)
        for item in union:
            result.add_item(item)
        return result