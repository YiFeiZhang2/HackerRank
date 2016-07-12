    int findMax(Node child){
        int leftMax = 0;
        int rightMax = 0;
        
        if (child.left != null) {
            leftMax = findMax(child.left);
        }
        if (child.right != null) {
            rightMax = findMax(child.right);
        }
        
        return Math.max(child.data, Math.max(leftMax, rightMax));
    }

    int findMin(Node child){
        int leftMin = 10000;
        int rightMin = 10000;
        
        if (child.left != null) {
            leftMin = findMin(child.left);
        }
        if (child.right != null) {
            rightMin = findMin(child.right);
        }
        
        return Math.min(child.data, Math.min(leftMin, rightMin));
    }
    
    boolean checkBST(Node root) {
        boolean isLeftBST = false;
        boolean isRightBST = false;
        
        if (root.left == null){
            isLeftBST = true;
        } else if (root.data <= findMax(root.left)){
            isLeftBST = false;
        } else {
            isLeftBST = checkBST(root.left);
        }
        
        if (root.right == null){
            isRightBST = true;
        } else if (root.data >= findMin(root.right)){
            isRightBST = false;
        } else {
            isRightBST = checkBST(root.right);
        }

        return (isLeftBST && isRightBST);
    }
