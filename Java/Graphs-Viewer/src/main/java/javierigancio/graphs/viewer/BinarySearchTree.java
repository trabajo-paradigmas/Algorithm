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
public class BinarySearchTree {

    node root;

    public BinarySearchTree() {
        this.root = null;
    }

    public void insert(int key) {
        root = fInert(root, key);
    }

    public void delete(int key) {
        root = fDelete(root, key);
    }

    public void preOrder(node fNode) {
        /*funcion de la wea de java que va a mostrar la caga en una pantalla qla.*/
        if (fNode.izq != null) {
            preOrder(fNode.izq);
        }
        if (fNode.der != null) {
            preOrder(fNode.der);
        }
    }

    public void inOrder(node fNode) {
        if (fNode.izq != null) {
            inOrder(fNode.izq);
        }
        /*funcion de la wea de java que va a mostrar la caga en una pantalla qla.*/
        if (fNode.der != null) {
            inOrder(fNode.der);
        }
    }

    public void posOrder(node fNode) {
        if (fNode.izq != null) {
            posOrder(fNode.izq);
        }
        if (fNode.der != null) {
            posOrder(fNode.der);
        }
        /*funcion de la wea de java que va a mostrar la caga en una pantalla qla.*/
    }

    public int buscarMin(node nodo) {
        if (nodo.izq == null) {
            return nodo.key;
        }
        return buscarMin(nodo.izq);
    }

    private node fInert(node nodo, int key) {
        if (nodo == null) {
            node f = new node(key);
            return f;
        }
        if (nodo.key < key) {
            node f = fInert(nodo.der, key);
            nodo.der = f;
        }
        if (nodo.key > key) {
            node f = fInert(nodo.izq, key);
            nodo.izq = f;
        }
        return nodo;
    }

    private node fDelete(node nodo, int key) {
        if (nodo == null) {
            return nodo;
        }
        if (nodo.key < key) {
            nodo.der = fDelete(nodo.der, key);
        } else if (nodo.key > key) {
            nodo.izq = fDelete(nodo.izq, key);
        } else {
            if (nodo.izq == null) {
                return nodo.der;
            } else if (nodo.der == null) {
                return nodo.izq;
            }
            nodo.key = buscarMin(nodo.der);
            nodo.der = fDelete(nodo.der, nodo.key);
        }
        return nodo;
    }
}
