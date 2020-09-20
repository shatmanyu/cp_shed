class newNode:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

## Views of Binary Tree
## D.S used -> Queue
## Algo useed -> Level order Traversal + Vertical Order Traversal
def leftView(root):
    if not root:
        return
    q=[];ans=[]
    q.append(root);ans.append(root.val);q.append(None)
    while q:
        temp=q.pop(0)
        printt=False
        if temp:
            while temp:
                ele=temp
                if ele.left:
                    q.append(ele.left)
                    if not printt:
                        printt=True
                        ans.append(ele.left.val)
                if ele.right:
                    q.append(ele.right)
                    if not printt:
                        printt=True
                        ans.append(ele.right.val)
                temp=q.pop(0)
            q.append(None)
        else:
            continue
    print(*ans)

def rightView(root):
    if not root:
        return
    q=[];ans=[]
    q.append(root);q.append(None)
    while q:
        temp=q.pop(0)
        printt=False
        if temp:
            while temp:
                ele=temp
                if ele.left:
                    q.append(ele.left)
                    if not printt:
                        printt=True
                        #ans.append(ele.left.val)
                if ele.right:
                    q.append(ele.right)
                    if not printt:
                        printt=True
                        #ans.append(ele.right.val)
                temp=q.pop(0)
                if not temp:
                    ans.append(ele.val)
            q.append(None)
        else:
            continue
    print(*ans)

def topView(root):
    if not root:
        return
    ## get level of every node of left and right subtree
    ans=[];l=0;q=[];q.append(root);d={};q.append(None)
    ans.append(root.val)
    while q:
        temp=q.pop(0)
        if temp:
            if temp.val not in d:
                d[temp.val]=l
            while temp:
                ele=temp
                if ele.left:
                    q.append(ele.left)
                    d[ele.left.val]=d[ele.val]-1
                    ans.append(ele.left.val)
                if ele.right:
                    q.append(ele.right)
                    d[ele.right.val]=d[ele.val]+1
                    ans.append(ele.right.val)
                temp=q.pop(0)
            q.append(None)
        else:
            continue
    ans1={i:0.5 for i in sorted(list(d.values()))}
    for i in ans:
        if ans1[d[i]]==0.5:
            ans1[d[i]]=i
    print(*list(ans1.values()))
    
def bottomView(root):
    if not root:
        return
    ## get level of every node of left and right subtree
    ans=[];l=0;q=[];q.append(root);d={};q.append(None)
    ans.append(root.val)
    while q:
        temp=q.pop(0)
        if temp:
            if temp.val not in d:
                d[temp.val]=l
            while temp:
                ele=temp
                if ele.left:
                    q.append(ele.left)
                    d[ele.left.val]=d[ele.val]-1
                    ans.append(ele.left.val)
                if ele.right:
                    q.append(ele.right)
                    d[ele.right.val]=d[ele.val]+1
                    ans.append(ele.right.val)
                temp=q.pop(0)
            q.append(None)
        else:
            continue
    ans1={i:0.5 for i in sorted(list(d.values()))}
    for i in ans:
        ans1[d[i]]=i
    print(*list(ans1.values()))
    
    
root = newNode(10)  
root.left = newNode(12)  
root.right = newNode(3)  
root.left.right = newNode(4)  
root.right.left = newNode(5)  
root.right.left.right = newNode(6)  
root.right.left.right.left = newNode(18)  
root.right.left.right.right = newNode(7) 
#leftView(root) 
bottomView(root)
