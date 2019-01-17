# aegir
**Wave Function Collapse for wine descriptions**

*This project is named for Ægir, the Norse god of beer and mead*


We Forked this repo: https://github.com/mewo2/oisin 
which mashes up sentance fragments to produce poems with fixed metric forms. 

Example of output with original Alice in Wonderland corpus:

![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/alice_output.png)

Example of output with wine description corpus:

![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/1.png)
![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/2.png)
![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/3.png)
![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/4.png)
![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/5.png)
![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/6.png)
![alt text](https://github.com/sarahmfrost/aegir/blob/master/images/7.png)


The original repository had minimal documentation for installation and running the algorithm, so we messed around with that for a while. 

The installation process running Mac OS: 

Download project and unzip
In your terminal, cd to the directory and run the following commands:

```
pip install -r requirements.txt
python3 ballad.py 
```

To change the output of ballad.py, an obvious first step is to change the corpus that is referenced. In our case, we tested this algorithm on a document filled with wine terminology definitions and drink descriptions that can be found in "input/wine.txt" and updated the filename reference in ballad.py. 

```
filename = "input/wine.txt"
```

Another way to adjust the output is to change the parameters called in the balladize() function in ballad.py. The balladize() function in defined in "oisin/poetry.py". This function takes in the following variables: tokens (or the corpus), meter (which is defined using the iambic() function), step size, refrain and order.

```
oisin.balladize(
    oisin.load(filename),
    meter=oisin.iambic(6, 'aabbcc'),
    step=13,
    order=3)
```

To add more variation to the output text, we randomized the step size between values of 1 to 12 in the balladize() function. Otherwise, running balladize() multiple times does not lead to varied results.

