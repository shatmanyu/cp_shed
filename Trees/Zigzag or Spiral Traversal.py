class newNode:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None


## ZigZag or spiral level order traversal of binary tree
## DS used -> Queue
## Algo used -> Level order traversal
## Concept -> Do Simple Level order Traversal + change directon at each level through switch(sw) variable



def zigzag(root):
    if not root:
        return
    q=[];q.append(root);q.append(None);ans=[];sw=0
    while q:
        temp=q.pop(0)
        if temp:
            k=[]
            while temp:
                ele=temp
                if ele.left:
                    q.append(ele.left)
                    k.append(ele.left.val)
                if ele.right:
                    q.append(ele.right)
                    k.append(ele.right.val)
                temp=q.pop(0)
            if k and sw:
                ans.append(k)
            elif k and not sw:
                k.reverse()
                ans.append(k)
            q.append(None)
            if sw==0:
                sw=1
            else:
                sw=0
        else:
            continue
    return ans
            
                
                    
                    

















root = newNode(10)  
root.left = newNode(12)  
root.right = newNode(3)  
root.left.right = newNode(4)  
root.right.left = newNode(5)  
root.right.left.right = newNode(6)  
root.right.left.right.left = newNode(18)  
root.right.left.right.right = newNode(7) 
zigzag(root)
