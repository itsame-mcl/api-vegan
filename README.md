# Pré-Requis

* Python 3.10 ou supérieur

# Installation

```shell
git clone https://gitlab.com/maxence-lagalle/clog-food.git
cd clog-food
pip install -r requirements.txt
```

# Lancement

```shell
python main.py
```

# Points d'accès disponibles

* GET /get_EAN/{produit} : récupère le code EAN de {produit}
* GET /is_vegan/{EAN} : indique si le produit au code {EAN} est vegan ou non