/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javierigancio.graphs.viewer;

/**
 *
 * @author ignacio
 */
public class BinarySearchTree<T> {

    Node<T> root;

    public BinarySearchTree() {
        this.root = null;
    }

    public void insert(T key) {
        root = fInert(root, key);
    }

    public void delete(T key) {
        root = fDelete(root, key);
    }

    public void preOrder(Node fNode) {
        /*funcion de la wea de java que va a mostrar la caga en una pantalla qla.*/
        if (fNode.left != null) {
            preOrder(fNode.left);
        }
        if (fNode.right != null) {
            preOrder(fNode.right);
        }
    }

    public void inOrder(Node fNode) {
        if (fNode.left != null) {
            inOrder(fNode.left);
        }
        /*funcion de la wea de java que va a mostrar la caga en una pantalla qla.*/
        if (fNode.right != null) {
            inOrder(fNode.right);
        }
    }

    public void posOrder(Node fNode) {
        if (fNode.left != null) {
            posOrder(fNode.left);
        }
        if (fNode.right != null) {
            posOrder(fNode.right);
        }
        /*funcion de la wea de java que va a mostrar la caga en una pantalla qla.*/
    }

    public T  buscarMin(Node nodo) {
        if (nodo.left == null) {
            return (T) nodo.value;
        }
        return buscarMin(nodo.left);
    }

    private Node fInert(Node nodo, T key) {
        if (nodo == null) {
            Node<T> f = new Node<>(key, null, null);
            return f;
        }
        if ((int) nodo.value < (int) key) {
            Node f = fInert(nodo.right, key);
            nodo.right = f;
        }
        if ((int) nodo.value > (int) key) {
            Node f = fInert(nodo.left, key);
            nodo.left = f;
        }
        return nodo;
    }

    private Node fDelete(Node nodo, T key) {
        if (nodo == null) {
            return nodo;
        }
        if ((int) nodo.value < (int) key) {
            nodo.right = fDelete(nodo.right, key);
        } else if ((int) nodo.value > (int) key) {
            nodo.left = fDelete(nodo.left, key);
        } else {
            if (nodo.left == null) {
                return nodo.right;
            } else if (nodo.right == null) {
                return nodo.left;
            }
            nodo.value = buscarMin(nodo.right);
            nodo.right = fDelete(nodo.right, (T) nodo.value);
        }
        return nodo;
    }
}
