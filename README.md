# aegir
Wave Function Collapse for wine descriptions 


Forked this repo: https://github.com/mewo2/oisin 
Mashes up sentance fragments to produce poems with fixed metric forms. 

Example of output with Alice in Wonderland corpus:

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

Sarah's installation process: 

Download project and unzip
In your terminal, cd to the directory and run the following commands:
```
pip3 install
pip install -r requirements.txt
python3 ballad.py 
```

To change the output of ballad.py, an obvious first step is to change the corpus that is referenced. In our case, we tested this algorithm on a document filled with wine terminology definitions and drink descriptions that can be found in "input/wine.txt"

```
import sys

import oisin

filename = "input/wine.txt"
try:
    filename = sys.argv[1]
except IndexError:
    pass

oisin.balladize(
    oisin.load(filename),
    meter=oisin.iambic(6, 'aabbcc'),
    step=13,
    order=3)
```

We then replaced the input file with descriptions of wine. 


