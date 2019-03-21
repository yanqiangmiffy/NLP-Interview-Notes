class TreeNode(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def insert(self,value):
        """
        二叉排序树添加节点
        """
        if self.value:
            if value <self.value:
                if self.left is None:
                    self.left=TreeNode(value)
                else:
                    self.left.insert(value)
            elif value>self.value:
                if self.right is None:
                    self.right=TreeNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value=value

    def preTraversal(self,root):
        """
        前序遍历 root->left->right
        """
        res=[]
        if root:
            # print(root.value)
            res.append(root.value)
            res=res+self.preTraversal(root.left)
            res=res+self.preTraversal(root.right)
        return res
    def midTraversal(self,root):
        """
        中序遍历 left->root->right
        """
        res=[]
        if root:
            res=res+self.midTraversal(root.left)
            # print(root.value)
            res.append(root.value)
            res=res+self.midTraversal(root.right)
        return res

    def postTraversal(self,root):
        """
        后序遍历 left->right->root
        """
        res=[]
        if root:
            res=res+self.postTraversal(root.left)
            res=res+self.postTraversal(root.right)
            # print(root.value)
            res.append(root.value)
        return res

    def levelTraversel(self,root):
        """
        层次遍历
        """
        res=[]
        if root is None:
            return 
        queue=[]
        queue.append(root)

        while queue:
            node=queue.pop(0)
            res.append(node.value)
            if node.left!=None:
                queue.append(node.left)    
            if node.right!=None:
                queue.append(node.right)
        return res
if __name__ == "__main__":
    root=TreeNode(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    
    print("前序遍历：")
    print(root.preTraversal(root))

    print("中序遍历：")
    print(root.midTraversal(root))

    print("后序遍历：")
    print(root.postTraversal(root))

    print("层次遍历：")
    print(root.levelTraversel(root))