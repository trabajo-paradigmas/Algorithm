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
public class node {

    int key;
    node izq;
    node der;

    public node(int key) {
        this.key = key;
        this.izq = null;
        this.der = null;
    }
}

