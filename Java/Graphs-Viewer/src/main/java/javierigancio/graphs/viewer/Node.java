package javierigancio.graphs.viewer;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Usach
 */
public class Node<T> {
    public T value;
    public Node<T> left;
    public Node<T> right;
    public Node<T> parent;
    
    public Node(T value, Node<T> left, Node<T> right) 
    {
        this.value = value;
        this.left = left;
        this.right = right;
    }
}
