public class Q2 {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty() ||val <= minStack.peek()) {
            minStack.push(val);
        }
        else{
            minStack.push(minStack.peek());
        }
    }
    
    public void pop() {
        if (stack.isEmpty()) return;
        stack.pop();
        minStack.pop();
        
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
